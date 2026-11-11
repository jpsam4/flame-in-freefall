# RESOURCE DAY — viernes 13/11: qué hacer cuando NASA publique los recursos

> Según la ficha del challenge, los recursos oficiales se publican el **viernes 13 de noviembre**. No sabemos la hora:
> revisar la página oficial desde las 8:00 (hora de Buenos Aires) y cada hora después.
> **Regla del día: nada de código de producto.** Solo lectura, triage, documentación y preparación de prompts. El código arranca el sábado.

## Roles del día
| Rol | Qué hace |
|---|---|
| **Vigía** | Monitorea la página y avisa al equipo apenas salen los recursos |
| **Datos** | Hace el triage de datasets y corre `prep/` |
| **Papers** | Hace el triage de papers y lecturas |
| **Integrador** | Actualiza SPEC, TASKS y la decisión final; coordina la reunión |

Con 1–2 personas, una sola hace Vigía + Integrador y la otra Datos + Papers.

---

## Protocolo (T0 = momento en que salen los recursos)

### T0 → T0+30 min · Capturar
1. Copiar **toda** la lista de recursos a `prep/resources_2026-11-13.md` (nombre, URL, agencia, tipo, descripción). Tal cual, sin filtrar.
2. Copiar el texto de la página oficial y compararlo con `docs/challenge/OFFICIAL_TEXT_2026-11-11.md`
   (`diff` o el prompt del final). Si cambió, guardarlo como `OFFICIAL_TEXT_2026-11-13.md` y anotar las diferencias arriba
   de todo, en negrita. Si no cambió, anotar "sin cambios".
3. Avisar al equipo: "Salieron los recursos: N datasets, M papers, cambios en el texto: sí/no".

### T0+30 → T0+2 h · Triage
Llenar esta tabla en `prep/resources_2026-11-13.md` (un agente puede hacer el primer borrador con el prompt del final):

| Recurso | Tipo | Cubre | ¿En el mapa O₂ × P cae cerca de algún hábitat? | Esfuerzo | Valor | Decisión |
|---|---|---|---|---|---|---|
| ej. PSI-69 FLEX | tabla | O1 O2 C6 | sí/no/parcial | S/M/L | A/M/B | **núcleo** / extra / descartar |

- **Tipo**: tabla · paper · página web · imágenes/video · herramienta/API · dataset de otra agencia.
- **Cubre**: IDs de objetivos y consideraciones de `STRATEGY.md` §1 (O1–O4, C1–C7).
- **Criterio de decisión**:
  - **Núcleo** = tabular o con condiciones extraíbles, y cubre O1, O2 o C6/C7. Va el sábado a la mañana.
  - **Extra** = suma, pero no es imprescindible. Va el domingo si hay tiempo.
  - **Descartar** = videos e imágenes crudas pesadas, fuera de alcance (propelentes) o duplicados.

En paralelo, el rol Datos corre:
```bash
uv run python prep/recon_psi.py PSI-xx PSI-yy            # IDs que aparezcan en los recursos
uv run python prep/recon_psi.py --download PSI-xx PSI-yy # solo tablas chicas
uv run python prep/recon_ntrs.py                          # si sumaron papers, agregar queries o IDs
```
y registra cada archivo descargado en `data/sources.json` (skill `add-data-source`).

### T0+2 h · Elegir rama
| Rama | Qué vemos en los recursos | Qué cambiamos |
|---|---|---|
| **A** | Lo esperado: PSI + NTRS, sin tablas nuevas | Plan intacto. Seguir `TASKS.md` |
| **B** | **Tablas nuevas** (Saffire, ACME, CFI-G, SAME…) | Una tarea de ingesta por tabla (copiar el prompt de T03). Prioridad máxima si tiene datos cerca de la base lunar (alto O₂, baja presión) |
| **C** | **Lista curada de papers** | Esos papers son el primer lote de extracción (T07): los jueces los conocen. Sumarlos a `evals/questions.yaml` |
| **D** | **Datos de agencias socias** (ESA, JAXA, CSA, etc.) | Integrar al menos uno: completa el campo "Space Agency Partner Data" de la entrega |
| **E** | **Datos de gravedad parcial** (LUCI, FM2, drop towers con centrífuga) | Subir la prioridad del acotamiento de gravedad parcial (C7) a núcleo |
| **F** | El texto del challenge **acota o cambia** el alcance | Volver a la matriz de cumplimiento (`STRATEGY.md` §4): primero O1–O3, y "dónde ensayar después" pasa a extra |

Pueden darse varias ramas a la vez (por ejemplo, B + C).

### T0+2,5 h · Reunión de equipo (30 min)
1. (5 min) Cambios en el texto del challenge.
2. (10 min) Tabla de triage: confirmar núcleo, extra y descartes.
3. (10 min) Rama elegida → qué tareas entran, salen o cambian en `TASKS.md`.
4. (5 min) Quién arranca qué el sábado a las 9:00 y con qué agente.

### T0+3 h → noche · Dejar todo listo
- [ ] Actualizar `docs/DATA_INVENTORY.md` con los recursos nuevos.
- [ ] Actualizar `docs/SPEC.md`: cerrar las "Preguntas abiertas" y ajustar los criterios de aceptación.
- [ ] Actualizar `docs/TASKS.md`: tareas nuevas con su prompt, dependencias y carril.
- [ ] Actualizar `data/environments.yaml` si los recursos traen atmósferas de hábitat o rover con otra fuente.
- [ ] Completar `evals/questions.yaml` con preguntas sobre los recursos nuevos.
- [ ] Commit `docs: resource day triage` (es documentación, no producto).
- [ ] Revisar que cada máquina tenga las herramientas logueadas, `.env` cargado y `make check` en verde.
- [ ] **Dormir.** El sábado es largo.

---

## Prompt para el primer borrador del triage (cualquier agente)
```
Leé docs/STRATEGY.md (sección 1: objetivos O1–O4 y consideraciones C1–C7) y prep/resources_2026-11-13.md.
Para cada recurso completá la tabla de triage de docs/RESOURCE_DAY.md: Tipo, Cubre (IDs), si tiene datos cerca de
los ambientes de data/environments.yaml, Esfuerzo, Valor y una Decisión propuesta con una línea de justificación.
No inventes contenido de los recursos: si no podés abrir uno, poné "no verificado". No escribas código.
Al final, decime qué rama (A–F) se aplica y por qué.
```

## Prompt para comparar el texto del challenge
```
Compará el texto oficial pegado abajo con docs/challenge/OFFICIAL_TEXT_2026-11-11.md. Listá solo las diferencias: objetivos
nuevos, eliminados o reformulados, consideraciones nuevas y cambios de alcance. Para cada una, qué parte de
docs/SPEC.md habría que ajustar.
<pegar texto oficial>
```
