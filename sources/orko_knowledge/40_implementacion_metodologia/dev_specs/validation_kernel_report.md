# validation_kernel_report (CAP-14, E1)

## §0. Contexto

- Mandato: `CAP-14` (validación kernel/expansión antes de RELEASE 1.0.0).
- Kernel: `v1.0.0-kernel` definido en `VOCABULARIO_CONTROLADO.yaml`.
- Artefactos clave:
  - `VOCABULARIO_CONTROLADO.yaml`
  - `DEPENDENCY_GRAPH.yaml`
  - `dependency_closure_script.py`
  - `KERNEL_READINESS.md`

## §1. Ejecución del closure script

- Comando ejecutado desde la raíz del repo:

  ```bash
  ./.venv/bin/python 40_implementacion_metodologia/dev_specs/dependency_closure_script.py
  ```

- Paths por defecto usados por el script:
  - `--vocab-path`: `40_implementacion_metodologia/dev_specs/VOCABULARIO_CONTROLADO.yaml`
  - `--deps-path`: `40_implementacion_metodologia/dev_specs/DEPENDENCY_GRAPH.yaml`

- Salida observada:

  ```text
  [SUMMARY] All dependency checks passed.
  ```

- Código de salida del proceso: `0`.

## §2. Alcance de los checks (según implementación actual)

Según `dependency_closure_script.py`, se validan tres familias de propiedades:

1. **Referencias (`[REF]`)**
   - Todas las fases (`fases.*.id`) definidas en `DEPENDENCY_GRAPH.yaml` deben existir en `VOCAB.layer_3.wslc_phases`.
   - Todos los playbooks en `deps.playbooks` deben existir en `VOCAB.layer_3.playbooks` y tener `id` consistente.
   - Todas las trayectorias en `deps.trayectorias` deben existir en `VOCAB.layer_3.trayectorias`.
   - Métricas usadas en:
     - `fases.*.layer_1.metricas`
     - `playbooks.*.triggered_by.metric`
     deben pertenecer a `VOCAB.layer_1.metricas`.
   - Fases referenciadas en `reads_from.phase`, `writes_to`, `coordinates_with`, `feedback_loops.phase`, `acts_on_phases`, `trayectorias.*.fases_core` y `fases_expansion` deben existir en el vocabulario de fases.

2. **Estructura DAG (`[DAG]`)**
   - Se construye un grafo dirigido de fases usando `dependencies.writes_to`.
   - Se ejecuta un DFS para detectar ciclos; cualquier ciclo se reportaría como `[DAG] cycle detected: ...`.

3. **Orphans (`[ORPHAN]`)**
   - A partir de `kernel.phases` se comprueba que cada fase kernel tenga al menos un consumidor en:
     - `fases.*.dependencies.reads_from`
     - `fases.*.dependencies.writes_to`
     - `playbooks.*.acts_on_phases`
     - `trayectorias.*.fases_core` / `fases_expansion`.
   - Si una fase kernel no tiene consumidores, se reportaría como `[ORPHAN] kernel phase 'Fx' has no consumers...`.

## §3. Resultado de la validación kernel

Dado que la ejecución anterior terminó con:

- Sin mensajes `[REF]`, `[DAG]` ni `[ORPHAN]` en stderr.
- Mensaje final `[SUMMARY] All dependency checks passed.`
- Código de salida `0`.

Concluimos para `v1.0.0-kernel` que:

1. **Consistencia de referencias**
   - Todas las fases kernel, playbooks y trayectorias referenciadas en `DEPENDENCY_GRAPH.yaml` existen en `VOCABULARIO_CONTROLADO.yaml`.
   - No se usan métricas fuera del conjunto canónico (`H_org`, `eta_org`, `ROI_Habilitacion`) en los campos validados por el script.

2. **Propiedad DAG del grafo de fases**
   - El subgrafo definido por `dependencies.writes_to` no contiene ciclos; los loops de feedback están representados explícitamente en `feedback_loops` y fuera del check DAG.

3. **Fases kernel no huérfanas**
   - Cada fase marcada como parte del kernel tiene al menos un consumidor (otra fase, un playbook o una trayectoria) según el grafo actual.

## §4. Observaciones y limitaciones

- El script **no valida contenido de archivos Markdown** ni la existencia física de todos los paths de documentación; solo razona sobre las estructuras YAML de VOCAB y DEP_GRAPH.
- Tampoco verifica semántica de negocio (por ejemplo, si un set de fases/playbooks es suficiente para cubrir todos los escenarios posibles); solo valida consistencia estructural.
- Métricas candidatas como `handoff_ratio`, `okr_alignment_score`, `capacity_gap_index`, `tf3_data_quality_score` aparecen en documentos de diseño/expansión y checklists, pero **no** como IDs canónicos en `VOCAB.layer_1.metricas` ni como `metric` en triggers del grafo; esto es consistente con el contrato kernel.

## §5. Conclusión CAP-14 (parte kernel)

Para efectos de `CAP-14`, la evidencia actual respalda que:

- El kernel semántico `v1.0.0-kernel` (VOCAB + DEP_GRAPH) es **internamente consistente** en términos de referencias, estructura DAG y ausencia de orphans en fases kernel.
- Cualquier futura modificación de `DEPENDENCY_GRAPH.yaml` deberá:
  - Mantener estas propiedades (ejecutando `dependency_closure_script.py` como check obligatorio).
  - Respetar el conjunto de métricas canónicas hasta que `VOCAB_v1.1.x` promueva nuevas métricas formales.
