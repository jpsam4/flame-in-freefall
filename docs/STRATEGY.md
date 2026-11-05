# STRATEGY — ganadores previos, potencial del tópico y cómo cumplir lo pedido

> Investigación del 5/11/2026. Complementa `BRAINSTORM.md`: allá se generan ideas, acá se explica por qué elegimos lo que elegimos.
> Fuentes al final. Lo marcado **[verificar]** se confirma el 13/11 con la página oficial.

---

## 1. Lo que pide el challenge (texto oficial resumido)

Resumido de la ficha oficial, replicada por el evento local de Athlone. **La página de spaceappschallenge.org es la palabra final.**

**Pedido central**: un dashboard web impulsado por SI que **resuma, rankee e interprete** décadas de resultados de llamas en
microgravedad de NASA, para apoyar la seguridad contra incendios en la exploración humana.

**Objetivos**
| ID | Objetivo |
|---|---|
| O1 | Identificar las investigaciones más relevantes para la seguridad contra incendios en **ambientes habitados**: naves, estaciones, bases en Luna y Marte, **rovers presurizados** |
| O2 | **Extraer datos que sirvan para modelado predictivo** de inflamabilidad y escenarios de incendio |
| O3 | Destacar la investigación que informa **controles y equipos de seguridad** de próxima generación |
| O4 | *(Opcional)* Aplicaciones en la Tierra: extintores de niebla de agua, detección de humo, equipo de bomberos |
| — | **Fuera de alcance**: incendios de cohetes y propelentes |

**Consideraciones (opcionales, pero son lo que el autor del challenge tiene en la cabeza)**
| ID | Consideración |
|---|---|
| C1 | Audiencia: profesores, estudiantes de grado y posgrado, investigadores e ingenieros aeroespaciales |
| C2 | Atributos a mostrar: objetivos del experimento, **forma y tamaño del combustible**, condiciones (O₂, flujo de aire), variables dentro y entre investigaciones, **sensores y mediciones** |
| C3 | **Similitudes y diferencias entre investigaciones** |
| C4 | Otras investigaciones de PSI: DAFT/DAFT-2 (polvo), ACME BRE |
| C5 | **Agrupar por hardware**: ACME → CIR · FLEX, FLEX-2, CFI → MDCA dentro del CIR · BASS, BASS-II, SPICE, SLICE → MSG con ducto de flujo |
| C6 | **O₂ y presión**: trajes con 100% O₂ a 4,3 psi; bases lunares con ≈30% O₂ o más a ≤10,2 psi; los ensayos de mayor O₂ en microgravedad (hasta 85%) son de CFI-G |
| C7 | **Gravedad parcial**: PSI no tiene datos de combustión en gravedad parcial (las fuentes futuras serían LUCI y FM2); ACME E-FIELD imita gravedad parcial con un campo eléctrico; **los resultados de µg y 1 g pueden acotar los niveles intermedios** |

**Lectura estratégica**: C6 y C7 son, casi palabra por palabra, nuestra idea I2 (mapa O₂ × presión con los hábitats encima, y huecos
de gravedad parcial). El autor del challenge está pidiendo ese análisis. La mayoría de los equipos va a hacer un buscador con chat
y no va a llegar ahí.

---

## 2. Qué hicieron los ganadores globales (2023–2025)

Revisé los 30 ganadores globales. No hay justificaciones por proyecto de los jueces: los patrones salen de las descripciones
oficiales y del artículo "Meet the 2025 Global Winners".

