# GUÍA DE IMPLEMENTACIÓN CAP-22 – CALCULADORAS ORKO

## Propósito
Documentación técnica para implementar las 3 calculadoras .xlsx operativas según `CALCULADORAS_P0_SPEC.md`.

**Enfoque:** Dado que los .xlsx son archivos binarios no editables directamente en texto plano, esta guía especifica:
1. Estructura exacta de hojas y celdas
2. Fórmulas Excel a implementar
3. Validaciones y formato
4. Método de generación (script Python + openpyxl o edición manual)

---

## 1. HEALTH_SCORE_CALCULATOR.XLSX

### Estructura de hojas:
1. **Inputs** - Parámetros de entrada editables
2. **Parametros** - Pesos y umbrales fenotípicos
3. **Calculos** - Cálculos intermedios (TF scores, A/P/D)
4. **Outputs** - H_org, health_band, recomendaciones
5. **Metadata** - Trazabilidad y versión

### Inputs (hoja 1):
| Celda | Variable | Valor inicial | Descripción |
|-------|----------|---------------|-------------|
| C3 | org_size | 50 | Número de personas |
| C4 | context_complexity | 3 | Escala 1-5 |
| C5 | budget_available | 50000000 | CLP/USD |
| C6 | current_state_maturity | 2 | Escala 1-5 |
| C7 | strategic_clarity | 60 | % (0-100) |
| C8 | TF1_capacity_deployed | 40 | % |
| C9 | TF2_flow_instrumented | 30 | % |
| C10 | TF3_info_governed | 25 | % |

### Parametros (hoja 2):
| Celda | Parámetro | Valor | Descripción |
|-------|-----------|-------|-------------|
| C3 | w_A | 0.33 | Peso Alignment |
| C4 | w_P | 0.33 | Peso Performance |
| C5 | w_D | 0.34 | Peso Development |
| C7 | TF1_weight | 0.40 | Peso tejido TF1 |
| C8 | TF2_weight | 0.35 | Peso tejido TF2 |
| C9 | TF3_weight | 0.25 | Peso tejido TF3 |
| C11 | maturity_floor | 0.35 | H_org mínimo viable |

### Calculos (hoja 3):
| Celda | Métrica | Fórmula Excel |
|-------|---------|---------------|
| C3 | TF1_Score | =Inputs!C8/100 |
| C4 | TF2_Score | =Inputs!C9/100 |
| C5 | TF3_Score | =Inputs!C10/100 |
| C7 | A_Score | =(Inputs!C7/100)*0.6 + C3*0.4 |
| C8 | P_Score | =C4*0.7 + (Inputs!C6/5)*0.3 |
| C9 | D_Score | =C5*0.5 + (1-(Inputs!C3/1000))*0.3 + 0.2 |

### Outputs (hoja 4):
| Celda | Métrica | Fórmula Excel |
|-------|---------|---------------|
| C3 | H_org | =Parametros!C3*Calculos!C7 + Parametros!C4*Calculos!C8 + Parametros!C5*Calculos!C9 |
| C4 | Health_Band | =IF(C3<0.35,"G1-Crítico",IF(C3<0.55,"G2-Bajo",IF(C3<0.75,"G3-Aceptable","G4-Saludable"))) |
| C6 | A_Score | =Calculos!C7 |
| C7 | P_Score | =Calculos!C8 |
| C8 | D_Score | =Calculos!C9 |

---

## 2. CONTEXT_DECISION_MATRIX.XLSX

### Estructura de hojas:
1. **Context_Inputs** - H_org, budget, org_size, riesgo
2. **Parametros** - Umbrales de trayectorias
3. **Decision_Rules** - Lógica DM1-DM5
4. **Trajectory_Output** - Trayectoria seleccionada y rationale
5. **Playbook_Mapping** - Playbooks por trayectoria
6. **Metadata**

### Context_Inputs (hoja 1):
| Celda | Variable | Valor inicial |
|-------|----------|---------------|
| C3 | H_org | 0.55 |
| C4 | budget_total | 50000000 |
| C5 | org_size | 50 |
| C6 | context_risk | 3 |
| C7 | strategic_horizon | 12 |
| C8 | current_maturity | 2 |

