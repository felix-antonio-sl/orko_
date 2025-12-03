# 01_validacion_trazabilidad_i1_i8 (draft)

## §0. Fundamento

- Invariantes: `I1`–`I8` (ver `VOCABULARIO_CONTROLADO.layer_0.invariantes` y `00_fundamentos_teoricos`).
- Mapa de evidencias VG4: `13_metricas_validacion/03_vg4_validation_map.md`.
- Artefactos clave: `VOCABULARIO_CONTROLADO.yaml`, `DEPENDENCY_GRAPH.yaml`, `02_health_gates.md`, `01_team_structure_raci.md`, trayectorias (`Survival`, `Minimal`, `Avanzada`), `03_decision_matrix.md`, `board_coordinación.md`.
 - Casos de ejemplo: 6 contextos completos en `40_implementacion_metodologia/ejemplos/*_completo` (startup, scaleup, enterprise, fintech, manufacturing, sector público).

Propósito de este archivo:

- Documentar, para SPRINT 1, cómo se valida a nivel de **diseño** que las invariantes `I1`–`I8` cuentan con artefactos de soporte suficientes para un VG4 MVO.
- Enfatizar la validación de `I3` (trazabilidad), `I5` (accountability humana), `I6` (trajectory-awareness) e `I8` (consistencia temporal), según `CAP-12`.

 > Nota: Esta validación sigue siendo principalmente conceptual/diseño y **cualitativa**; en SPRINT 6 se apoya en la existencia de 6 casos completos en `40_implementacion_metodologia/ejemplos` como evidencia de aplicación, pero deja fuera del alcance la validación cuantitativa con datos operativos reales.

---

## §1. Método de validación (VG4 v0.1)

1. Usar `03_vg4_validation_map.md` como índice para localizar, por invariante, los artefactos relevantes.
2. Verificar que cada invariante `I1`–`I8` tiene **al menos un** conjunto de artefactos de soporte ya existentes (sin crear nuevos IDs ni métricas).
3. Revisar consistencia semántica con `VOCABULARIO_CONTROLADO.yaml` y `DEPENDENCY_GRAPH.yaml` (sin violar el kernel `v1.0.0-kernel`).
4. Registrar hallazgos por invariante (cobertura y gaps conocidos) para informar decisiones de release.

---

## §1.1 Casos de evidencia VG4

- Casos considerados como evidencia cualitativa para VG4:
  - `40_implementacion_metodologia/ejemplos/01_startup_50p_completo/`
  - `40_implementacion_metodologia/ejemplos/02_scaleup_200p_completo/`
  - `40_implementacion_metodologia/ejemplos/03_enterprise_2000p_completo/`
  - `40_implementacion_metodologia/ejemplos/04_fintech_500p_completo/`
  - `40_implementacion_metodologia/ejemplos/05_manufacturing_800p_completo/`
  - `40_implementacion_metodologia/ejemplos/06_gore_nuble_completo/`

Cada caso se espera que cuente al menos con:

- `context.yaml`: instancia de `context_pattern_schema.yaml`.
- `trajectory.md`: trayectoria seleccionada usando `03_decision_matrix.md` + G1–G4.
- `artefactos.md`: lista de fases, playbooks, templates y calculadoras usadas con IDs canónicos.

Estos casos se usan como soporte transversal en la validación de I1–I8, especialmente en I2 (operación de arquitectura/tejidos en contextos reales), I3 (trazabilidad end-to-end), I6 (trajectory-awareness) e I8 (consistencia temporal).

## §2. Validación por invariante (resumen)

### §2.1 I1 – (resumen alto nivel)

- Evidencias principales (según mapa VG4):
  - Arquitectura y metodología núcleo (`out/00_fundamentos_teoricos.md`, `out/30_metodologia_orko.md`, `SPEC_ARQUITECTURA_DEFINITIVA.md`).
  - Casos de ejemplo (`01_startup_50p_completo` … `06_gore_nuble_completo`) que instancian el stack conceptual en contextos distintos.
- Evaluación v0.1:
  - Existen documentos que conectan GENOME ↔ FENOTIPO a nivel conceptual.
  - Se dispone de 6 casos completos que ilustran la aplicación de la metodología; la validación sigue centrada en existencia/consistencia más que en métricas de resultado.

### §2.2 I2 – (resumen alto nivel)

- Evidencias principales:
  - `out/10_arquitectura_orko.md`, `out/20_tejidos.md`.
  - Casos `01_startup_50p_completo` … `06_gore_nuble_completo`, que muestran configuraciones distintas de tejidos/arquitectura para contextos variados.
- Evaluación v0.1:
  - El diseño de capas arquitectónicas y tejidos está documentado.
  - Los 6 casos sirven como evidencia cualitativa de que la arquitectura y los tejidos son aplicables; sigue pendiente conectar estos diseños con resultados cuantitativos por caso.

### §2.3 I3 – Trazabilidad (FOCO)

- Evidencias principales:
  - Kernel semántico: `VOCABULARIO_CONTROLADO.yaml`, `DEPENDENCY_GRAPH.yaml`, `dependency_closure_script.py`, `KERNEL_READINESS.md`.
  - Health gates y métricas: `02_health_gates.md` (G1–G4, `H_org`, `eta_org`, `ROI_Habilitacion`).
  - Governance y trayectorias: `01_team_structure_raci.md`, `01_minimal_6_12_meses.md`, `02_avanzada_18_36_meses.md`, `04_survival_0_10K.md`, `03_decision_matrix.md`.
  - Coordinación: `board_coordinación.md`.
