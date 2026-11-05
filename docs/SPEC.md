# SPEC — Flame in Freefall

> Estado: borrador v2 pre-evento (5/11). Se congela el sábado 14/11 a las 12:00.
> Por qué estas funcionalidades: `STRATEGY.md`. Ajustes del 13/11: `RESOURCE_DAY.md`.

## Problema
NASA corrió décadas de experimentos de fuego en microgravedad (torres de caída, vuelos parabólicos, ISS, naves libres como Cygnus
en Saffire). Los resultados están dispersos en papers, páginas de experimentos y repositorios. Quien diseña un hábitat lunar,
un rover presurizado o una nave a Marte no tiene una forma rápida de responder:
*"en este ambiente, ¿qué sabemos de cómo se comporta un fuego, qué tan sólida es esa evidencia y qué falta?"*

## Pregunta central y métrica
- **Gancho**: "Will it burn on the Moon?"
- **Métrica**: **Evidence Readiness Level (ERL)** por ambiente o celda de condiciones (definición en `STRATEGY.md` §4).
  Mide cuánta evidencia hay; **no** es una predicción de riesgo.

## Usuarios (C1)
1. **Ingeniera/o de seguridad de misión**: evidencia para un ambiente concreto.
2. **Investigador/a o profesor/a**: comparar investigaciones y ver huecos.
3. **Estudiante y jurado**: entender en 30 segundos por qué el fuego en el espacio es distinto.

## Alcance MVP (prioridad en orden)
Cada funcionalidad indica qué objetivo (O) o consideración (C) del challenge cubre.

### F0 — Selector de ambiente *(O1, C6)* · núcleo
- Presets desde `data/environments.yaml`; cada uno muestra su fuente. Los presets con `status: missing` no se muestran.
- También se pueden ingresar condiciones a mano: O₂, presión, flujo, material, gravedad.
- **Aceptación**: elegir "Exploration atmosphere (2012)" muestra 56,5 kPa y 34% O₂ con la cita a Wessel et al. 2018.

### F1 — Explorador y fichas de investigación *(O1, C2, C4, C5)* · núcleo
- Tabla y filtros sobre `Experiment`; agrupación por hardware (CIR, MDCA, MSG).
- Ficha por `Investigation` con los atributos de C2: objetivos, forma y tamaño del combustible, condiciones, variables, sensores y mediciones.
- **Aceptación**: con FLEX y BASS-II cargados, filtrar por rango de O₂, ver conteo y gráfico, y abrir ambas fichas con todos los campos (o "not reported").

### F2 — Ranking de relevancia por ambiente *(O1)* · núcleo
- Entrada: el ambiente de F0. Salida: investigaciones, experimentos y hallazgos rankeados, con el desglose "why this order?".
- Resumen en lenguaje claro generado por LLM **solo** a partir de lo rankeado, con citas inline verificadas.
- **Aceptación**: cada oración del resumen tiene al menos una cita clicable; si no hay evidencia cercana, lo dice.

### F3 — Mapa O₂ × presión con ERL *(C6, diferencial)* · núcleo
- Ensayos como puntos; ambientes de `environments.yaml` como zonas (la base lunar es una región: O₂ ≥ 0,30 y P ≤ 70,3 kPa); ERL por celda.
- **Aceptación**: el gráfico se genera desde `data/processed/` y `environments.yaml`, sin valores hardcodeados.

### F4 — Hallazgos por prevención, detección y supresión *(O3)* · núcleo
- `Finding` verificados agrupados según el marco de NASA (incluye FLEX con CO₂ y He, SAME para humo, BASS para materiales).
- **Aceptación**: al menos 3 hallazgos verificados por grupo, cada uno con cita.

### F5 — Acotamiento de gravedad parcial *(C7, diferencial)* · alta
- Para un ambiente lunar o marciano: evidencia en µg y en 1 g lado a lado, con LUCI (NTRS 20250010653) como único punto de
  gravedad parcial, sus caveats y una mención a FM2 como fuente futura.
- Rótulo fijo: "Bounds, not predictions".
- **Aceptación**: no aparece ningún número interpolado; solo los extremos medidos y el punto de LUCI, cada uno con cita.

### F6 — Dataset listo para modelar *(O2)* · alta
- Descarga de `experiments.csv` y `.parquet`, más diccionario de datos y procedencia por fila (`source_id`, `source_row`, DOI).
- **Aceptación**: el CSV descargado coincide con `data/processed/` y el diccionario documenta cada columna con su unidad.

### F7 — Comparador de investigaciones *(C3)* · media
- 2–3 investigaciones lado a lado: rangos de condiciones superpuestos, similitudes y diferencias.

### F8 — "Where to test next" *(diferencial)* · media
- Celdas de ambientes habitados con ERL bajo → condiciones sugeridas, con la regla de puntaje visible.

### F9 — "Ask the evidence" (`/ask`) · media
- RAG sobre `Finding` + `Experiment`, con citas, que se niega cuando no puede respaldar.
- **Aceptación**: ≥ 80% en `evals/questions.yaml` y 100% de rechazo en las trampas.

### F10 — Aplicaciones en la Tierra *(O4)* · baja
- 3 tarjetas: niebla de agua, detección de humo, equipo de bomberos, cada una con fuente.

## Fuera de alcance
- Fuego de cohetes y propelentes (excluido por el challenge).
- CFD o modelos físicos propios. Interpolación numérica a gravedad parcial.
- ML predictivo entrenado sobre pocas filas (ver ADR-004). El dataset de F6 habilita que otros modelen.
- Procesar video o imágenes crudas de PSI.

## Ranking de relevancia (F2)
Puntaje = `w_c · cercanía_de_condiciones + w_e · calidad_de_evidencia + w_r · aplicabilidad`
- **cercanía**: distancia normalizada en O₂, presión y flujo; penaliza si el material es de otra clase.
- **calidad**: vuelo orbital > nave libre (Saffire) > gravedad parcial (LUCI) > drop tower o parabólico > tierra; dataset > paper revisado > presentación.
- **aplicabilidad**: gravedad del ambiente vs. la del experimento.
- Pesos en `backend/ranking.py` como constantes con nombre; se muestran en la UI.

## Requisitos de la entrega (ver `STRATEGY.md` §5)
- UI y página del proyecto en **inglés**.
- Demo: video de **≤ 30 s** con subtítulos en inglés, o **≤ 7 slides**.
- Funciona sin backend: F0, F1, F3, F4, F5 y F6 son estáticas.

## Métricas de éxito para la demo
- 0 números sin fuente en la UI (test automático).
- ≥ 2 datasets PSI integrados y ≥ 30 papers de NTRS procesados.
- `/ask` ≥ 80% en evals; 100% de rechazo en las trampas.
- Video de 30 s que una persona sin contexto entiende en un solo visionado.

## Preguntas abiertas
- [x] ~~¿Valores de atmósfera de hábitat con fuente?~~ → `data/environments.yaml` (exploración 2005/2012, Shuttle, base lunar, traje).
- [ ] Fuente para la cabina de la ISS y para el rover presurizado.
- [ ] ¿Qué recursos lista NASA el 13/11? → `RESOURCE_DAY.md`.
- [ ] ¿Proveedor de LLM y cuota? (ADR-003)
- [ ] ¿Saffire o CFI-G tienen datos tabulares públicos?
- [ ] Definición final de los umbrales de "cercano" para el ERL.
