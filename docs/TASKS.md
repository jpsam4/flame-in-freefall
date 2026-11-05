# TASKS

Estados: `todo` · `doing` · `review` · `done`. Rama: `<carril>/<ID>-<slug>`.
Cada tarea trae un **prompt listo** para pegar en el agente. Se ejecutan desde el sábado 14/11 (ver `EVENT_PLAYBOOK.md`).

| ID | Tarea | Carril | Agente | Depende de | Estado |
|---|---|---|---|---|---|
| T00 | Reconocimiento PSI/NTRS + descargar FLEX y BASS-II | Datos | Humano + `prep/` | — | todo (pre-evento) |
| T01 | Scaffold Next.js en `frontend/` | UI | Antigravity | — | todo |
| T02 | `pipeline/schema.py` según DATA_CONTRACT | Datos | Claude Code | — | todo |
| T03 | Ingesta FLEX (PSI-69) | Datos | Claude Code | T02 | todo |
| T04 | Ingesta BASS-II (PSI-25) | Datos | Claude Code | T02 | todo |
| T05 | Tests físicos y de procedencia | Calidad | Codex | T02 | todo |
| T06 | Descarga de papers NTRS + chunking por página | Datos | Codex | T00 | todo |
| T07 | `extract_findings.py` con verificación de fragmento | Datos | Claude Code | T02, T06 | todo |
| T08 | `pipeline/gaps.py` + `run.py` + export a frontend | Datos | Claude Code | T03, T04 | todo |
| T09 | F1 Explorador | UI | Antigravity | T01, T08 | todo |
| T10 | `backend/ranking.py` + `/rank` | API | Claude Code | T08 | todo |
| T11 | `backend/ask.py` + `/ask` con validación de citas | API | Claude Code | T07, T10 | todo |
| T12 | Runner de evals | Calidad | Codex | T11 | todo |
| T13 | F3 Mapa de huecos | UI | Antigravity | T08 | todo |
| T14 | F2 Asesor por escenario | UI | Antigravity | T10 | todo |
| T15 | F4 Tarjetas "por qué es distinto" | UI | Antigravity | T07 | todo |
| T16 | F5 Chat de evidencia | UI | Antigravity | T11 | todo |
| T19 | `investigations.json` + `environments.json` (F0, F1) | Datos | Claude Code | T03, T04 | todo |
| T20 | ERL: fórmula en `backend/erl.py` + tests + campo en `gap_grid` | API | Claude Code | T08 | todo |
| T21 | F5 Acotamiento de gravedad parcial (µg / 1 g / LUCI) | UI | Antigravity | T19, T07 | todo |
| T22 | F6 Export CSV/Parquet + `data_dictionary.md` | Datos | Codex | T08 | todo |
| T17 | Deploy + **video ≤ 30 s** + **≤ 7 slides** | Todos | Humano | T09–T16 | todo |
| T18 | Página de entrega en inglés + AI_LOG + References | Todos | Humano + Claude | T17 | todo |

---

## Prompts

### T02 — Esquema (Claude Code)
```
Tarea T02. Leé AGENTS.md y docs/DATA_CONTRACT.md. Implementá pipeline/schema.py con modelos Pydantic v2
para Source, Measurement, Experiment, Finding y Scenario, exactamente como el contrato (nombres, tipos, enums).
Agregá validadores para los chequeos físicos de AGENTS.md. Escribí tests en tests/test_schema.py que prueben
casos válidos y que fallen con O2 fuera de [0,1], presión <= 0 y flujo negativo. No inventes campos.
Rama data/T02-schema. Terminá con make check verde.
```

### T03 — Ingesta FLEX (Claude Code)
```
Tarea T03. Usá la skill add-data-source. El archivo está en data/raw/psi/PSI-69/ (encoding cp1252).
Leé las rarezas de FLEX en docs/DATA_INVENTORY.md. Creá pipeline/mappings/psi-69-flex-table.yaml (columna → campo,
unidad de origen, conversión) y pipeline/ingest_flex.py que devuelva list[Experiment]. Antes de mapear,
imprimí los encabezados reales y mostrámelos; no asumas nombres de columnas. Si una columna no tiene
significado claro, dejala en measurements con note y avisá. Test con 3 filas reales.
```

### T04 — Ingesta BASS-II (Claude Code)
Igual que T03 con `data/raw/psi/PSI-25/`. BASS-II no tiene velocidad de propagación ni extinción explícita: `null`.

### T05 — Tests de calidad (Codex)
```
Tarea T05. Leé AGENTS.md (chequeos físicos y regla de oro). Escribí tests/test_provenance.py: todo Experiment y
Finding en data/processed/ tiene source_id presente en data/sources.json; todo Source con file_path tiene sha256
que coincide con el archivo. Escribí tests/test_no_synthetic.py: ningún registro en data/processed/ tiene
synthetic: true. Si data/processed/ está vacío, los tests se saltean con pytest.skip y mensaje claro.
```

