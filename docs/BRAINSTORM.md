# BRAINSTORM — cómo ganar con un diferencial real

> Documento vivo hasta el viernes 13/11. Se edita, no se reescribe: las ideas descartadas se tachan y se explica por qué.
> El sábado 14 a las 12:00 lo que quede en "Decisión" pasa a `SPEC.md`.

---

## 1. Contra qué nos miden
Criterios oficiales de Space Apps, que usan los jueces locales y globales:

| Criterio | Qué preguntan | Cómo lo atacamos |
|---|---|---|
| **Influence** | Escala y calidad del impacto | Que sirva para decidir algo real (diseño de hábitat, próximo experimento) |
| **Creativity** | Qué tan novedoso es frente a lo que existe | No ser "otro chat sobre papers" (ver §2) |
| **Validity** | ¿Es científicamente sólido? ¿Funciona? | Trazabilidad, verificación de citas, honestidad sobre los huecos |
| **Relevance** | Responde al challenge, completo, usable | Dashboard que **resume, rankea y explica** (las 3 palabras del challenge) |
| **Presentation** | Cómo contamos la historia (pesa igual que el resto) | Demo de 2 min con un momento "wow" claro |

Premios globales a los que apuntamos: **Best Use of Science** (método), **Best Use of Data** (datos de NASA accesibles),
**Best Mission Concept** si la parte de "próximo experimento" queda bien.

Para la entrega: la página del proyecto va en **inglés**. El video puede estar en español si tiene subtítulos en inglés.
Todos los recursos externos se listan en References.

## 2. Qué ya existe, para no repetirlo
Hay muchos repos públicos de 2026 sobre este challenge. Patrones que se repiten:
- Chat/RAG sobre papers con citas "decorativas" (no verificadas).
- Dashboard Streamlit con FLEX y BASS-II y algunos gráficos.
- Simuladores físicos 2D o números adimensionales (Grashof, Damköhler).
- Ranking de papers por BM25 o puntaje de "importancia".

**Conclusión**: el dashboard con chat es la base mínima, no el diferencial. Hay que ganar en algo que los demás no hacen.

## 3. Principios para elegir idea
1. **Que responda una pregunta que un ingeniero de NASA se haría de verdad**, no una pregunta de demo.
2. **Que la IA haga algo que no se puede hacer con un filtro de tabla.**
3. **Que sea defendible ante un científico**: si un juez experto pregunta "¿de dónde sale eso?", siempre hay respuesta.
4. **Que se pueda mostrar en 20 segundos.**
5. **Que entre en 48 h con 2–6 personas y agentes.**

---

## 4. Banco de ideas

### I1 — Asesor de evidencia por escenario *(ya en SPEC, F2)*
Definís condiciones de cabina y el sistema rankea la evidencia aplicable, explica el orden y resume con citas verificadas.
- ➕ Responde exactamente al challenge. Base sólida.
- ➖ Solo, es parecido a lo que hacen otros, aunque mejor ejecutado.

### I2 — "Lo que no sabemos": mapa de huecos → próximo experimento ⭐
Se cruza la cobertura de evidencia (O₂ × presión × flujo × material × gravedad) con las atmósferas propuestas para
hábitats de exploración. El sistema dice **dónde hay más riesgo con menos evidencia** y propone el próximo experimento
de mayor valor: condiciones, material, plataforma posible y qué paper o dataset cubriría.
- ➕ Muy original. Le habla directo a NASA (Influence) y es ciencia honesta (Validity). Encaja con *Best Mission Concept*.
- ➖ Requiere valores de atmósfera de hábitat **con fuente**. Hay que definir bien "riesgo" sin inventar física.
- Hipótesis a validar: las atmósferas propuestas para exploración (menor presión y mayor O₂ que la ISS) caen en zonas
  con poca evidencia en microgravedad. **[verificar con datos]**

