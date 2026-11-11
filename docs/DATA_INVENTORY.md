# DATA INVENTORY (reconocimiento al 4/11/2026)

> Investigación previa al evento. Todo lo marcado **[verificar]** hay que confirmarlo con el archivo real.
> NASA publica la lista oficial de recursos del challenge el 13/11: actualizar este documento ese día.

## 1. NASA Physical Sciences Informatics (PSI)

**Acceso**
- Sitio: https://psi.nasa.gov/physci/repo/ (app JavaScript: WebFetch/curl de la página no muestra contenido).
- **API de metadatos (JSON, sin login)**: `https://psi.nasa.gov/geode-py/ws/repo/investigations/<PSI-ID>`
  - Campo `added[]`: un objeto por archivo con `file_name`, `file_size` (bytes), `remote_url`, `s3_version_id`,
    `subcategory`, `date_created`.
  - Descarga de archivos legacy: `https://psi.ndc.nasa.gov/mpglobal/api/athena/file/{id}/?inline=1&log=1`.
  - Algunos registros usan una ruta relativa `/datamanager/file/{remote_path}` **[verificar base URL]**.
- `prep/recon_psi.py` recorre esta API y arma un inventario CSV.
- Licencia: los metadatos de PSI-25 y PSI-69 declaran CC0-1.0 (según un equipo que los descargó el 24/10/2026) **[verificar]**.

**Investigaciones de Combustion Science en PSI** (19, todas "Complete"; IDs PSI a completar con `recon_psi.py`):

| Acrónimo | Nombre | PSI-ID | Tipo | Prioridad |
|---|---|---|---|---|
| FLEX | Flame Extinguishment Experiment | PSI-69 | gotas | **Alta** — tabla de 274 ensayos |
| BASS-II | Burning and Suppression of Solids II | PSI-25 | sólidos | **Alta** — tabla de 129 ensayos |
| BASS | Burning and Suppression of Solids | ? | sólidos | Media |
| FLEX-2 | Flame Extinguishment Experiment 2 | ? | gotas | Media |
| SAFFIRE-I/II/III | Spacecraft Fire Experiment | ? | sólidos a gran escala | **Alta** (más cercano a un incendio real de cabina) |
| ACME (BRE, E-FIELD, S-Flames) | Advanced Combustion via Microgravity Experiments | ? | gas | Media |
| CFI | Cool Flames Investigation | ? | gotas/gas | Media (storytelling) |
| SAME / SAME-R | Smoke Aerosol Measurement Experiment | ? | humo | Media (toxicidad/detección) |
| DAFT / DAFT-2 | Dust and Aerosol Measurement Feasibility Test | ? | aerosoles | Baja |
| SLICE | Structure and Liftoff in Combustion Experiment | ? | gas | Baja |
| SPICE | Smoke Point in Coflow Experiment | ? | gas | Baja |
| (sin acrónimo) | Cool flame transitions, counterflow (ground) | ? | tierra | Baja |
| (sin acrónimo) | SAME data for smoke modeling (ground) | ? | modelado | Baja |

### FLEX — PSI-69 (DOI 10.60555/mbq8-0451)
- Archivo: `PSI-69_Experimental table_FLEX.csv`, 24.776 bytes,
  SHA-256 `37c88ce8ae9391b7544ff630a45ce87543d04d317cdbfbed104fe7d5c27e1b96` **[verificar al descargar]**.
- **Encoding Windows-1252** (no UTF-8).
- 274 ensayos de combustión de gotas en la ISS: combustible, presión, atmósfera, diámetros de gota,
  constante de tasa de quemado (mm²/s), resultado.
- Rarezas conocidas:
  - El encabezado "Burning rate; mm" es mm²/s truncado.
  - La columna "CO" es en realidad CO₂.
  - El significado de columnas está en **NASA/TP-2015-216046**, Apéndice A.1 y Tabla IX.
  - Ensayos con resultado "Disruption" no sirven para análisis de extinción.

### BASS-II — PSI-25 (DOI 10.60555/4qc4-de67)
- Archivo: `PSI-25_Experimental table_BASS-II.csv`, 16.590 bytes,
  SHA-256 `71e792bf6b5fb5ea620c5dd70fbbac05515992e12aefcf5dff47312caa48c042` **[verificar]**.
- 129 ensayos de llama sobre sólidos en la ISS: materiales, configuración de flujo, lecturas de O₂, CO₂ y CO.
- Rarezas: **no tiene columna de velocidad de propagación** ni registro explícito de extinción
  → esos campos van `null`, no se infieren.
- El resto de PSI-25 son videos `.mp4` (5–150 MB c/u) y zips de imágenes de varios GB: **no descargar**.

## 2. NASA Technical Reports Server (NTRS)
- API sin login: `https://ntrs.nasa.gov/api/citations/search?q=<texto>&page.size=<n>`
  y `https://ntrs.nasa.gov/api/citations/<id>`.
- Desde el sandbox de Claude la API no es accesible por shell; desde tu máquina sí. Usar `prep/recon_ntrs.py`.
- Búsqueda "microgravity flame spread spacecraft fire safety": 59 resultados. Papers clave detectados (con PDF):

