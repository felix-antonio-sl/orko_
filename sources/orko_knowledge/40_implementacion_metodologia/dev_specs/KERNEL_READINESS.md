# KERNEL_READINESS – v1.0.0-kernel

## 1. Propósito

Este one‑pager explica **qué está congelado en el kernel v1.0.0-kernel** y **cómo leer el grafo de dependencias** para que E2–E4 puedan trabajar sin ambigüedad.

Artefactos núcleo:

- `VOCABULARIO_CONTROLADO.yaml` (v1.0.0 + `kernel_contract.release_tag = v1.0.0-kernel`).
- `DEPENDENCY_GRAPH.yaml` (v1.0.0-kernel, scope F1,F3,F7,F9,F13).
- `dependency_closure_script.py` (valida consistencia entre ambos).

## 2. Qué está congelado en v1.0.0-kernel

### 2.1. IDs estables (kernel_contract)

Según `VOCABULARIO_CONTROLADO.metadata.kernel_contract`:

- **Familias de IDs estables:**
  - `A*` (axiomas A1–A5).
  - `P*` (primitivos P1–P5).
  - `I*` (invariantes I1–I8).
  - `D*` (dominios D1–D4).
  - `F*` (fases WSLC F1–F18).
  - `P0x` (playbooks P01–P15).
  - `trayectorias` (`Minimal`, `Avanzada`, `Survival`).
- **Métricas canónicas estables:**
  - `H_org`, `eta_org`, `ROI_Habilitacion`.
- **Política de cambio:**
  - Cualquier cambio será **backward‑compatible** o documentado como **breaking change** en el `changelog`.

### 2.2. Kernel de fases

El kernel de metodología WSLC está definido en `DEPENDENCY_GRAPH.yaml.kernel`:

- Fases kernel: `F1`, `F3`, `F7`, `F9`, `F13`.
- Flujo principal:
  - `F1 → F3 → F7,F9 → F13`.
- Interpretación:
  - **F1**: contexto + baseline `H_org`.
  - **F3**: selección de trayectoria (`Survival`, `Minimal`, `Avanzada`).
  - **F7**: cascada de propósito / OKR.
  - **F9**: diseño de estado objetivo `E6`.
  - **F13**: monitoreo de salud y loops de aprendizaje.

### 2.3. Kernel de métricas

En SPRINT 1 solo se usan como `metric_id`:

- `H_org` (health organizacional).
- `eta_org` (eficiencia global).
- `ROI_Habilitacion` (retorno de habilitación).

Otras señales (`handoff_ratio`, `okr_alignment_score`, etc.) están **aprobadas conceptualmente** para versiones futuras, pero hoy son solo **texto explicativo**, no IDs canónicos.

## 3. Cómo leer `DEPENDENCY_GRAPH.yaml`

`DEPENDENCY_GRAPH.yaml` tiene cinco bloques principales:

1. **`metadata`**
   - `version: 1.0.0-kernel`, `status: kernel_only`.
   - `scope`: `F1,F3,F7,F9,F13`.
   - `expansion_plan`: lista de fases de expansión, playbooks y trayectorias futuras.

2. **`kernel`**
   - Lista de fases kernel (`phases`).
   - `dependency_flow`: cadena principal F1→F3→F7,F9→F13.
   - `completeness`: qué se puede hacer solo con kernel y qué queda postergado.

3. **`fases`**
   - Nodo por cada fase kernel (`F1`, `F3`, `F7`, `F9`, `F13`).
   - Cada nodo incluye:
     - `layer_0`: A/P/I usados en esa fase (IDs de VOCAB).
     - `layer_1`: dominios `D*`, entidades (`E6` cuando aplica), métricas canónicas.
     - `layer_2`: relación con tejidos `TF1–TF3` (si aplica).
     - `dependencies`:
       - `reads_from`: qué fases alimentan a esta fase.
       - `writes_to`: a qué fases empuja esta fase.
       - `coordinates_with`: coherencia entre decisiones.
       - `feedback_loops`: ciclos explícitos (ej. `F13→F1`).

