#!/usr/bin/env bash
# Recrea el enlace .claude/skills -> .agents/skills (o copia en sistemas sin symlinks).
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf .claude/skills
if ln -s ../.agents/skills .claude/skills 2>/dev/null; then
  echo "symlink creado"
else
  cp -r .agents/skills .claude/skills && echo "copiado (sin symlink): recordá re-copiar si cambian las skills"
fi
