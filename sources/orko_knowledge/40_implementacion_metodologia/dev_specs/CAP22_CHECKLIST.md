# CAP-22 Validation Checklist

## Definition of Done (DoD)

### Calculadoras Excel

#### Health Score Calculator
- [ ] Archivo `health_score_calculator.xlsx` creado
- [ ] Hoja **Inputs** con campos:
  - [ ] strategic_clarity (0..1)
  - [ ] okr_alignment (0..1)
  - [ ] leadership_commitment (0..1)
  - [ ] TF1_score (0..1)
  - [ ] staffing_index (0..1)
  - [ ] skill_index (0..1)
  - [ ] DORA_score (0..1)
  - [ ] flow_stability (0..1)
  - [ ] handoff_ratio (0..1)
  - [ ] data_quality (0..1)
  - [ ] monitoring_coverage (0..1)
  - [ ] decision_latency_score (0..1)
  - [ ] governance_clarity (0..1)
- [ ] Hoja **Formulas** con:
  - [ ] H_A = 100 * (0.50*SC + 0.30*OKR + 0.20*LC)
  - [ ] H_B = 100 * (0.60*TF1 + 0.25*staffing + 0.15*skill)
  - [ ] H_C = 100 * (0.50*DORA + 0.30*flow_stability + 0.20*(1-handoff_ratio))
  - [ ] H_D = 100 * (0.70*data_quality + 0.30*monitoring_coverage)
  - [ ] H_E = 100 * (0.60*decision_latency + 0.40*governance_clarity)
  - [ ] H_org = 0.30*H_A + 0.25*H_B + 0.20*H_C + 0.15*H_D + 0.10*H_E
- [ ] Hoja **Defaults** con tabla maturity_level → valores default
- [ ] Hoja **Lineage** con columnas: output_field, source_fields, formula_cell, voca_reference
- [ ] Hoja **Examples** con casos 01 y 06
  - [ ] Caso 01: H_org ≈ 72 (±2)
  - [ ] Caso 06: H_org ≈ 66 (±2)

#### Context Decision Matrix
- [ ] Archivo `context_decision_matrix.xlsx` creado
- [ ] Columnas: priority, id, condition_text, condition_eval, result, rationale, examples
- [ ] 8 reglas implementadas (DM1..DM8)
- [ ] Prioridades: 10, 20, 30, 40, 50, 60, 70, 80
- [ ] Resultados: Survival, Minimal, Avanzada
- [ ] Fórmulas lógicas en condition_eval funcionales

#### Convergence Tracker
- [ ] Archivo `convergence_tracker.xlsx` creado
- [ ] Fórmula E6_current implementada:
  - [ ] Base = 0.60*(H_org/100) + 0.40*(TF1+TF2+TF3)/3
  - [ ] CF = clamp((complexity-1)/5, 0, 0.40)
  - [ ] E6_current = Base * (1 - CF)
- [ ] Tabla E6_target por trayectoria:
  - [ ] Survival: E6_current + 0.10 (3 meses)
  - [ ] Minimal: min(1, E6_current + 0.25) (12 meses)
  - [ ] Avanzada: min(1, E6_current + 0.50) (24-36 meses)
- [ ] Outputs: E6_current, E6_target, Gap, Convergence_score, monthly_velocity, projected_months
- [ ] Casos de prueba:
  - [ ] Caso 01: E6_current ≈ 0.43 (±0.02)
  - [ ] Caso 06: E6_current ≈ 0.38 (±0.02)

### Scripts

#### impl_cap22_run.py
- [ ] Script ejecuta sin errores
- [ ] Función `compute_H_org` implementada
- [ ] Función `compute_E6` implementada
- [ ] Funciones demo para casos 01 y 06
- [ ] Output coincide con valores esperados:
  - [ ] Caso 01: H_org=72, E6_current=0.43
  - [ ] Caso 06: H_org=66, E6_current=0.38

### Blueprints

- [ ] `health_score_calculator_blueprint.md` creado
- [ ] `context_decision_matrix_blueprint.md` creado
- [ ] `convergence_tracker_blueprint.md` creado
- [ ] Todos los blueprints incluyen:
  - [ ] Descripción de hojas
  - [ ] Fórmulas Excel
  - [ ] Ejemplos de celdas
  - [ ] Estructura de lineage

### Documentación

- [ ] `CAP22_IMPL_GUIDE.md` creado con:
  - [ ] Objetivos claros
  - [ ] Pasos de implementación
  - [ ] Criterios de éxito
  - [ ] Referencias
- [ ] `CAP22_CHECKLIST.md` (este archivo) completado

### FUNDAMENTOS (§0)

- [ ] F7_purpose_cascade.md actualizado con §0 STABLE
- [ ] F9_target_state_design.md actualizado con §0 STABLE
- [ ] F14_incident_response.md actualizado con §0 STABLE
- [ ] F15_continuous_execution.md actualizado con §0 STABLE
- [ ] F17_adaptation.md actualizado con §0 STABLE
- [ ] F18_convergence_check.md actualizado con §0 STABLE

### Playbooks

- [ ] P14_client_expectation_mgmt.md actualizado a estado mvo
- [ ] P15_adaptive_cadence.md actualizado a estado mvo
- [ ] playbook_schema.yaml actualizado a v0.2 con:
  - [ ] Campo triggers_examples
  - [ ] Campo raci
  - [ ] Campo acceptance_criteria
- [ ] playbook_instances.yaml actualizado:
  - [ ] P14 estado = mvo
  - [ ] P15 estado = mvo

## Validación E2E

### Paso 1: Validar scripts
```bash
cd 40_implementacion_metodologia/dev_specs/scripts
python3 impl_cap22_run.py
```
Resultado esperado:
```
CASE 01 (startup): {'H_org': 72, 'E6_current': 0.43}
CASE 06 (GORE Ñuble): {'H_org': 66, 'E6_current': 0.38}
```

### Paso 2: Validar calculadoras Excel
1. Abrir `health_score_calculator.xlsx`
2. Ir a hoja Examples
3. Verificar que caso 01 produce H_org ≈ 72
4. Verificar que caso 06 produce H_org ≈ 66

### Paso 3: Validar lineage
```bash
cd 40_implementacion_metodologia/dev_specs/scripts
python3 dependency_closure_script.py
```
- [ ] Sin errores de dependencias circulares
- [ ] Lineage completo para H_org → VOCABULARIO_CONTROLADO

### Paso 4: Validar integración
- [ ] Playbooks P14/P15 referenciados correctamente en playbook_instances.yaml
- [ ] Schema v0.2 valida sin errores
- [ ] FUNDAMENTOS F7/F9/F14/F15/F17/F18 con estado STABLE

## Criterios de aceptación final

- [ ] Todas las calculadoras reproducen valores simulados (tolerancia ±2%)
- [ ] Scripts ejecutan sin errores
- [ ] FUNDAMENTOS completos con §0 STABLE
- [ ] Playbooks P14/P15 en estado mvo
- [ ] Schema v0.2 implementado
- [ ] Lineage documentado
- [ ] Tests E2E pasan

## Aprobaciones requeridas

- [ ] Arquitecto (technical review)
- [ ] Owner metodológico (content review)
- [ ] PMO (process compliance)

## Notas
- Tolerancia de ±2 puntos en H_org por redondeo
- Tolerancia de ±0.02 en E6_current
- Validar visualmente las fórmulas Excel antes de cerrar