| NTRS ID | Título | Año | Tipo | Por qué importa |
|---|---|---|---|---|
| 20210017780 | Fire Safety Implications of Preliminary Results from Saffire IV and V Experiments on Large Scale Spacecraft Fires | 2021 | Presentación | Implicaciones directas de seguridad |
| 20130001713 | Large Scale Experiments on Spacecraft Fire Safety | 2012 | Paper | Motivación de Saffire |
| 20180005168 | Saffire: A Novel Approach to Study of Spacecraft Fire Safety Using Un-Manned Spacecraft | 2017 | Presentación | Diseño de Saffire |
| 19930015566 | Contributions of Microgravity Test Results to the Design of Spacecraft Fire Safety Systems | 1993 | Paper | Puente ciencia → diseño |
| 20200000557 | Buoyancy Effects on Concurrent Flame Spread Over Thick PMMA | 2018 | Manuscrito | PMMA, flujo concurrente |
| 20210017787 | Determining the Cause of Reduced Concurrent Flame Spread over Thin Solid Fuels in Low Pressure and Low Gravity | 2021 | Paper | Baja presión (hábitats) |
| 20220012861 | Determining Flame Temperature by Broadband Two Color Pyrometry in a Flame Spreading over a Thin Solid in Microgravity | 2022 | Manuscrito | Mediciones |
| 19970020613 | Ignition, Transition, Flame Spread in Multidimensional Configurations in Microgravity | 1997 | Paper | Ignición |
| 19960008418 | Ignition and subsequent transition to flame spread in a microgravity environment | 1995 | Paper | Ignición |
| 20140004929 | Effect of Longitudinal Oscillations on Downward Flame Spread over Thin Solid Fuels | 2013 | Paper | Vibraciones |
| 19900004364 | Flame Spread over Shallow Liquid Pools in Microgravity and Nonair Environments | 1989 | Paper | Líquidos |
| 20160000593 | Combustion of Solids in Microgravity: Results from the BASS-II Experiment | — | Paper | Documenta PSI-25 |
| (buscar) | NASA/TP-2015-216046 (FLEX) | 2015 | TP | Diccionario de columnas de PSI-69 |

Queries sugeridas para `recon_ntrs.py`: "Saffire", "BASS-II", "FLEX droplet extinction", "cool flames ISS",
"SoFIE", "spacecraft fire safety oxygen pressure", "exploration atmosphere flammability", "smoke detection ISS SAME".

## 3. Gravedad parcial y atmósferas de exploración (encontrado el 5/11)
- **PSI no tiene datos de combustión en gravedad parcial** (lo dice el texto del challenge).
- **LUCI — Lunar-g Combustion Investigation** (NTRS 20250010653, presentación ASGSR 2025, Ferkul et al.):
  - Voló en New Shepard el 4/2/2025, girando a 11 RPM con radio efectivo de 1,22 m para simular gravedad lunar.
  - Muestras de PMMA y SIBAL en aire a ≈1 atm.
  - La propagación fue más lenta en gravedad parcial que en 1 g. Hay valores por material en la presentación: citar la página.
  - Caveat: el efecto Coriolis desvía la llama. **No** concluye que los materiales sean más inflamables en gravedad parcial.
- **FM2 — Flammability of Materials on the Moon** (página de NASA): sería el primer experimento de combustión en otro cuerpo
  planetario, con 4 muestras en atmósferas de hábitat lunar. Mide propagación, temperaturas, O₂ y CO₂. Una presentación de 2025
  lo ubica a fines de 2026 **[verificar]**.
- **ACME E-FIELD Flames**: imita gravedad parcial con un campo eléctrico (está en PSI).
- **CFI-G** (ACME): tiene los ensayos de mayor O₂ en microgravedad, hasta 85% (según el texto del challenge).
- **Atmósferas de exploración**: Wessel et al. 2018 (ver `data/environments.yaml`). 8,2 psia con 34% O₂ supera el 31,4%,
  que es el límite para no aumentar la tasa de quemado a esa presión.
- **Grupos de hardware** (texto del challenge): ACME → CIR · FLEX, FLEX-2 y CFI → MDCA dentro del CIR ·
  BASS, BASS-II, SPICE y SLICE → MSG con ducto de flujo.

- **Asignación oficial prevención / detección / supresión** (texto del challenge del 11/11):
  prevención → BASS, BASS-II, Saffire-I/II/III · detección → SAME, SAME-R · supresión → FLEX (CO₂ y He).
  DAFT y DAFT-2 usaron uno de los instrumentos de SAME para detectar polvo.
  ACME BRE estudió inflamabilidad de materiales en atmósfera quieta, en función de las propiedades del material (con combustibles gaseosos).

## 4. Otras fuentes a evaluar
- NASA BPS: "NASA Studies Fire in Microgravity" (2026) — imágenes CIR/SoFIE para storytelling (crédito NASA).
- SoFIE (Solid Fuel Ignition and Extinction) — **no** aparece en la lista de PSI de combustión: buscar papers en NTRS.
- MaCFP matl-db (GitHub) — datos de tierra (cono calorimétrico de PMMA). Solo como referencia 1 g, rotulado.

## 5. Qué hicieron otros equipos (para diferenciarnos)
Repos públicos de 2026 con este challenge: chat sobre papers, dashboards Streamlit con FLEX/BASS-II, simuladores
físicos 2D, rankings BM25. Casi ninguno tiene: verificación automática de citas, asesor por escenario con
explicación del ranking, ni mapa de huecos. Eso es nuestro espacio.