4. **`playbooks`**
   - Vista resumida P01–P15 desde el kernel.
   - Para cada playbook:
     - `triggered_by`: métricas canónicas (`H_org`, `eta_org`, `ROI_Habilitacion`) + fase fuente.
     - `acts_on_phases`: fases WSLC donde opera.

5. **`trayectorias`**
   - `Survival`, `Minimal`, `Avanzada` con:
     - `fases_core`: subconjunto de fases imprescindibles.
     - `fases_expansion`: fases adicionales para esa trayectoria.
     - `playbooks_clave`: P0x clave por trayectoria.

6. **`validation_rules`**
   - Reglas que `dependency_closure_script.py` debe respetar:
     - `no_orphan_outputs`: salidas de F1,F3,F7,F9,F13 con al menos un consumer.
     - `no_invalid_references`: todos los IDs usados existen en VOCAB.
     - `dag_structure`: grafo sin ciclos salvo `feedback_loops` explícitos.

## 4. `dependency_closure_script.py` – cómo usarlo

Ubicación: `40_implementacion_metodologia/dev_specs/dependency_closure_script.py`.

Ejemplo de uso (desde root del repo, con `.venv` activado):

```bash
./40_implementacion_metodologia/dev_specs/dependency_closure_script.py
```

Comportamiento:

- Si todo está bien:
  - Imprime: `[SUMMARY] All dependency checks passed.`
- Si hay problemas, imprime líneas tipo:
  - `[REF] ...`  (referencias a fases/playbooks/trayectorias/métricas que no existen en VOCAB).
  - `[DAG] ...`  (ciclos detectados en el grafo de fases).
  - `[ORPHAN] ...` (fases kernel sin consumers).

Flags opcionales:

```bash
python3 40_implementacion_metodologia/dev_specs/dependency_closure_script.py \
  --check-refs --check-dag --check-orphans
```

## 5. Instrucciones para equipos 2–3–4

### 5.1. Antes de tocar el grafo o el VOCAB

- No modificar:
  - Familias de IDs marcadas como estables.
  - Métricas canónicas (`H_org`, `eta_org`, `ROI_Habilitacion`).
- Extensiones permitidas en SPRINT 1:
  - Añadir detalle en docs de fases F4–F12, playbooks, health gates.
  - Crear schemas (compliance, contexto) usando IDs canónicos.

### 5.2. Al proponer cambios de dependencias

- Si agregas/modificas:
  - `reads_from` / `writes_to` / `acts_on_phases` / `fases_*` / `playbooks_clave`:
    1. Asegúrate de usar solo IDs de VOCAB (`F*`, `P0x`, trayectorias).
    2. Ejecuta `dependency_closure_script.py`.
    3. Si hay errores `[REF]`, corrige los IDs; si hay `[DAG]`, revisa el diseño con E1.

### 5.3. Propuesta de nuevas métricas

- Si necesitas una métrica nueva (ej. formalizar `handoff_ratio`):
  - Documentarla como **métrica candidata** (sin usarla como `metric_id`).
  - Notificar a E1 según el proceso de `HOWTO_VOCABULARIO.md` (§5).
  - Esperar a que aparezca en `VOCABULARIO_CONTROLADO.layer_1.metricas` antes de usarla como ID.

## 6. Resumen de readiness

- `VOCABULARIO_CONTROLADO.yaml v1.0.0-kernel` + `DEPENDENCY_GRAPH.yaml v1.0.0-kernel` + `dependency_closure_script.py` forman el **kernel sólido** sobre el que se apoya SPRINT 1.
- Último run del script sobre el kernel actual: **`[SUMMARY] All dependency checks passed.`**
- E2–E4 pueden construir sobre este kernel sin esperar cambios estructurales; cualquier cambio mayor se coordinará vía `board_coordinación.md` y nuevas versiones de VOCAB/DEP_GRAPH.
