---
name: review-pr
description: Checklist de revisión cruzada de PRs entre agentes (un agente revisa lo que hizo otro). Usar cuando te piden revisar un PR o un diff de este repo.
---

# Revisión cruzada de PR

Revisá como si el autor fuera otro equipo. Respondé con: **Bloqueante**, **Sugerencia**, **OK**.

## Bloqueantes (cualquiera de estos frena el merge)
- [ ] Aparece un número, DOI, ID o nombre de experimento que no sale de `data/` + `data/sources.json`.
- [ ] Cambia `docs/DATA_CONTRACT.md` o un modelo de esquema sin ADR en `docs/DECISIONS.md`.
- [ ] Toca archivos fuera del carril de la tarea sin justificarlo en el PR.
- [ ] `make check` falla o se borraron/debilitaron tests para que pase.
- [ ] Datos sintéticos fuera de `tests/fixtures/` o sin `synthetic: true`.
- [ ] Unidades ambiguas (campo numérico sin unidad en el nombre o en el esquema).
- [ ] Secretos, claves o rutas personales en el código.

## A revisar
- ¿Los tests prueban comportamiento con datos reales (3 filas del archivo) además de casos borde?
- ¿El código respeta la frontera de módulos de `docs/ARCHITECTURE.md`?
- ¿Errores claros cuando falta un dato, en vez de defaults silenciosos?
- Frontend: ¿estados vacíos, carga y error? ¿Capturas en desktop y 390px? ¿Cada insight muestra su fuente?
- ¿Se actualizó `docs/TASKS.md` y `docs/AI_LOG.md`?

## Formato de respuesta
```
Veredicto: APROBAR | CAMBIOS | BLOQUEAR
Bloqueantes: ...
Sugerencias: ...
Probé: <comandos que corriste>
```