### Los casos más parecidos a nuestro challenge
| Año · Premio | Proyecto | Qué hicieron | Lección para nosotros |
|---|---|---|---|
| 2025 · Best Use of Science | **SpaceGenes+** (Alemania, **1 persona**) | Challenge "Build a Space Biology Knowledge Engine", con la **misma forma que el nuestro** (dashboard sobre publicaciones de NASA). No ganó por buscar mejor: mostró **efectos sinérgicos** de radiación + microgravedad juntas, que no aparecen con cada factor por separado. Diseño y visualización cuidados | **Un insight científico no obvio le gana a un buen buscador.** Nuestro análogo: la base lunar **combina** baja presión, O₂ alto, gravedad parcial y ventilación baja. Casi nadie ensayó esa combinación |
| 2025 · Best Mission Concept | **PureFlow** (Brasil) | Plataforma para diseñar hábitats y **ponerlos a prueba contra amenazas reales** (tormentas solares). De lo teórico a la resiliencia práctica, "la seguridad de la tripulación primero" | **"Poné a prueba la atmósfera de tu hábitat contra 40 años de evidencia de fuego"** |
| 2025 · Galactic Impact | **Astro Sweepers** | Convirtieron datos de basura orbital en un **"credit score" por satélite** que puede guiar misiones, regulación e inversión | **Una métrica simple que se vuelve un instrumento de decisión.** Para nosotros: un nivel de madurez de la evidencia por ambiente (§4) |
| 2025 · Best Use of Data | **Resonant Exoplanets** (EE.UU.) | Pipeline de IA sobre datos de JWST con foco en hacer las señales pequeñas **transparentes y confiables** | **La confianza es una funcionalidad**: citas verificadas y "no hay evidencia" explícito |
| 2025 · Best Use of Technology | **SkySense** (México) | Pipeline que mezcla y limpia varias fuentes de NASA y las convierte en **probabilidades para decidir** cuándo salir. Desplegado y estable, presentado como un asistente simple | Una pregunta cotidiana como gancho, una demo que funciona y un deploy estable |
| 2024 · Best Use of Science | **SkyShield** (Canadá) | Web app que identifica **zonas de riesgo** para satélites con datos reales de NEOs | Riesgo sobre un mapa: se entiende en 5 segundos |
| 2023 · Best Use of Science | **LunarTech Ensemble** (Egipto) | Hicieron entendibles los datos sísmicos de Apollo con visualización y juego | Hacer accesibles datos viejos y dispersos de NASA (lo mismo que nos piden a nosotros) |
| 2023 · Best Use of Technology | **Spacebee** (EE.UU. y **Argentina**) | Integración de datos de Apollo en un sitio | Equipos con argentinos ya ganaron |

### Contraejemplo: el proyecto típico que no gana
Un equipo de 2025 en el mismo challenge de knowledge engine armó una biblioteca de 39 artículos con etiquetas, filtros y un chat
con Mistral 7B (no RAG). Es correcto, pero hay cientos iguales. **Eso es el piso, no el diferencial.**

### Patrones (en orden de importancia)
1. **Responder una pregunta científica o de decisión, no solo organizar información.**
2. **Una métrica o metáfora central** que se entienda sin explicación: credit score, zonas de riesgo, ¿me llueve en el desfile?
3. **Poner a prueba algo real** (un diseño o un escenario) contra datos reales.
4. **Transparencia y confianza** como valor explícito.
5. **Visualización cuidada y accesible para no expertos.** Presentation pesa igual que el resto.
6. **El tamaño del equipo no decide**: un equipo de 1 persona ganó Best Use of Science.
7. **Latinoamérica gana seguido**: Brasil (varios por año), Perú, México, Argentina.

---

## 3. Potencial del tópico: por qué es buen momento

1. **El primer fuego en la Luna está por suceder.** NASA prepara **FM2 (Flammability of Materials on the Moon)**, "el primer
   experimento de combustión en otro cuerpo planetario". Su objetivo es **vincular los ensayos de materiales en 1 g con el
   comportamiento real en gravedad reducida**. Una presentación de 2025 lo ubica a fines de 2026, en un vuelo de prueba no
   tripulado del lander de SpaceX **[verificar estado]**.
   → Gancho narrativo: *"FM2 está por prender el primer fuego en la Luna. Construimos la herramienta para poner sus resultados
   en contexto con 40 años de evidencia."*
2. **Ya hay un dato real de gravedad parcial: LUCI.** Voló en New Shepard el 4/2/2025, girando para simular gravedad lunar. En
   ese vuelo la propagación fue **más lenta** en gravedad parcial que en 1 g: PMMA 0,15 vs 0,40 cm/s en la punta de la llama.
   La extinción también fue distinta. La presentación **no** concluye que los materiales sean más inflamables en gravedad parcial,
   y advierte sobre el efecto Coriolis.
   → No contradecimos a NASA: mostramos el dato como **el único punto de gravedad parcial**, con sus caveats.
3. **NASA misma sospecha que la Luna puede ser más peligrosa.** Según la página de FM2, el modelado computacional, respaldado por
   vuelos parabólicos y la ISS, sugiere que **algunos materiales podrían arder con menos O₂ en gravedad lunar que en la Tierra**.
   Materiales "no inflamables" en la Tierra podrían serlo en un hábitat lunar.