### T06 — Papers NTRS (Codex)
```
Tarea T06. Con prep/ntrs_inventory.csv (generado por prep/recon_ntrs.py), creá pipeline/fetch_papers.py que
descargue los PDFs con has_pdf=True a data/raw/ntrs/<id>.pdf (gitignored), registre cada uno en data/sources.json
y extraiga texto por página a data/interim/pages/<id>.jsonl ({page, text}). Usar pypdf. Reintentos con backoff.
```

### T07 — Extracción de hallazgos (Claude Code)
```
Tarea T07. Usá la skill extract-findings. Implementá pipeline/extract_findings.py usando backend/llm.py (creá la
interfaz LLMClient si no existe, ver ADR-003). Prompt versionado en pipeline/prompts/extract_findings.md.
Verificación automática de evidence_snippet contra el texto de la página. Corré primero sobre 3 papers y
mostrame 10 Findings para revisión humana antes de procesar el resto.
```

### T08 — Orquestación y huecos (Claude Code)
```
Tarea T08. pipeline/gaps.py: grilla O2 (bins de 0.05) × presión (bins logarítmicos, definilos como constantes)
con n_experiments, n_findings, best_evidence. pipeline/run.py: corre ingestas, normaliza, valida, escribe los
archivos de salida de DATA_CONTRACT.md y build_info.json. make export-frontend copia a frontend/public/data/.
```

### T01 / T09 — Frontend base y Explorador (Antigravity)
```
Leé AGENTS.md y GEMINI.md. Tarea T01: scaffold Next.js App Router + TypeScript + Tailwind en frontend/, export
estático. Layout con nav: Explorar, Escenario, Huecos, Por qué es distinto, Preguntar. Tarea T09: página Explorar
que lee /data/experiments.json y /data/sources.json; filtros por investigación, combustible, rango de O2, presión,
resultado; tabla + un gráfico de dispersión O2 vs presión coloreado por resultado (con leyenda en texto).
Cada fila enlaza a su fuente. Estados vacío/carga/error. Verificá en el navegador a 1280px y 390px, adjuntá capturas.
```

### T10 — Ranking (Claude Code)
```
Tarea T10. backend/ranking.py puro según "Ranking de relevancia" en docs/SPEC.md, pesos como constantes con nombre,
devuelve breakdown por componente. POST /rank en backend/main.py según el contrato de ARCHITECTURE.md.
Tests: el mismo escenario da el mismo orden; un experimento idéntico al escenario queda primero.
```

### T11 — /ask (Claude Code)
```
Tarea T11. backend/ask.py: recuperar top-k Findings verificados + Experiments vía ranking, construir prompt con
SOLO esa evidencia numerada, pedir respuesta con [n] citas, validar que cada [n] exista; reintentar 1 vez; si
falla, refused=true. Si no hay evidencia con score mínimo, refused=true con reason. Tests con un LLMClient falso.
```

### T12 — Evals (Codex)
```
Tarea T12. evals/run_evals.py: lee evals/questions.yaml, llama a /ask, y puntúa: (a) preguntas normales: la
respuesta no es refused y alguna cita coincide con expected_sources (por source_id o investigación);
(b) preguntas trampa (trap: true): refused=true o la respuesta dice explícitamente que no hay evidencia.
Imprime tabla y escribe evals/results.json. Exit code 1 si < 80% normales o < 100% trampas.
```

### T20 — ERL (Claude Code)
```
Tarea T20. Implementá backend/erl.py según la tabla de ERL de docs/STRATEGY.md §4. Los umbrales de "cercano"
(O2 y presión) y el orden de calidad de plataforma van como constantes con nombre. Función pura:
erl(cell_or_environment, experiments, findings) -> {level, reasons[], counts}. Las reasons son las que muestra la UI.
Tests: celda sin evidencia → 1; solo ground → 2; µg cercano con un material → 4. Agregá erl a gap_grid.json.
```

### T21 — Acotamiento de gravedad parcial (Antigravity)
```
Tarea T21 (F5 de docs/SPEC.md). Para un ambiente lunar o marciano, mostrá en tres columnas: evidencia en µg, el punto
de gravedad parcial (LUCI, source_id ntrs-20250010653, con sus caveats) y evidencia en 1 g. Rótulo fijo "Bounds, not
predictions". Prohibido interpolar o dibujar curvas entre puntos. Cada valor con su cita. UI en inglés.
```

### T13–T16 — Resto de UI (Antigravity)
Un prompt por página siguiendo F2–F5 de `docs/SPEC.md`, con la misma regla: nada hardcodeado, cada insight con fuente,
capturas en 1280px y 390px.
