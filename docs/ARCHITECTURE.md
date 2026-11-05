# ARCHITECTURE

## Principio: precomputar todo lo posible
Todo lo pesado (ingesta, normalización, extracción con LLM, rankings base, grilla de huecos) corre **offline**
y deja archivos versionados en `data/processed/`. En vivo solo corren el frontend y dos endpoints
(`/rank` y `/ask`). Si el LLM falla en la demo, todo menos `/ask` sigue andando.

```
            OFFLINE (pipeline/, se corre a mano o en CI)
 ┌──────────────┐   ┌──────────────┐   ┌───────────────┐   ┌────────────────┐
 │ data/raw/    │──▶│ ingest +     │──▶│ normalize +   │──▶│ data/processed │
 │ PSI CSVs     │   │ mappings     │   │ validate      │   │ *.json/parquet │
 │ NTRS PDFs    │──▶│ extract_     │──▶│ (Pydantic,    │   └───────┬────────┘
 └──────────────┘   │ findings LLM │   │ físicos)      │           │
                    └──────────────┘   └───────────────┘           │
            ONLINE                                                 ▼
 ┌──────────────────────────┐   JSON estático     ┌──────────────────────────┐
 │ frontend/ (Next.js)      │◀────────────────────│ frontend/public/data/    │
 │ F1 F3 F4 sin backend     │                     └──────────────────────────┘
 │ F2 F5 → backend          │──── HTTP ──────────▶┌──────────────────────────┐
 └──────────────────────────┘                     │ backend/ (FastAPI)       │
                                                  │ /rank  /ask  /health     │
                                                  │ DuckDB sobre processed/  │
                                                  │ LLMClient (env)          │
                                                  └──────────────────────────┘
```

## Módulos y fronteras
| Módulo | Responsabilidad | Puede importar | No puede |
|---|---|---|---|
| `pipeline/schema.py` | Modelos Pydantic del contrato | pydantic | nada del backend |
| `pipeline/ingest_*.py` | Leer un raw → filas crudas | `schema`, `io` | llamar LLM |
| `pipeline/normalize.py` | Unidades, nombres de combustible, enums | `schema` | I/O |
| `pipeline/extract_findings.py` | Papers → `Finding` vía LLM | `schema`, `backend.llm` | escribir en raw |
| `pipeline/gaps.py` | Grilla de huecos | `schema` | |
| `pipeline/run.py` | Orquesta todo y escribe processed | todo `pipeline` | |
| `backend/ranking.py` | Puntaje de relevancia (puro) | `pipeline.schema` | I/O, LLM |
| `backend/ask.py` | RAG: recuperar → prompt → validar citas | `ranking`, `llm` | |
| `backend/llm.py` | Interfaz `LLMClient` + adaptadores | SDKs | lógica de negocio |
| `backend/main.py` | Rutas FastAPI | todo `backend` | |
| `frontend/` | UI | solo JSON y API HTTP | importar Python |

## API (contrato con el frontend)
```
GET  /health                    → {"status":"ok","build":{...}}
POST /rank   body: Scenario     → {"experiments":[{experiment_id, score, breakdown:{conditions,evidence,applicability}}],
                                    "findings":[{finding_id, score, breakdown}], "weights":{...}}
POST /ask    body: {question, scenario?}
                                → {"answer_md": str, "citations":[{source_id, page?, finding_id?, experiment_id?}],
                                    "refused": bool, "reason": str|null}
```
Regla de `/ask`: después de generar, el backend verifica que cada `[cita]` del texto exista en `citations` y en
`sources.json`. Si falla, reintenta una vez y si vuelve a fallar responde `refused: true`.

## Despliegue para la demo
- Frontend: Vercel o GitHub Pages (export estático) — F1/F3/F4 funcionan sin backend.
- Backend: Render/Fly/Railway o local con túnel. Variable `NEXT_PUBLIC_API_URL`.
- Plan B: video grabado de la demo completa el domingo antes de las 14:00.
