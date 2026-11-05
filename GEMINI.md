# Overrides para Antigravity

Antigravity lee `AGENTS.md` (v1.20.x en adelante) y este archivo tiene prioridad sobre él. Mantenelo corto:
todo lo compartido va en `AGENTS.md`.

- Carril por defecto: `frontend/`. No edites `pipeline/`, `backend/` ni `docs/DATA_CONTRACT.md`.
- El frontend consume SOLO: los JSON de `data/processed/` (vía `frontend/public/data/`, copiados por
  `make export-frontend`) y la API documentada en `docs/ARCHITECTURE.md`. Si te falta un campo, pedilo en el PR.
- Después de cada cambio visual, abrí la app en el navegador del agente, verificá en ancho de escritorio
  y de celular (390px), y adjuntá capturas al PR.
- Nunca pongas números "de ejemplo" en componentes. Si no hay datos, mostrá un estado vacío explícito.
- Accesibilidad: contraste AA, no codificar significado solo con color (las curvas de riesgo llevan etiqueta).