4. **La atmósfera de exploración ya está en zona de mayor riesgo.** La atmósfera propuesta de **8,2 psia (56,5 kPa) con 34% O₂**
   supera el **31,4% O₂**, que es el límite calculado para no aumentar la tasa de quemado a esa presión. Por eso se clasifica como
   atmósfera de tasa de quemado aumentada y exige ensayar materiales y excluir algunos (Wessel et al., 2018).
5. **Hay pocos datos tabulares y muchos papers dispersos.** Eso es justo lo que el challenge pide resolver, y la IA ahí aporta de
   verdad: extraer condiciones de papers, unificar y comparar.

**Riesgos del tópico**: datos tabulares escasos (FLEX con 274 ensayos y BASS-II con 129), condiciones heterogéneas entre
investigaciones, riesgo de sobreafirmar física y de que el LLM alucine. Nuestra regla de oro y el foco en "evidencia, no
predicción" son la respuesta a los cuatro.

---

## 4. La propuesta refinada

### Pregunta central (el gancho)
> **"¿Arde en la Luna?"** — *Will it burn on the Moon?*
> Elegí dónde va a vivir la tripulación y mirá qué sabemos, qué tan seguros estamos y qué falta.

### Métrica central: **Evidence Readiness Level (ERL)**
Un análogo del TRL (Technology Readiness Level), que en NASA todos conocen, aplicado a **cuánto sabemos de cómo se comporta el
fuego** en un ambiente. Escala transparente, con la fórmula visible en la UI:

| ERL | Significado (borrador) |
|---|---|
| 1 | Sin evidencia directa; solo extrapolación |
| 2 | Solo ensayos en 1 g o modelos |
| 3 | Microgravedad o gravedad parcial en condiciones lejanas (otra presión u O₂) |
| 4 | Microgravedad en condiciones cercanas, un solo material o configuración |
| 5 | Microgravedad en condiciones cercanas, varios materiales o configuraciones, con acuerdo entre fuentes |
| 6 | Lo anterior más datos a escala grande (tipo Saffire) o en la gravedad del destino |

"Cercano" se define con umbrales explícitos de O₂ y presión, ajustables en la UI. **No es una predicción de riesgo**: mide
cuánta evidencia hay. Es el "credit score" del challenge y se puede defender ante un científico.

### Cómo cubre el pedido (y lo supera)
| Pedido | Funcionalidad | Momento de demo |
|---|---|---|
| O1 + C6 | **Selector de ambiente** con presets citados (ISS, atmósfera de exploración, base lunar, rover presurizado, traje) → investigaciones rankeadas por relevancia, con "¿por qué este orden?" | Elegir "Base lunar" y ver el ranking |
| C2 + C5 | **Fichas de investigación** con los atributos exactos de C2, agrupadas por hardware (CIR, MDCA, MSG) | Abrir la ficha de BASS-II |
| C3 | **Comparador** de 2–3 investigaciones: rangos de condiciones superpuestos, similitudes y diferencias | FLEX vs BASS-II |
| C6 | **Mapa O₂ × presión**: ensayos de microgravedad como puntos, ambientes de hábitat como zonas, ERL por celda | La base lunar cae donde hay pocos puntos |
| C7 | **Acotamiento de gravedad parcial**: evidencia en µg y en 1 g lado a lado, LUCI como único punto intermedio, rotulado "acota, no predice" | "Entre estos dos extremos está la Luna, y este es el único dato real" |
| O3 | Hallazgos organizados por **prevención / detección / supresión** (el marco de NASA), con citas verificadas | Supresión: FLEX con CO₂ y He |
| O2 | **Dataset unificado listo para modelar**: CSV/Parquet + diccionario de datos + procedencia (DOI, fila de origen), descargable | Botón "Descargar dataset" |
| Diferencial | **"¿Dónde ensayar después?"**: celdas de ambientes de hábitat con ERL bajo → condiciones sugeridas para el próximo ensayo (estilo FM2/LUCI) | "Este es el ensayo que más subiría el ERL de la base lunar" |
| O4 | 3 tarjetas de aplicaciones en la Tierra | Opcional |
| Confianza | Cada cita es clicable; preguntas trampa → "no hay evidencia" | Pregunta trampa en vivo |

### Nombre del proyecto (candidatos)
**FireBound** (juega con "acotar" y con los límites del fuego) · **Will It Burn?** · **Ember Atlas**. Se decide en equipo el 8/11.

