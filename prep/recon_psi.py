"""Reconocimiento de PSI: lista los archivos de cada investigación de combustión.

Uso (desde la raíz del repo, en tu máquina):
    uv run python prep/recon_psi.py                 # recorre PSI-1..PSI-130 y filtra combustión
    uv run python prep/recon_psi.py PSI-25 PSI-69   # solo esas
    uv run python prep/recon_psi.py --download PSI-25 PSI-69   # baja los CSV/XLSX chicos (< 50 MB)

Salida: prep/psi_inventory.csv (una fila por archivo). No modifica data/raw salvo con --download.
La API de metadatos es la que usa el sitio de PSI: /geode-py/ws/repo/investigations/<ID>.
"""

from __future__ import annotations

import csv
import hashlib
import json
import sys
import time
from pathlib import Path

import requests

META_URL = "https://psi.nasa.gov/geode-py/ws/repo/investigations/{pid}"
COMBUSTION_HINTS = (
    "combust",
    "flame",
    "fire",
    "flex",
    "bass",
    "saffire",
    "acme",
    "smoke",
    "same",
    "cool flame",
    "spice",
    "slice",
    "daft",
    "droplet",
    "burn",
)
TABULAR_EXT = (".csv", ".xlsx", ".xls", ".txt", ".json", ".dat")
MAX_DOWNLOAD_BYTES = 50 * 1024 * 1024
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "prep" / "psi_inventory.csv"


def fetch_meta(pid: str) -> dict | None:
    try:
        r = requests.get(META_URL.format(pid=pid), timeout=30)
    except requests.RequestException as e:
        print(f"  {pid}: error de red {e}", file=sys.stderr)
        return None
    if r.status_code != 200:
        return None
    try:
        return r.json()
    except json.JSONDecodeError:
        return None


def looks_like_combustion(meta: dict) -> bool:
    text = json.dumps(meta)[:20000].lower()
    return any(h in text for h in COMBUSTION_HINTS)


def title_of(meta: dict) -> str:
    for key in ("title", "name", "investigation_title", "short_title"):
        if isinstance(meta.get(key), str):
            return meta[key]
    return ""


def resolve_url(f: dict) -> str:
    url = f.get("remote_url") or ""
    if url.startswith("/"):
        url = "https://psi.nasa.gov" + url  # [verificar] base para rutas relativas
    return url


def download(url: str, dest: Path) -> tuple[str, int]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256()
    size = 0
    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(dest, "wb") as fh:
            for chunk in r.iter_content(1 << 16):
                fh.write(chunk)
                h.update(chunk)
                size += len(chunk)
    return h.hexdigest(), size


def main(argv: list[str]) -> None:
    do_download = "--download" in argv
    ids = [a for a in argv if a.upper().startswith("PSI-")]
    scan_all = not ids
    if scan_all:
        ids = [f"PSI-{i}" for i in range(1, 131)]

    rows: list[dict] = []
    for pid in ids:
        meta = fetch_meta(pid)
        time.sleep(0.3)  # ser amables con el servidor
        if not meta:
            continue
        if scan_all and not looks_like_combustion(meta):
            continue
        files = meta.get("added") or []
        print(f"{pid}: {title_of(meta)[:70]!r} — {len(files)} archivos")
        for f in files:
            name = f.get("file_name", "")
            size = f.get("file_size") or 0
            url = resolve_url(f)
            row = {
                "psi_id": pid,
                "investigation_title": title_of(meta),
                "file_name": name,
                "size_bytes": size,
                "subcategory": f.get("subcategory", ""),
                "is_tabular": name.lower().endswith(TABULAR_EXT),
                "url": url,
                "s3_version_id": f.get("s3_version_id", ""),
                "sha256": "",
            }
            if do_download and row["is_tabular"] and int(size) < MAX_DOWNLOAD_BYTES and url:
                dest = ROOT / "data" / "raw" / "psi" / pid / name
                if not dest.exists():
                    print(f"  ↓ {name}")
                    row["sha256"], _ = download(url, dest)
            rows.append(row)

    if not rows:
        print("Sin resultados. ¿Cambió la API? Probá abrir META_URL en el navegador.")
        return
    OUT.parent.mkdir(exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    tab = sum(r["is_tabular"] for r in rows)
    print(f"\n{len(rows)} archivos ({tab} tabulares) → {OUT.relative_to(ROOT)}")
    if do_download:
        print("Registrá cada descarga en data/sources.json (skill add-data-source).")


if __name__ == "__main__":
    main(sys.argv[1:])
