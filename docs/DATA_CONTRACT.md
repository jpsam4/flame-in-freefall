# DATA CONTRACT

Contrato entre carriles. Los modelos Pydantic en `pipeline/schema.py` (a crear el 14/11, tarea T02) deben
implementar exactamente esto. Cambios = ADR en `DECISIONS.md` + aviso a todos los carriles.

Convenciones: unidades en el nombre del campo, fracciones en [0, 1], fechas ISO 8601, `null` = desconocido.

## Source
Toda pieza de información apunta a un `Source`. Se guardan en `data/sources.json` (lista).

| Campo | Tipo | Notas |
|---|---|---|
| `source_id` | str | Único. Ej. `psi-69-flex-table`, `ntrs-20210017780` |
| `kind` | enum | `psi_dataset` \| `ntrs_paper` \| `nasa_page` \| `other` |
| `title` | str | |
| `url` | str | Página humana |
| `doi` | str \| null | Ej. `10.60555/mbq8-0451` |
| `ntrs_id` | str \| null | |
| `license` | str \| null | Copiado de los metadatos, no asumido |
| `file_path` | str \| null | Relativo a la raíz del repo; null si no se versiona (archivo grande) |
| `sha256` | str \| null | |
| `size_bytes` | int \| null | |
| `encoding` | str \| null | Ej. `cp1252` para FLEX |
| `retrieved_at` | datetime | |
| `notes` | str | Rarezas de columnas, caveats |

## Investigation
Ficha por investigación (F1, consideraciones C2 y C5). `data/processed/investigations.json`.

| Campo | Tipo | Notas |
|---|---|---|
| `investigation` | str | `FLEX`, `BASS-II`, ... (misma clave que en `Experiment`) |
| `full_name` | str | |
| `psi_id` | str \| null | `PSI-69` |
| `hardware` | enum \| null | `CIR` \| `MDCA` \| `MSG` \| `free_flyer` \| `other` |
| `platform` | enum | Mismo enum que `Experiment` |
| `combustion_type` | enum | Mismo enum que `Experiment` |
| `objectives` | str \| null | Texto de la fuente, resumido y citado |
| `fuel_geometries` | list[str] | |
| `fuel_dimensions` | str \| null | Ej. "droplet diameter 2–5 mm" (solo si la fuente lo dice) |
| `condition_ranges` | object | `{o2_mole_fraction: [min, max], pressure_kpa: [...], flow_velocity_cm_s: [...]}`, calculado desde `Experiment` |
| `sensors_measurements` | list[str] | |
| `fire_safety_layer` | list[enum] | `prevention` \| `detection` \| `suppression` |
| `n_experiments` | int | |
| `source_ids` | list[str] | |

## Environment
Ambiente habitado de referencia (F0). Fuente: `data/environments.yaml` (se valida en `tests/test_repo_contract.py`).
Campos: `id`, `name`, `pressure_psia`, `pressure_kpa`, `o2_mole_fraction`, `gravity_regime`, `source_id`, `status`, `note`.

## Experiment
Una fila = un ensayo (test) de un experimento. `data/processed/experiments.parquet` (+ `.json` para el frontend).

| Campo | Tipo | Notas |
|---|---|---|
| `experiment_id` | str | `<investigation>-<test_id>` |
| `investigation` | str | `FLEX`, `BASS-II`, `SAFFIRE-IV`, ... |
| `test_id` | str | Tal cual el archivo de origen |
| `platform` | enum | `iss` \| `free_flyer` \| `drop_tower` \| `parabolic` \| `sounding_rocket` \| `suborbital_spin` \| `lunar_surface` \| `ground` |
| `gravity_regime` | enum | `microgravity` \| `lunar` \| `martian` \| `earth` |
| `combustion_type` | enum | `solid_flame_spread` \| `droplet` \| `gas_jet` \| `smoke` \| `other` |
| `fuel` | str | Nombre normalizado (ver `pipeline/mappings/fuels.yaml`) |
| `fuel_raw` | str | Tal cual el archivo |
| `fuel_geometry` | str \| null | `thin_sheet`, `rod`, `sphere`, `droplet`, ... |
| `o2_mole_fraction` | float \| null | [0, 1] |
| `pressure_kpa` | float \| null | > 0 |
| `diluent` | str \| null | `N2`, `He`, `CO2`, ... |
| `diluent_mole_fraction` | float \| null | |
| `flow_velocity_cm_s` | float \| null | ≥ 0 |
| `flow_configuration` | enum \| null | `opposed` \| `concurrent` \| `quiescent` \| `coflow` |
| `outcome` | enum \| null | `sustained` \| `extinguished` \| `no_ignition` \| `disruption` \| `other` |
| `measurements` | dict[str, Measurement] | Ver abajo |
| `source_id` | str | FK → Source |
| `source_row` | int \| null | Fila del archivo de origen (1-based, sin header) |
| `status` | enum | `ok` \| `missing` \| `suspect` |

### Measurement
`{ "value": float, "unit": str, "name_raw": str, "note": str | null }`
Ej.: `measurements["burning_rate_constant"] = {"value": 0.62, "unit": "mm2/s", "name_raw": "Burning rate; mm"}`
(valor ilustrativo de formato, no un dato).

## Finding
Hallazgo extraído de un paper. `data/processed/findings.jsonl`.

| Campo | Tipo | Notas |
|---|---|---|
| `finding_id` | str | |
| `claim` | str | Una afirmación en lenguaje claro, ≤ 40 palabras |
| `safety_implication` | str \| null | Qué significa para la tripulación/diseño |
| `topic` | enum | `flame_spread` \| `extinction` \| `ignition` \| `smoke_toxicity` \| `suppression` \| `cool_flames` \| `ventilation` \| `material_flammability` \| `other` |
| `conditions` | object | Mismos campos de condición que `Experiment` (todos opcionales) |
| `gravity_regime` | enum | Obligatorio |
| `evidence_type` | enum | `flight_experiment` \| `ground_experiment` \| `model` \| `review` |
| `source_id` | str | FK → Source (paper) |
| `page` | int | Página del PDF |
| `evidence_snippet` | str | Textual, ≤ 25 palabras |
| `extracted_by` | str | `<modelo>@<versión-prompt>` o `human:<nombre>` |
| `extracted_at` | datetime | |
| `status` | enum | `verified` \| `unverified` \| `rejected` |
| `needs_human_review` | bool | |
| `human_reviewed_by` | str \| null | |

## Scenario (entrada del asesor, F2)
| Campo | Tipo |
|---|---|
| `name` | str |
| `o2_mole_fraction` | float |
| `pressure_kpa` | float |
| `flow_velocity_cm_s` | float |
| `material_class` | str \| null |
| `gravity_regime` | enum |
| `preset_source_id` | str \| null — obligatorio si es un preset |

## Archivos de salida (lo que consume el frontend)
- `data/processed/experiments.json` y `experiments.csv` / `.parquet` (descarga de F6) + `data_dictionary.md`
- `data/processed/investigations.json`
- `data/processed/environments.json` (copia validada de `data/environments.yaml`)
- `data/processed/findings.json` (solo `status == "verified"`)
- `data/processed/sources.json` (copia de `data/sources.json`)
- `data/processed/gap_grid.json` — celdas `{o2_bin, pressure_bin, n_experiments, n_findings, best_evidence, erl}`
- `data/processed/build_info.json` — fecha, commit, conteos
