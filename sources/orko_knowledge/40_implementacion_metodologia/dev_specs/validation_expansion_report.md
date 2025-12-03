# validation_expansion_report (CAP-14, E1)

## §0. Propósito

- Mandato asociado: `CAP-14` (validación de expansión frente a kernel).
- Objetivo: documentar un chequeo v0.1 de **consistencia semántica** entre:
  - Kernel (`VOCABULARIO_CONTROLADO.yaml`, `DEPENDENCY_GRAPH.yaml`).
  - Documentación de metodología (`30_metodologia_orko/`), governance y ejemplos (`40_implementacion_metodologia/`).
  - Métricas y términos que aparecen en expansión pero aún no son canónicos.

## §1. Metodología de revisión

1. **Greps de términos prohibidos (vocab.terminos_prohibidos)**
   - Patrón buscado (simplificado): `"recurso|gente|equipo IT|iniciativa suelta|AI genérica|proyecto transformación"`.
   - Ámbitos:
     - `30_metodologia_orko/**/*.md`
     - `40_implementacion_metodologia/**/*.md`

2. **Greps de métricas candidatas conocidas**
   - `handoff_ratio`
   - `okr_alignment_score`
   - `capacity_gap_index`
   - `tf3_data_quality_score`
   - Ámbito: `**/*.md`, `**/*.yaml` en el repo.

3. **Revisión puntual de artefactos núcleo de expansión**
   - `playbooks_triggers_catalog.md`
   - `13_metricas_validacion/02_health_gates.md`
   - Fases WSLC clave (F4–F6, F10–F13) y playbooks P01–P08.

## §2. Hallazgos sobre términos prohibidos

### 2.1. Uso en guías/meta-documentos

- Matches principales aparecen en documentación de **guía de autor** y **planes internos**, por ejemplo:
  - `00_wip_desarrollo_metodologia/GUIA_AUTOR_CONTENIDO.md` (antipatrones, ejemplos de “no usar”).
  - `00_wip_desarrollo_metodologia/PLAN_ETAPA_1_KERNEL.md` (tabla de términos prohibidos y comandos `grep` sugeridos).
  - `40_implementacion_metodologia/dev_specs/HOWTO_VOCABULARIO.md` (reglas sobre “recurso”, “gente”, etc.).

- En estos casos, los términos aparecen **como ejemplos de qué NO hacer**, no como parte de contratos metodológicos. Esto es compatible con el diseño del VOCAB.

### 2.2. Uso en documentos de metodología / ejemplos

- En el barrido actual no se detectaron usos evidentes de:
  - `equipo IT`, `iniciativa suelta`, `AI genérica`, `proyecto transformación`
  como parte de contratos de fases, playbooks, trayectorias o health gates.

- Términos como `recursos`/`resources` aparecen en algunos documentos de especificaciones (`dev/especificaciones.md`, `dev/meta.md`), pero en contexto descriptivo y **fuera** del núcleo de metodología publicado (`30_metodologia_orko/`).

**Evaluación v0.1:**

- No se encontraron violaciones claras al conjunto `terminos_prohibidos` en contratos principales de metodología (fases WSLC, playbooks, health gates, trayectorias).
- Las menciones encontradas se limitan a guías de estilo o documentación de análisis, donde el uso es aceptable como ejemplo/antipatrón.

## §3. Métricas candidatas vs métricas canónicas

### 3.1. Métricas canónicas (kernel)

Según `VOCAB.layer_1.metricas`:

- `H_org`
- `eta_org`
- `ROI_Habilitacion`

Estas son las **únicas métricas canónicas** en kernel `v1.0.0-kernel`.

### 3.2. Métricas candidatas observadas

Durante la revisión aparecen recurrentemente, en diseño/expansión:

- `handoff_ratio`
- `cycle_time`, `cycle_time_baseline`
- `flow_efficiency` / `efficiency`
- `okr_alignment_score` / `alignment_score`
- `capacity_gap_index`
- `tf3_data_quality_score`

Contextos típicos:

