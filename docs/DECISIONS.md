# DECISIONS (ADRs cortos)

Formato: contexto → decisión → consecuencias. Una decisión nueva = una entrada nueva, no se edita la vieja.

## ADR-001 — Frontend: Next.js + JSON precomputado (Streamlit como plan B)
- **Contexto**: 48 h, el jurado valora una demo pulida; queremos usar Antigravity en el carril de UI y que F1/F3/F4
  funcionen aunque el backend se caiga.
- **Decisión**: Next.js (App Router, TypeScript, Tailwind) con export estático leyendo `frontend/public/data/*.json`;
  F2 y F5 llaman al backend.
- **Plan B**: si el sábado a las 20:00 el frontend no muestra F1 con datos reales, pasamos a Streamlit en `app_streamlit/`
  reutilizando `pipeline/` y `backend/ranking.py`.
- **Consecuencias**: dos lenguajes; el contrato JSON (`DATA_CONTRACT.md`) es la frontera.

## ADR-002 — Precomputar offline, solo /rank y /ask en vivo
- **Decisión**: ver `ARCHITECTURE.md`. Los artefactos de `data/processed/` se versionan en git.
- **Consecuencias**: la demo es reproducible; hay que correr `make pipeline` antes de cada deploy.

## ADR-003 — Proveedor de LLM detrás de `LLMClient`
- **Estado**: PENDIENTE (decidir el 14/11 a la mañana según créditos/cuotas del equipo).
- **Decisión provisoria**: interfaz única `LLMClient.complete(messages, json_schema=None) -> str` con adaptadores;
  el proveedor se elige con `LLM_PROVIDER` en `.env`. Extracción offline y `/ask` pueden usar modelos distintos.

## ADR-004 — Sin ML predictivo en el MVP
- **Contexto**: ~400 filas tabulares heterogéneas; un modelo predictivo invita a afirmar cosas no respaldadas.
- **Decisión**: el "SI" del producto es extracción + ranking explicable + síntesis con citas verificadas.
- **Consecuencias**: lo explicamos en el pitch como decisión de seguridad, no como limitación.

## ADR-005 — ERL como métrica central y dataset descargable para O2
- **Contexto**: el objetivo O2 del challenge pide "extraer datos que sirvan para modelado predictivo". Los ganadores previos
  usan una métrica simple como instrumento de decisión (ver `STRATEGY.md` §2).
- **Decisión**: (1) cumplimos O2 entregando un dataset unificado con procedencia y diccionario de datos (F6), para que otros
  modelen; (2) la métrica central es el Evidence Readiness Level (ERL), que mide cobertura de evidencia y no predice riesgo.
- **Consecuencias**: complementa ADR-004 sin contradecirlo. La fórmula del ERL tiene que estar visible en la UI y testeada.

## ADR-006 — UI y entrega en inglés, docs internos en español
- **Contexto**: la guía de entrega exige que todo el contenido esté en inglés.
- **Decisión**: textos de la UI, README de entrega y `data/environments.yaml` en inglés desde el primer commit del evento.
  `docs/` puede seguir en español.
