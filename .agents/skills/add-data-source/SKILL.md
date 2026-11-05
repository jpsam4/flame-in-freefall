---
name: add-data-source
description: Incorporar un dataset de NASA PSI o un paper de NTRS al repo con procedencia completa (sources.json, hash, licencia). Usar antes de leer cualquier archivo nuevo en pipeline/.
---

# Agregar una fuente de datos

## Pasos
1. **Descargá sin modificar** el archivo a `data/raw/<origen>/` (ej. `data/raw/psi/PSI-69/`).
   - PSI: el listado de archivos de una investigación está en
     `https://psi.nasa.gov/geode-py/ws/repo/investigations/<PSI-ID>` (campo `added[]`, con `file_name`,
     `file_size`, `remote_url`). `prep/recon_psi.py` lo hace por vos.
   - NTRS: `https://ntrs.nasa.gov/api/citations/<id>` para metadatos; el PDF está en `downloads[]`.
2. **Calculá SHA-256 y tamaño**: `uv run python -m pipeline.provenance hash <ruta>`
   (si todavía no existe ese módulo, usá `sha256sum`).
3. **Registrá en `data/sources.json`** un objeto `Source` según `docs/DATA_CONTRACT.md`:
   `source_id`, `kind`, `title`, `url`, `doi`, `license`, `file_path`, `sha256`, `size_bytes`,
   `retrieved_at`, `encoding`, `notes`.
4. **Leé la documentación del dataset** antes de mapear columnas (el paper o TP asociado). Anotá en `notes`
   cualquier rareza de encabezados. Ejemplos conocidos en `docs/DATA_INVENTORY.md`
   (FLEX: "Burning rate; mm" es mm²/s truncado; la columna "CO" es CO₂; encoding Windows-1252).
5. **Escribí el mapeo** columna → campo del contrato en `pipeline/mappings/<source_id>.yaml`, con unidad de origen
   y conversión. Nada de mapeos implícitos dentro del código.
6. **Test**: agregá un test que cargue 3 filas reales y verifique los valores convertidos contra el archivo.

## No hacer
- No edites archivos en `data/raw/`.
- No subas al repo archivos de más de 50 MB (videos, zips de imágenes): registralos en `sources.json` con
  `file_path: null` y la `url`.
- No asumas la licencia: copiala de los metadatos de PSI/NTRS.
