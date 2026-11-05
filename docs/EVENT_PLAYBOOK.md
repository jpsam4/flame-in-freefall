# EVENT PLAYBOOK — 14 y 15 de noviembre (Buenos Aires, UTC-3)

## Qué se puede hacer antes del evento
Las reglas oficiales mandan: **leelas en spaceappschallenge.org antes de seguir**. Criterio seguro que usa este repo:
- ✅ Antes: aprender, investigar datos, escribir specs/contratos/instrucciones de agentes, configurar herramientas, CI
  y scripts de reconocimiento (`prep/`). Todo eso es preparación y se declara en el README de entrega.
- ❌ Antes: código de producto (pipeline, backend, frontend). Arranca el sábado.
- Declarar en la entrega qué existía antes (este scaffold) y qué se hizo durante el evento, y el uso de IA (`AI_LOG.md`).

## Checklist pre-evento (hasta el viernes 13)
- [ ] Equipo: definir quién maneja cada carril (Datos/API, UI, Calidad) y quién es "integrador" (mergea).
- [ ] Crear repo en GitHub (privado hasta el evento si las reglas lo piden), subir este scaffold, activar Actions.
- [ ] Instalar y loguear: Claude Code, Codex, Antigravity. Probar que cada uno lee AGENTS.md
      (preguntarle "¿cuál es la regla de oro de este repo?").
- [ ] `uv sync && make check` verde en todas las máquinas.
- [ ] Correr `prep/recon_psi.py` y `prep/recon_ntrs.py` → completar PSI-IDs en `DATA_INVENTORY.md`.
- [ ] Descargar FLEX y BASS-II a `data/raw/psi/...` y verificar SHA-256.
- [ ] Leer: NASA/TP-2015-216046 (FLEX), paper BASS-II (NTRS 20160000593), presentación Saffire IV/V (20210017780).
- [ ] Completar `evals/questions.yaml` con citas esperadas reales de esas lecturas.
- [ ] Decidir proveedor de LLM y cargar créditos (ADR-003). `.env` en cada máquina.
- [ ] **Viernes 13**: seguir el protocolo de `RESOURCE_DAY.md`.
- [ ] Confirmar que todos los integrantes figuran en el evento local de Buenos Aires (no en lista de espera).

## Sábado 14
| Hora | Objetivo | Hito verificable |
|---|---|---|
| 09–10 | Kickoff, congelar SPEC | Preguntas abiertas resueltas |
| 10–12 | T01, T02, T05, T06 en paralelo | Schema + scaffold frontend mergeados |
| 12–15 | T03, T04, T08 | `data/processed/experiments.json` real |
| 15–18 | T07, T09, T10 | Explorador con datos reales en deploy |
| 18–20 | T13, T11 | **Gate 20:00**: si F1 no anda en Next.js → plan B Streamlit (ADR-001) |
| 20–24 | T14, extracción de papers completa | F2 de punta a punta |

## Domingo 15
| Hora | Objetivo | Hito |
|---|---|---|
| 08–11 | T12 evals, T15, T16 | Evals ≥ 80% |
| 11–13 | **Feature freeze 13:00**. Solo bugs | — |
| 13–16 | Deploy final. **Video de ≤ 30 s con subtítulos en inglés** y **≤ 7 slides** en inglés | Video público, sin login |
| 16–19 | Página del proyecto en inglés: summary, descripción, NASA Data, Partner Data, Use of AI. Guardar borrador seguido | Todos los campos completos |
| 19–20 | Probar todos los links en ventana privada. **Enviar a las 20:00** | "Submit for Judging" hecho |

> La guía de entrega más reciente cierra a las **23:59 hora local del domingo** y no acepta cambios después **[verificar 2026]**.
> Un demo que pase los 30 s o las 7 slides queda **fuera del juzgamiento global**. Detalle en `STRATEGY.md` §5.

## Ritmo de trabajo con agentes
- Cada 2 h: el integrador mergea lo aprobado, todos hacen `git pull` y rebase de sus ramas.
- Un agente por worktree, nunca dos agentes en la misma rama.
- Si un agente da vueltas más de 20 min en lo mismo: parar, achicar la tarea, reescribir el prompt.
- Revisión cruzada: Codex revisa PRs de Claude Code y viceversa (`/review` o skill `review-pr`).

## Demo
- **Entrega (obligatorio)**: video de ≤ 30 s, storyboard en `STRATEGY.md` §5. Grabar con la app real, sin imágenes
  generadas con branding de NASA. Si usamos alguna imagen generada por IA, lleva marca de agua visible.
- **Pitch en el evento local (si lo hay)**: preguntar el formato a los organizadores de Buenos Aires. Guion de 2 min:
  1. (15 s) Problema: un fuego en una nave no sube, se vuelve esférico; décadas de datos dispersos. FM2 está por prender el primer fuego en la Luna.
  2. (30 s) Elegir "Base lunar" → mapa O₂ × presión y ERL. "¿Por qué este orden?".
  3. (25 s) Acotamiento de gravedad parcial: µg vs 1 g, con LUCI como único punto real.
  4. (20 s) Clic en una cita → fila del dataset o página del paper. "Cada número es verificable".
  5. (15 s) Pregunta trampa en vivo → el sistema se niega a inventar.
  6. (15 s) "Dónde ensayar después" + descarga del dataset listo para modelar.
