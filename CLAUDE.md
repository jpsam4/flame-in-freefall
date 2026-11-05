@AGENTS.md

# Overrides para Claude Code

- Carril por defecto: `pipeline/`, `data/` y `backend/`. Para tocar `frontend/` la tarea lo tiene que pedir.
- Para tareas de más de un paso, usá plan mode primero y mostrá el plan antes de editar.
- Usá un worktree por tarea (`claude --worktree` o `git worktree add ../fif-<id> <rama>`), así no chocás
  con Codex ni Antigravity trabajando en paralelo.
- Al terminar una tarea: `make check`, actualizá el estado en `docs/TASKS.md` y agregá una línea a `docs/AI_LOG.md`.
- Las skills compartidas están en `.claude/skills` (symlink a `.agents/skills`). Si el symlink no funciona
  en tu sistema (Windows), corré `scripts/link_skills.sh` o copiá la carpeta.
