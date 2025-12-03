# CHECKLIST DE VALIDACIÓN – KERNEL v1.0.0-kernel

> Uso recomendado: ejecutar esta checklist antes de aprobar cambios en dependencias (VOCAB, DEPENDENCY_GRAPH, fases F*, playbooks P0x, trayectorias) o antes de un hito del sprint.

## 1. Precondiciones

- [ ] **Entorno activado**: entorno `.venv` activo en el root del repo.
- [ ] **Dependencias instaladas**: `PyYAML` instalado en la venv.
- [ ] **Kernel congelado**: confirmar que no se modificará `v1.0.0-kernel` (solo fixes menores de typos/refs).

## 2. Revisión rápida de cambios propuestos

Para cada cambio en este sprint:

- [ ] **IDs canónicos**: todos los IDs usados en cambios (F*, P0x, trayectorias, métricas) existen en `VOCABULARIO_CONTROLADO.yaml`.
- [ ] **Métricas**: solo se usan como `metric_id` las métricas canónicas `H_org`, `eta_org`, `ROI_Habilitacion`.
- [ ] **Scope kernel**: si el cambio toca F1, F3, F7, F9 o F13, verificar que es un fix menor (no se cambian roles ni flujo principal sin decisión explícita del Capitán).

## 3. Ejecución de dependency_closure_script.py

Desde el root del repo (`orko/`), con `.venv` activado:

- [ ] Ejecutar el script de cierre de dependencias:

```bash
./40_implementacion_metodologia/dev_specs/dependency_closure_script.py
```

Resultados esperados:

- [ ] Si la salida es:
  - `[SUMMARY] All dependency checks passed.` → **OK**.
- [ ] Si aparecen errores:
  - `[REF] ...`  → revisar IDs vs `VOCABULARIO_CONTROLADO.yaml`.
  - `[DAG] ...`  → revisar ciclos en `DEPENDENCY_GRAPH.yaml` junto a E1.
  - `[ORPHAN] ...` → revisar que fases kernel tengan al menos un consumer.

No se debe aprobar un cambio en dependencias mientras haya errores abiertos del script.

## 4. Revisión de métricas, playbooks y gates

- [ ] G1–G4 siguen usando solo métricas canónicas (`H_org`, `eta_org`, `ROI_Habilitacion`).
- [ ] P01–P04 solo referencian métricas canónicas y gates G1–G2 según `playbooks_triggers_catalog.md` y `02_health_gates.md`.
- [ ] Cualquier métrica nueva (`handoff_ratio`, `okr_alignment_score`, etc.) está documentada como **candidata** y no se usa como `metric_id`.

## 5. Registro en board_coordinación

Después de correr esta checklist:

- [ ] Registrar un evento en `board_coordinación.md`:
  - Tipo: `[OUTCOME]` (y `[UNBLOCK]` si resolvió un riesgo).
  - Referencia a `CAP-09` y a los artefactos verificados.
  - Incluir si el script pasó OK o qué errores se encontraron y cómo se resolverán.

Solo después de completar esta checklist y registrar el OUTCOME se considera que el kernel + expansiones están **validados** para el hito correspondiente.