---

## 5. Cumplir lo simple de forma impecable (lo que hace perder puntos sin que nadie lo note)

Requisitos de entrega según la guía oficial más reciente **[verificar que no cambien en 2026]**:

| Requisito | Cómo lo cumplimos |
|---|---|
| **Demo: video de ≤ 30 s con subtítulos en inglés, o ≤ 7 slides en inglés.** Si se pasa, **queda fuera del juzgamiento global** | Hacemos los dos. El video de 26–28 s es el principal; las slides incluyen nombre del equipo, integrantes y challenge |
| Todo el contenido en **inglés** | La UI se construye en inglés desde el principio. Los docs internos pueden quedar en español |
| Link al proyecto **público, sin login** | Frontend estático en Vercel o Pages; el repo público. Probar en ventana privada |
| Campo **NASA Data** con detalle | Listar PSI-69 (DOI 10.60555/mbq8-0451), PSI-25 (DOI 10.60555/4qc4-de67), los IDs de NTRS y qué hicimos con cada uno |
| Campo **Space Agency Partner & Other Data**: todo recurso, código, texto e imagen, aunque sea open source | Generarlo desde `data/sources.json` más las dependencias |
| Campo **Use of AI**: qué herramientas y cómo. Imágenes de IA con marca de agua visible. **Nada de branding de NASA** en contenido generado | `docs/AI_LOG.md` → texto del campo. Sin logos de NASA en imágenes generadas ni en el video |
| Todos los integrantes **confirmados en el evento local de Buenos Aires** | Verificar el lunes 9/11 |
| Enviar antes de las **23:59 hora local del domingo** | Nuestro objetivo es enviar a las **20:00**. Guardar borradores durante todo el día |
| Que todo el trabajo sea original | El README declara qué se preparó antes del evento |

**Errores típicos a evitar**: demo largo, links privados, campos de datos vagos ("usamos datos de NASA"), UI en español,
un deploy que depende de un backend caído, y no explicar en una oración qué hace el proyecto.

### El demo de 30 segundos (storyboard)
| Seg. | Imagen | Texto en pantalla (inglés) |
|---|---|---|
| 0–4 | Llama esférica en microgravedad (imagen de NASA con crédito, no generada) | *In space, fire doesn't rise.* |
| 4–9 | Selector → "Lunar base: 34% O₂, 8.2 psi" | *Pick where the crew will live.* |
| 9–15 | Mapa O₂ × presión; la zona lunar casi vacía | *See what 40 years of NASA experiments actually cover.* |
| 15–20 | ERL 2/6 y el acotamiento µg / 1 g, con el punto de LUCI | *Know how sure we are, and what's missing.* |
| 20–25 | Clic en una cita → fila del dataset o página del paper | *Every number traceable to NASA data.* |
| 25–30 | Logo del proyecto + "Where to test next" | *FireBound — evidence for the first fires on the Moon.* |

---

## 6. Fuentes
- Ficha del challenge (réplica del evento local): https://hackathlone.com/challenges/flame-in-freefall
- Página oficial: https://www.spaceappschallenge.org/2026/challenges/flame-in-freefall/
- Ganadores 2025: https://www.nasa.gov/learning-resources/stem-engagement-at-nasa/nasa-announces-2025-international-space-apps-challenge-global-winners/
- Meet the 2025 Global Winners: https://www.spaceappschallenge.org/2025/meet-the-2025-global-winners/
- Ganadores 2024: https://www.nasa.gov/learning-resources/stem-engagement-at-nasa/nasa-international-space-apps-challenge-announces-2024-global-winners/
- Ganadores 2023: https://science.nasa.gov/directorates/smd/2023-nasa-international-space-apps-challenge-announces-10-global-winners
- Guía de juzgamiento: https://spaceappschallenge.org/resources/judging-awards-guide
- Guía de entrega: https://www.spaceappschallenge.org/resources/project-submission-guide/
- FM2: https://www.nasa.gov/flammability-of-materials-on-the-moon-fm2/
- LUCI (Ferkul et al., ASGSR 2025): https://ntrs.nasa.gov/citations/20250010653
- Wessel et al. 2018, Aerosp Med Hum Perform 89(9):792–797: https://asma.kglmeridian.com/downloadpdf/view/journals/amhp/89/9/article-p792.pdf
- Contraejemplo (knowledge engine 2025): https://tb-space-bio-engine.vercel.app/about.html