### I3 — Brecha tierra ↔ microgravedad ("¿el ensayo de tierra te miente?")
Los materiales para naves se aprueban con ensayos en 1 g. Se compara qué dicen esos ensayos y qué mostraron los
experimentos en microgravedad (BASS, Saffire), por ejemplo si un material que "pasa" en tierra puede sostener una llama
con ventilación en microgravedad.
- ➕ Es *el* insight de seguridad que importa, y se cuenta muy bien en una demo.
- ➖ Depende de encontrar pares material/condición comparables con fuente. Riesgo de sobreafirmar.
- Validación: buscar en NTRS papers que comparen explícitamente límites de inflamabilidad en 1 g y µg. **[verificar]**

### I4 — Gemelo de módulo / hábitat
Un plano simple de un módulo con zonas (ventilación, materiales, equipos). Cada zona se colorea según la evidencia
aplicable, y al hacer clic se ve el "por qué" con citas.
- ➕ Muy visual (Presentation, Art & Technology).
- ➖ Fácil de que parezca un juguete o una simulación que no es. Lleva mucho tiempo de UI.
- Mejor uso: como **capa de presentación de I2**, no como idea en sí.

### I5 — Revisión sistemática viva con grado de evidencia
Cada hallazgo lleva un grado (vuelo orbital > nave libre > torre de caída > tierra > modelo) y un acuerdo o desacuerdo
entre fuentes. Se muestran las **contradicciones** entre papers.
- ➕ Best Use of Science. Detectar contradicciones es algo que un filtro no puede hacer.
- ➖ La extracción de contradicciones con LLM es frágil y necesita revisión humana.
- Mejor uso: **motor interno** que alimenta I1 e I2.

### I6 — Tarjetas de decisión para tripulación
"Primeros 60 segundos ante humo en microgravedad", basado en evidencia.
- ➖ **Descartar como producto**: dar instrucciones de seguridad operativas sin ser NASA es riesgoso y poco creíble.
  Sirve como storytelling (F4), siempre como "qué dice la evidencia" y no como "qué hacer".

### I7 — Ángulo local: bases antárticas como análogo
Hábitats aislados y confinados, con ventilación cerrada y lejos de ayuda. Argentina opera bases en la Antártida.
- ➕ Local Impact Award y buena historia para el evento de Buenos Aires.
- ➖ Las condiciones físicas (con gravedad) son distintas y se puede forzar la analogía. Hay que confirmar antecedentes
  de incendios con fuente. **[verificar]**
- Mejor uso: **una diapositiva** de impacto en la Tierra, no una funcionalidad.

---

## 5. Matriz de puntaje (1–5)
Primera pasada mía. **Re-puntuar en equipo** (§9).

| Idea | Influence | Creativity | Validity | Relevance | Presentation | Factible 48 h | Total |
|---|---|---|---|---|---|---|---|
| I1 Asesor | 3 | 2 | 4 | 5 | 3 | 5 | 22 |
| **I2 Huecos → próximo experimento** | **5** | **5** | 4 | 4 | 4 | 3 | **25** |
| I3 Brecha tierra/µg | 4 | 4 | 3 | 4 | 5 | 2 | 22 |
| I4 Gemelo de módulo | 3 | 3 | 2 | 3 | 5 | 2 | 18 |
| I5 Revisión viva | 3 | 3 | 5 | 4 | 2 | 3 | 20 |
| I7 Antártida | 2 | 3 | 2 | 1 | 4 | 4 | 16 |

---

> **Actualización 5/11**: el análisis de ganadores y del texto oficial refuerza I2 y suma dos cosas: una métrica central
> (Evidence Readiness Level) y el acotamiento de gravedad parcial (C7). Propuesta refinada en `STRATEGY.md` §4. La I3 ahora
> tiene un ancla concreta: FM2 se diseñó para responder justamente esa pregunta.

## 6. Mi recomendación (propuesta, no decisión)

**"La IA que sabe lo que no sabe."**

Combinamos las ideas en un ciclo que nadie más está cerrando:

```
  EVIDENCIA            →        RIESGO DE ESCENARIO        →        HUECOS          →     PRÓXIMO EXPERIMENTO
  (I5: hallazgos            (I1: condiciones de cabina        (I2: dónde el hábitat      (I2: qué ensayo daría
   graduados y                → evidencia rankeada              cae en zona sin             más información,
   verificados)                 con citas)                       evidencia)                  con justificación)
```