- Evaluación v0.1:
  - Existe trazabilidad explícita GENOME → VOCAB → DEP_GRAPH → Fases/Playbooks/Trayectorias → Health gates → Governance → Board.
  - `dependency_closure_script.py` valida que las referencias de DEP_GRAPH existen en VOCAB y que el grafo es DAG (salvo loops declarados).
  - Los 6 casos (`01_startup_50p_completo` … `06_gore_nuble_completo`) proporcionan rutas concretas de trazabilidad (context → Fases/Playbooks/Trayectorias → Health gates); se han tomado como referencia cualitativa para comprobar que cada capa tiene anclajes en ejemplos reales.
  - Gaps v0.1:
    - Aún falta formalizar un procedimiento estándar de auditoría "end-to-end" por caso (paso a paso) y documentar resultados caso por caso.

### §2.4 I4 – (resumen alto nivel)

- Evidencias principales:
  - Fases Development/Implementation: `F4`, `F5`, `F6`, `F10`, `F11`, `F12`.
  - Schemas de compliance y contexto (`compliance_framework_schema.yaml`, `context_pattern_schema.yaml`).
- Evaluación v0.1:
  - Las interfaces de estas fases y schemas están definidas de forma canónica.
  - Falta vincular explícitamente estas salidas con mejoras de `H_org`/`eta_org`/`ROI_Habilitacion` en ejemplos concretos.

### §2.5 I5 – Accountability humana (FOCO)

- Evidencias principales:
  - `01_team_structure_raci.md` (roles por gate G1–G4).
  - `02_health_gates.md` (quién detecta/decide/ejecuta/audita).
  - `board_coordinación.md` (registro de INTENT/OUTCOME/NEED/MANDATO/DECISIÓN).
- Evaluación v0.1:
  - Para los escenarios G1–G4 existe un RACI que asigna claramente responsabilidades humanas.
  - El board se usa como "ledger" de decisiones/mandatos del Capitán y equipos.
  - Gaps v0.1:
    - No hay aún un RACI fino por playbook ni evidencias empíricas de uso en entornos reales; la validación es de diseño.

### §2.6 I6 – Trajectory-awareness (FOCO)

- Evidencias principales:
  - Trayectorias: `01_minimal_6_12_meses.md`, `02_avanzada_18_36_meses.md`, `04_survival_0_10K.md`.
  - `03_decision_matrix.md` (condiciones G1–G4 + contexto → trayectoria recomendada).
  - `02_health_gates.md` (asociación gate ↔ trayectoria recomendada).
  - Casos `01_startup_50p_completo` … `06_gore_nuble_completo` donde se documenta explícitamente la trayectoria elegida y las decisiones de F3/F17 en `trajectory.md`.
- Evaluación v0.1:
  - Las decisiones de cambio de trayectoria se estructuran a través de G1–G4 y la decision_matrix, con `F3`/`F17` como fases explícitas de selección/adaptación.
  - La metodología es consciente de en qué trayectoria está operando y cuál sería la siguiente según gates/contexto; los 6 casos actúan como ejemplos concretos de estas decisiones.
  - Gaps v0.1:
    - Falta estandarizar cómo se anota el estado de trayectoria en artefactos operativos (OKR, backlogs, casos); se valida en términos de diseño, no de operación.

### §2.7 I7 – (resumen alto nivel)

- Evidencias principales:
  - Combinación de metodología (`out/30_metodologia_orko.md`) y tejidos (`out/20_tejidos.md`).
- Evaluación v0.1:
  - El diseño general respeta I7, pero se requieren ejemplos completos para validación profunda.

### §2.8 I8 – Consistencia temporal (FOCO)

- Evidencias principales:
  - Fases ligadas a tiempo y adaptación: `F6`, `F10`, `F11`, `F12`, `F15`, `F18` (ver docs correspondientes).
  - Health gates + decision_matrix como mecanismos para leer cambios en `H_org`/`eta_org`/`ROI_Habilitacion` y ajustar trayectoria.
  - `board_coordinación.md` como registro temporal de decisiones e hitos.
  - Casos `01_startup_50p_completo` … `06_gore_nuble_completo` que muestran cómo se distribuyen en el tiempo fases, playbooks y cambios de trayectoria en contextos distintos.
- Evaluación v0.1:
  - Existen mecanismos explícitos para leer el tiempo (health gates, quick wins, deployment/state_transition, cadencias) y para registrar decisiones a lo largo del sprint.
  - La consistencia temporal se valida de forma cualitativa (presencia de estos mecanismos) y usando los 6 casos como ejemplos; la validación cuantitativa queda fuera del alcance de este sprint.
  - Gaps v0.1:
    - No se han definido aún KPIs temporales adicionales ni series de tiempo concretas; la validación numérica de I8 queda fuera del alcance de SPRINT 1.

---

## §3. Conclusión VG4 v0.1

- Para SPRINT 1, las invariantes `I1`–`I8` cuentan con **soporte de diseño** suficiente en los artefactos ya creados, especialmente `I3`, `I5`, `I6` e `I8`.
- Los principales gaps identificados se relacionan con:
  - Ausencia de casos completos en producción (validación empírica).
  - Falta de procedimientos operativos estandarizados de auditoría por caso y anotación de trayectoria/tiempo.
- Este archivo y `03_vg4_validation_map.md` sirven como base para que el Capitán evalúe readiness de completion en SPRINT 1, sabiendo que la validación es de naturaleza principalmente conceptual.