### Trajectory_Output (hoja 4):
| Celda | Métrica | Fórmula Excel |
|-------|---------|---------------|
| C3 | trajectory_selected | =IF(Context_Inputs!C3<Parametros!C4,"Survival",IF(Context_Inputs!C3<Parametros!C6,"Minimal","Avanzada")) |
| C4 | rationale | =IF(C3="Survival","H_org bajo o riesgo alto",IF(C3="Minimal","Condiciones intermedias","Alta madurez y recursos")) |
| C5 | health_band_used | =IF(Context_Inputs!C3<0.35,"G1",IF(Context_Inputs!C3<0.55,"G2",IF(Context_Inputs!C3<0.75,"G3","G4"))) |

---

## 3. CONVERGENCE_TRACKER.XLSX

### Estructura de hojas:
1. **E6_Current** - Estado actual (TF1/TF2/TF3 current, H_org_current)
2. **E6_Target** - Estado objetivo (TF1/TF2/TF3 target, H_org_target)
3. **Parametros** - Pesos y umbral de convergencia
4. **Gap_Analysis** - Cálculo de ratios y convergence_score
5. **Projections** - Estimación tiempo a target
6. **Metadata**

### E6_Current (hoja 1):
| Celda | Variable | Valor inicial |
|-------|----------|---------------|
| C3 | TF1_current_capacity_count | 5 |
| C4 | TF2_current_flow_count | 3 |
| C5 | TF3_current_info_artifacts | 8 |
| C6 | H_org_current | 0.55 |

### E6_Target (hoja 2):
| Celda | Variable | Valor inicial |
|-------|----------|---------------|
| C3 | TF1_target_capacity_count | 12 |
| C4 | TF2_target_flow_count | 8 |
| C5 | TF3_target_info_artifacts | 20 |
| C6 | H_org_target | 0.75 |

### Gap_Analysis (hoja 4):
| Celda | Métrica | Fórmula Excel |
|-------|---------|---------------|
| C3 | TF1_convergence_ratio | =MIN(1, E6_Current!C3/E6_Target!C3) |
| C4 | TF2_convergence_ratio | =MIN(1, E6_Current!C4/E6_Target!C4) |
| C5 | TF3_convergence_ratio | =MIN(1, E6_Current!C5/E6_Target!C5) |
| C6 | H_org_convergence_ratio | =MIN(1, E6_Current!C6/E6_Target!C6) |
| C8 | Convergence_Score | =Parametros!C3*C3 + Parametros!C4*C4 + Parametros!C5*C5 + Parametros!C6*C6 |
| C9 | Convergence_Status | =IF(C8>=Parametros!C8,"Converged",IF(C8>=0.5,"In Progress","Lagging")) |

---

## MÉTODO DE IMPLEMENTACIÓN

### Opción A: Generación programática (recomendada)
Crear script Python usando `openpyxl` que genere los .xlsx con la estructura especificada.

```bash
cd 40_implementacion_metodologia/dev_specs/scripts
python generate_calculadoras_cap22.py
```

### Opción B: Edición manual en Excel/LibreOffice
1. Abrir cada .xlsx placeholder
2. Crear las hojas especificadas
3. Ingresar fórmulas y datos según tablas anteriores
4. Aplicar formato y validaciones
5. Guardar

---

## VALIDACIÓN POST-IMPLEMENTACIÓN

Checklist para verificar que los .xlsx son operativos:

**health_score_calculator.xlsx:**
- [ ] Inputs: 8 variables editables con valores iniciales
- [ ] Calculos: TF scores, A/P/D scores se calculan correctamente
- [ ] Outputs: H_org ∈ [0,1], health_band asignada correctamente
- [ ] Metadata: Trazabilidad a VOCAB, axiomas, tejidos documentada

**context_decision_matrix.xlsx:**
- [ ] Inputs: H_org, budget, org_size editables
- [ ] Trajectory_Output: Selecciona Survival/Minimal/Avanzada según inputs
- [ ] Playbook_Mapping: Lista correcta de playbooks por trayectoria
- [ ] Metadata: Referencias a F1/F3, DM1-DM5, health gates

**convergence_tracker.xlsx:**
- [ ] E6_Current/Target: Valores editables para TF1/TF2/TF3 y H_org
- [ ] Gap_Analysis: Convergence_score se calcula correctamente
- [ ] Projections: Status "Converged/In Progress/Lagging" coherente
- [ ] Metadata: Referencias a F9/F18, primitivo E6, invariante I3

---

**Estado:** Guía de implementación CAP-22 completada  
**Siguiente paso:** Ejecutar generación de .xlsx y validar con casos 01/06  
**Fecha:** 2025-11-18
