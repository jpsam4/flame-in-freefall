# 🔥 Flame in Freefall

**NASA Space Apps Challenge 2026 · Buenos Aires, Argentina**
Challenge: *Flame in Freefall: SI-Powered Fire Safety Insights from Microgravity Combustion Data*

Un dashboard que resume, rankea y explica décadas de experimentos de combustión en microgravedad de NASA
para dar insights de seguridad contra incendios en misiones a la Luna y Marte, donde **cada número y cada
insight enlaza a su fuente** (dataset de PSI con DOI o paper de NTRS con página).

## Estado
Scaffold pre-evento: especificación, contratos, instrucciones para agentes, CI, scripts de reconocimiento y evals.
El código de producto (pipeline, backend, frontend) se desarrolla durante el hackathon (14–15/11).
Ver **Trabajo previo al evento** abajo.

## Mapa del repo
| Ruta | Qué es |
|---|---|
| `AGENTS.md` | Instrucciones canónicas para Claude Code, Codex y Antigravity |
| `CLAUDE.md`, `GEMINI.md` | Overrides por herramienta |
| `.agents/skills/` | Skills compartidas (`.claude/skills` es un symlink) |
| `docs/STRATEGY.md` | Análisis de ganadores, potencial del tópico, propuesta y cumplimiento de la entrega |
| `docs/BRAINSTORM.md` | Ideas, matriz de puntaje y plan hasta el evento (documento vivo) |
| `docs/RESOURCE_DAY.md` | Protocolo para el 13/11, cuando NASA publica los recursos |
| `data/environments.yaml` | Atmósferas de hábitat, vehículo y traje con fuente |
| `docs/SPEC.md` | Qué construimos y criterios de aceptación |
| `docs/DATA_CONTRACT.md` | Esquemas `Source`, `Experiment`, `Finding`, `Scenario` |
| `docs/ARCHITECTURE.md` | Módulos, fronteras y API |
| `docs/DATA_INVENTORY.md` | Reconocimiento de datos de PSI y NTRS |
| `docs/TASKS.md` | Tablero de tareas con prompts listos por agente |
| `docs/EVENT_PLAYBOOK.md` | Checklist pre-evento, horario del finde y guion de demo |
| `docs/DECISIONS.md` | ADRs |
| `docs/AI_LOG.md` | Registro de uso de IA |
| `prep/` | Scripts de reconocimiento de PSI/NTRS |
| `evals/questions.yaml` | Preguntas de evaluación (incluye trampas anti-alucinación) |

## Arranque rápido
```bash
# requisitos: Python 3.11+, uv, (Node 22 para el frontend)
uv sync --all-extras
make check
make recon          # inventario PSI y NTRS → prep/*.csv
```

## Trabajo previo al evento
Todo lo presente en el primer commit fue preparado antes del 14/11/2026: documentación, instrucciones para agentes,
configuración de CI, scripts de reconocimiento de datos y preguntas de evaluación. No incluye código de producto.

## Uso de IA
Usamos Claude Code, OpenAI Codex y Google Antigravity como asistentes de desarrollo, con revisión humana de cada
merge. Detalle en `docs/AI_LOG.md`.

## Datos
Datos de NASA Physical Sciences Informatics (PSI) y NASA Technical Reports Server (NTRS). Las licencias de cada
fuente están en `data/sources.json`.
