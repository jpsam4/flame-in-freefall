"""Reconocimiento de NTRS: arma un inventario de papers sobre combustión en microgravedad.

Uso:  uv run python prep/recon_ntrs.py [--per-query 50]
Salida: prep/ntrs_inventory.csv (deduplicado por id). No descarga PDFs (eso es T06).
"""

from __future__ import annotations

import csv
import sys
import time
from pathlib import Path

import requests

API = "https://ntrs.nasa.gov/api/citations/search"
QUERIES = [
    "microgravity flame spread spacecraft fire safety",
    "Saffire spacecraft fire experiment",
    "BASS-II burning and suppression of solids",
    "FLEX flame extinguishment droplet microgravity",
    "cool flames International Space Station",
    "SoFIE solid fuel ignition extinction",
    "exploration atmosphere flammability oxygen pressure",
    "smoke aerosol measurement experiment SAME",
    "ACME advanced combustion microgravity experiments",
    "material flammability NASA-STD-6001 microgravity",
]
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "prep" / "ntrs_inventory.csv"


def search(q: str, size: int) -> list[dict]:
    r = requests.get(API, params={"q": q, "page.size": size}, timeout=60)
    r.raise_for_status()
    return r.json().get("results", [])


def year_of(rec: dict) -> str:
    for key in ("publicationDate", "created", "submittedDate"):
        v = rec.get(key)
        if isinstance(v, str) and len(v) >= 4:
            return v[:4]
    pubs = rec.get("publications") or []
    if pubs and isinstance(pubs[0].get("publicationDate"), str):
        return pubs[0]["publicationDate"][:4]
    return ""


def main(argv: list[str]) -> None:
    size = int(argv[argv.index("--per-query") + 1]) if "--per-query" in argv else 50
    seen: dict[str, dict] = {}
    for q in QUERIES:
        try:
            results = search(q, size)
        except requests.RequestException as e:
            print(f"✗ {q!r}: {e}", file=sys.stderr)
            continue
        print(f"{len(results):3d}  {q}")
        for rec in results:
            rid = str(rec.get("id"))
            if rid in seen:
                seen[rid]["queries"] += f" | {q}"
                continue
            downloads = rec.get("downloads") or []
            seen[rid] = {
                "ntrs_id": rid,
                "title": (rec.get("title") or "").strip(),
                "year": year_of(rec),
                "doc_type": rec.get("stiType") or rec.get("stiTypeDetails") or "",
                "has_pdf": bool(rec.get("downloadsAvailable") and downloads),
                "url": f"https://ntrs.nasa.gov/citations/{rid}",
                "queries": q,
            }
        time.sleep(0.5)

    OUT.parent.mkdir(exist_ok=True)
    rows = sorted(seen.values(), key=lambda r: r["year"] or "0000", reverse=True)
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else ["ntrs_id"])
        w.writeheader()
        w.writerows(rows)
    with_pdf = sum(r["has_pdf"] for r in rows)
    print(f"\n{len(rows)} papers únicos ({with_pdf} con PDF) → {OUT.relative_to(ROOT)}")
    print("Siguiente: marcá en una columna 'priority' los ~30 que vamos a procesar.")


if __name__ == "__main__":
    main(sys.argv[1:])
