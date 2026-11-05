---
name: extract-findings
description: Extraer hallazgos (Finding) de papers de NTRS con un LLM, con cita obligatoria y validación por esquema. Usar al construir o modificar pipeline/extract_findings.py o al procesar papers nuevos.
---

# Extraer hallazgos de papers

## Principio
El LLM **propone**, el esquema **valida**, un humano **muestrea**. Un hallazgo sin página y fragmento citado se descarta.

## Pasos
1. Partí el PDF en chunks por página (conservá el número de página real del PDF).
2. Prompt de extracción (guardado en `pipeline/prompts/extract_findings.md`, versionado):
   - Pedí salida JSON que cumpla `Finding` de `docs/DATA_CONTRACT.md`.
   - Exigí `evidence_snippet` (≤ 25 palabras, textual del paper) y `page`.
   - Pedí condiciones (O₂, presión, flujo, material, gravedad) solo si están en el texto; si no, `null`.
   - Instrucción explícita: "Si el texto no lo dice, no lo infieras".
3. Validá con Pydantic. Rechazá y logueá en `data/processed/rejected_findings.jsonl` lo que no valide.
4. **Verificación automática del fragmento**: el `evidence_snippet` normalizado tiene que aparecer en el texto de esa
   página. Si no aparece → `status: "unverified"` y no se muestra en el dashboard.
5. Guardá `extracted_by` (modelo + versión del prompt) y `extracted_at`.
6. Muestreo humano: marcá 10% al azar con `needs_human_review: true`; el dashboard muestra cuántos fueron revisados.

## No hacer
- No resumir papers enteros en un solo llamado: extraé por chunk y consolidá después.
- No mezclar resultados de tierra (1 g) y microgravedad sin el campo `gravity_regime`.
- No pedirle al LLM números que después se grafican sin verificar el fragmento.
