"""Tests de higiene del repo que valen desde antes del evento.

Los tests de esquema, físicos y de procedencia de datos se agregan en T02/T05.
"""

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SOURCE_FIELDS = {"source_id", "kind", "title", "url", "license", "retrieved_at"}
SOURCE_KINDS = {"psi_dataset", "ntrs_paper", "nasa_page", "other"}


def test_agent_instruction_files_exist():
    for name in ("AGENTS.md", "CLAUDE.md", "GEMINI.md"):
        assert (ROOT / name).is_file(), f"falta {name}"
    assert (ROOT / "CLAUDE.md").read_text().lstrip().startswith("@AGENTS.md"), (
        "CLAUDE.md debe importar AGENTS.md en la primera línea"
    )


def test_skills_have_frontmatter():
    skills = list((ROOT / ".agents" / "skills").glob("*/SKILL.md"))
    assert skills, "no hay skills en .agents/skills"
    for s in skills:
        text = s.read_text()
        assert text.startswith("---"), f"{s} sin frontmatter"
        front = yaml.safe_load(text.split("---")[1])
        assert front.get("name") == s.parent.name, f"{s}: name debe coincidir con la carpeta"
        assert front.get("description"), f"{s}: falta description"


def test_sources_json_is_valid():
    sources = json.loads((ROOT / "data" / "sources.json").read_text())
    assert isinstance(sources, list)
    ids = [s["source_id"] for s in sources]
    assert len(ids) == len(set(ids)), "source_id duplicado"
    for s in sources:
        missing = REQUIRED_SOURCE_FIELDS - s.keys()
        assert not missing, f"{s.get('source_id')}: faltan {missing}"
        assert s["kind"] in SOURCE_KINDS
        if s.get("file_path"):
            path = ROOT / s["file_path"]
            assert path.exists(), f"{s['source_id']}: no existe {s['file_path']}"
            if s.get("sha256"):
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                assert digest == s["sha256"], f"{s['source_id']}: el archivo cambió (sha256 no coincide)"


def test_eval_questions_are_well_formed():
    qs = yaml.safe_load((ROOT / "evals" / "questions.yaml").read_text())
    ids = [q["id"] for q in qs]
    assert len(ids) == len(set(ids))
    traps = [q for q in qs if q.get("trap")]
    assert len(traps) >= 3, "necesitamos al menos 3 preguntas trampa"
    for q in qs:
        assert q["question"].strip()
        if not q.get("trap"):
            assert "expected_sources" in q


def test_environments_are_sourced_and_physical():
    envs = yaml.safe_load((ROOT / "data" / "environments.yaml").read_text())
    source_ids = {s["source_id"] for s in json.loads((ROOT / "data" / "sources.json").read_text())}
    for e in envs:
        if e["status"] == "missing":
            assert e["pressure_kpa"] is None and e["o2_mole_fraction"] is None, (
                f"{e['id']}: status missing pero tiene valores"
            )
            continue
        assert e["source_id"] in source_ids, f"{e['id']}: source_id {e['source_id']} no está en sources.json"
        assert 0 < e["o2_mole_fraction"] <= 1, f"{e['id']}: O2 fuera de (0, 1]"
        assert e["pressure_kpa"] > 0, f"{e['id']}: presión <= 0"
        if e.get("pressure_psia") is not None:
            kpa = e["pressure_psia"] * 6.894757
            assert abs(kpa - e["pressure_kpa"]) < 0.1, f"{e['id']}: psia y kPa no coinciden ({kpa:.2f})"


def test_no_synthetic_data_in_processed():
    for f in (ROOT / "data" / "processed").glob("*.json*"):
        assert '"synthetic": true' not in f.read_text(), f"{f.name} contiene datos sintéticos"