- Arquitectura y diseño de flujos (`10_arquitectura_orko/0x_*.md`, F5, quick wins, patrones de flujo).
- Planes de etapa (`PLAN_ETAPA_2_EXPANSION.md`, `PLAN_ETAPA_3_PLAYBOOKS.md`).
- Checklists y documentos de readiness (`CHECKLIST_VALIDACION.md`, `KERNEL_READINESS.md`).
- Instrucciones a equipos en `board_coordinación.md` (como métricas **candidatas** para futuras versiones del VOCAB).

### 3.3. Validación de uso frente a kernel

- `dependency_closure_script.py` construye el conjunto de métricas válidas a partir de `VOCAB.layer_1.metricas` y verifica que:
  - Métricas usadas en `fases.*.layer_1.metricas` y `playbooks.*.triggered_by.metric` pertenezcan a ese conjunto.

- Dado que el script terminó con:

  ```text
  [SUMMARY] All dependency checks passed.
  ```

  concluimos que **ninguna** de las métricas candidatas anteriores está siendo usada como `metric_id` en las estructuras validadas (fases WSLC y triggers de playbooks dentro del grafo).

- En los documentos revisados, estas métricas aparecen como:
  - Campos de salida de fases (ej. `F5_flow_design` → `handoff_ratio` como output).
  - Métricas derivadas en ejemplos y patrones (diagnóstico, vistas, queries).
  - “Signal text” en checklists y guías, coherente con la nota de `KERNEL_READINESS.md` de que son candidatas para `VOCAB v1.1.x`.

**Evaluación v0.1:**

- El uso actual de métricas candidatas **no rompe** el contrato kernel:
  - No están registradas como métricas canónicas en `VOCAB.layer_1.metricas`.
  - No se usan como IDs de métrica en triggers del grafo.
- Se consideran aptas para aparecer en un archivo de notas (`VOCAB_v1.1.x_NOTAS.md`) como insumo para la próxima versión del VOCAB.

## §4. Expansión en playbooks, health gates y casos

### 4.1. Playbooks y health gates

- `playbooks_triggers_catalog.md`:
  - Confirma que cada playbook P01–P15 se engancha **solo** a métricas canónicas (`H_org`, `eta_org`, `ROI_Habilitacion`).
  - Otras señales (ej. drifts, handoffs, conflictos) se modelan como incidentes ligados a fases/entidades (`F*`, `E6`, `E7`), no como métricas nuevas.

- `13_metricas_validacion/02_health_gates.md` (G1–G4):
  - Usa exclusivamente `H_org`, `eta_org`, `ROI_Habilitacion` como métricas numéricas.
  - Puede mencionar `handoff_ratio` y otros conceptos como contexto descriptivo, pero no los trata como métricas canónicas.

### 4.2. Casos de ejemplo (`40_implementacion_metodologia/ejemplos`)

- Tras el trabajo de E2 bajo `CAP-15`, los 6 casos (`*_completo`) tienen `context.yaml` instancias de `context_pattern_schema` sin introducir métricas nuevas.
- Cualquier métrica no canónica aparece, en todo caso, como parte de narrativa o notas, no como campo formal del schema.

## §5. Conclusión CAP-14 (parte expansión)

- **Términos prohibidos:**
  - No se detectan usos problemáticos en contratos núcleo de metodología.
  - Las apariciones en guías/planes se consideran aceptables como ejemplos/antipatrones.

- **Métricas candidatas:**
  - Varias métricas adicionales (`handoff_ratio`, `cycle_time`, `capacity_gap_index`, etc.) aparecen de forma consistente en diseño y ejemplos.
  - Ninguna está promovida aún a métrica canónica ni se usa como `metric_id` en el grafo; su uso actual es compatible con el kernel.

- **Recomendación:**
  - Mantener el kernel cerrado en `H_org`, `eta_org`, `ROI_Habilitacion` para RELEASE 1.0.0.
  - Utilizar `VOCAB_v1.1.x_NOTAS.md` como backlog de trabajo para formalizar, en futuras versiones, las métricas candidatas que resulten más críticas en operación/governance.