- **Base que tiene que andar sí o sí**: I1 + I5 en versión simple (grado de evidencia por plataforma).
- **Diferencial**: I2. Es el "momento wow" de la demo: *"este hábitat propuesto cae acá, donde hay N experimentos de
  microgravedad; este es el ensayo que más reduciría la incertidumbre"*.
- **Si los datos dan**: I3 como insight estrella en las tarjetas F4.
- **Capa visual opcional**: I4 solo si sobra tiempo el domingo a la mañana.
- **Pitch**: I7 en una diapositiva.

¿Por qué esta y no otra? Responde las tres palabras del challenge (resume, rankea, explica) y suma una cuarta que nadie
hace: **recomienda**. Además, convierte la honestidad sobre los límites (nuestra regla de oro) en una funcionalidad,
en vez de que sea una limitación.

### Riesgos y criterios de corte
| Riesgo | Señal temprana | Qué hacemos |
|---|---|---|
| No hay valores de atmósfera de hábitat con fuente | Para el 9/11 no encontramos ninguno citable | I2 usa escenarios definidos por el usuario, sin presets "oficiales" |
| "Valor de información" suena a física inventada | Un juez lo pregunta y no tenemos fórmula simple | Usar un puntaje transparente: distancia al experimento más cercano × grado de evidencia. Mostrar la fórmula |
| Pocos datos tabulares (solo FLEX y BASS-II) | El inventario PSI no suma más tablas | Los hallazgos de papers (con condiciones extraídas) también cuentan como cobertura |
| I3 no encuentra pares comparables | Para el 11/11 hay menos de 3 pares con fuente | I3 pasa a ser una tarjeta narrativa, no una funcionalidad |

---

## 7. Preguntas para validar antes del evento
Cada una tiene responsable y fecha. Las respuestas van en §10.

- [ ] **P1** ¿Qué atmósferas (presión, O₂) propuso NASA para hábitats y vehículos de exploración? Buscar en NTRS
      "exploration atmosphere" con fuente citable. *(→ I2)*
- [ ] **P2** ¿Cuántos ensayos de FLEX y BASS-II caen cerca de esas atmósferas? Correr con las tablas reales. *(→ I2)*
- [ ] **P3** ¿Hay papers que comparen límites de inflamabilidad 1 g vs µg para el mismo material? *(→ I3)*
- [ ] **P4** ¿Saffire publicó resultados tabulares (velocidad de propagación, materiales) o solo presentaciones? *(→ I2/I3)*
- [ ] **P5** ¿Qué hace un ingeniero de seguridad hoy para responder "¿qué sabemos de X condición?" Si conocen a alguien
      (CONAE, facultad de ingeniería, bomberos), hacer una charla de 15 min. *(→ Influence)*
- [ ] **P6** ¿Qué recursos lista NASA para el challenge el 13/11? *(→ todo)*
- [ ] **P7** ¿Antecedentes documentados de incendios en bases antárticas? Solo si hay tiempo. *(→ I7)*

---

## 8. Plan día por día hasta el evento

| Día | Foco | Salida concreta |
|---|---|---|
| **Jue 5** | Este documento + scaffold | `BRAINSTORM.md` v1 |
| **Vie 6** | Correr `prep/recon_psi.py` y `prep/recon_ntrs.py`; bajar FLEX y BASS-II | `prep/*_inventory.csv`; PSI-IDs completos en `DATA_INVENTORY.md` |
| **Sáb 7** | Leer: TP de FLEX, paper BASS-II, Saffire IV/V. Responder P1 y P4 | Notas en §10 |
| **Dom 8** | Sesión de brainstorming en equipo (§9), re-puntuar la matriz | Decisión provisoria en §11 |
| **Lun 9** | Responder P2 a mano (planilla), es la prueba de fuego de I2 | Sí/no sobre I2 |
| **Mar 10** | Responder P3. Bocetos en papel de la demo (5 pantallas) | Storyboard |
| **Mié 11** | Ajustar SPEC y TASKS según la decisión. Completar `evals/questions.yaml` con citas reales | SPEC v2 |
| **Jue 12** | Ensayo de herramientas: cada agente lee AGENTS.md y responde la regla de oro. Pitch de 2 min en voz alta | Checklist pre-evento cerrada |
| **Vie 13** | Protocolo de `RESOURCE_DAY.md` (P6) | Triage hecho, rama elegida, SPEC y TASKS actualizados |

---

## 9. Formato para las sesiones de brainstorming en equipo (60 min)
1. **(10 min)** Cada uno, en silencio, escribe 3 ideas en una línea: *"para [usuario] que necesita [decisión], mostramos [cosa]"*.
2. **(15 min)** Se leen todas sin debatir. Se agrupan las parecidas.
3. **(15 min)** Se puntúa con la matriz de §5. Cada uno solo, después se promedia.
4. **(10 min)** "Abogado del diablo" sobre la ganadora: ¿qué preguntaría un juez de NASA para destruirla?
5. **(10 min)** Se define la prueba más barata que la confirma o la mata, con responsable y fecha.

Regla: ninguna idea se descarta sin escribir el motivo.

---

## 10. Hallazgos de la investigación
*(Se completa a medida que respondemos §7.)*

| Fecha | Pregunta | Hallazgo | Fuente |
|---|---|---|---|
| 5/11 | P1 | Atmósfera de exploración: 8,2 psia (56,5 kPa) con 34% O₂, por encima del 31,4% de "tasa de quemado sin aumento". El texto del challenge da para la base lunar ≈30% O₂ o más a ≤10,2 psi, y para trajes 100% O₂ a 4,3 psi. Cargado en `data/environments.yaml` | Wessel et al. 2018; texto del challenge |
| 5/11 | — | **El propio challenge pide I2.** Las consideraciones C6 (O₂ y presión) y C7 (gravedad parcial, acotar con µg y 1 g) coinciden con nuestro mapa de huecos | `STRATEGY.md` §1 |
| 5/11 | P3 (parcial) | FM2 busca justamente vincular los ensayos en 1 g con la gravedad reducida. Según NASA, el modelado sugiere que algunos materiales arderían con menos O₂ en gravedad lunar. LUCI (2025) midió propagación más lenta en gravedad parcial que en 1 g, sin concluir mayor inflamabilidad | Página de FM2; NTRS 20250010653 |
| 5/11 | — | Análisis de ganadores 2023–2025: gana el insight no obvio y la métrica de decisión, no el buscador con chat | `STRATEGY.md` §2 |
| 5/11 | — | **Demo de entrega: ≤ 30 s o ≤ 7 slides**; si se pasa, queda fuera del juzgamiento global | Guía de entrega |
| 11/11 | — | **Texto oficial completo**: los objetivos no cambian. Lo nuevo: el problema en tres verbos (encontrar, comparar, interpretar), se rankean investigaciones, asignación oficial prevención/detección/supresión, el rover comparte la atmósfera de la base lunar, y la pregunta "¿qué variaron y qué mantuvieron?" | `docs/challenge/OFFICIAL_TEXT_2026-11-11.md`; `STRATEGY.md` §1.1 |
| 11/11 | — | **"Mismo O₂ para los pulmones, más O₂ para el fuego"**: la base lunar (30% a 70,3 kPa) tiene la misma ppO₂ que el aire a nivel del mar (21,1 vs 21,2 kPa), con 1,44× la fracción de O₂. Es el insight visual del mapa F3 | Cálculo sobre `environments.yaml`; `STRATEGY.md` §3.6 |
| 11/11 | — | Gancho del pitch: 3 de los 4 incidentes que cita el texto oficial (Apollo 1, Apollo 13, Mir) involucran oxígeno | Texto oficial |

## 11. Decisión
*(Vacío hasta la sesión del domingo 8.)*

- Idea elegida:
- Por qué:
- Qué descartamos y por qué:
- Prueba que la confirmó:
