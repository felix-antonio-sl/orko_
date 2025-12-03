# Health Score Calculator - Blueprint

Este documento describe la estructura y fórmulas para el archivo `health_score_calculator.xlsx`.

## Propósito
Calcular H_org (health score organizacional) a partir de 5 dimensiones (H_A..H_E) y múltiples indicadores de entrada.

## Estructura del workbook

### Hoja 1: Inputs

Contiene los valores de entrada normalizados (0-1):

| Campo | Tipo | Descripción |
|-------|------|-------------|
| strategic_clarity | 0-1 | Claridad estratégica |
| okr_alignment | 0-1 | Alineamiento OKR |
| leadership_commitment | 0-1 | Compromiso del liderazgo |
| TF1_score | 0-1 | Tissue Fabric 1 (Capacity) score |
| staffing_index | 0-1 | Índice de dotación |
| skill_index | 0-1 | Índice de habilidades |
| DORA_score | 0-1 | DORA metrics score normalizado |
| flow_stability | 0-1 | Estabilidad de flujo |
| handoff_ratio | 0-1 | Ratio de handoffs (menor es mejor) |
| data_quality | 0-1 | Calidad de datos |
| monitoring_coverage | 0-1 | Cobertura de monitoreo |
| decision_latency_score | 0-1 | Score de latencia de decisiones (normalizado, inverso) |
| governance_clarity | 0-1 | Claridad de gobernanza |

**Named Ranges:** Definir cada campo como named range (ej: `SC`, `OKR`, `LC`, etc.)

### Hoja 2: Formulas

Calcula los componentes H_A..H_E y H_org final:

#### Fórmulas de componentes

```
Cell B2 (H_A - Strategic Alignment):
=100*(0.5*SC + 0.3*OKR + 0.2*LC)

Cell B3 (H_B - Capacity):
=100*(0.6*TF1 + 0.25*STAFF + 0.15*SKILL)

Cell B4 (H_C - Flow):
=100*(0.5*DORA + 0.3*FLOW_STAB + 0.2*(1-HANDOFF))

Cell B5 (H_D - Information):
=100*(0.7*DQ + 0.3*MON_COV)

Cell B6 (H_E - Decision):
=100*(0.6*DEC_LAT + 0.4*GOV_CLAR)
```

#### Fórmula agregada

```
Cell B8 (H_org):
=0.30*H_A + 0.25*H_B + 0.20*H_C + 0.15*H_D + 0.10*H_E
```

**Nota:** Reemplazar `H_A`, `H_B`, etc. con referencias de celda apropiadas (ej: `B2`, `B3`, etc.)

### Hoja 3: Defaults

Tabla de valores default por nivel de madurez:

| maturity_level | strategic_clarity | okr_alignment | leadership_commitment | TF1_score | staffing_index | skill_index | DORA_score | flow_stability | handoff_ratio | data_quality | monitoring_coverage | decision_latency_score | governance_clarity |
|----------------|-------------------|---------------|-----------------------|-----------|----------------|-------------|------------|----------------|---------------|--------------|---------------------|------------------------|-------------------|
| low | 0.30 | 0.25 | 0.30 | 0.35 | 0.40 | 0.35 | 0.30 | 0.35 | 0.45 | 0.35 | 0.30 | 0.35 | 0.30 |
| mid | 0.60 | 0.55 | 0.60 | 0.65 | 0.65 | 0.60 | 0.60 | 0.65 | 0.25 | 0.65 | 0.60 | 0.60 | 0.60 |
| high | 0.85 | 0.80 | 0.85 | 0.85 | 0.85 | 0.80 | 0.85 | 0.85 | 0.10 | 0.85 | 0.85 | 0.80 | 0.85 |

**Uso:** Seleccionar maturity_level como input y popular automáticamente los valores de Inputs.

### Hoja 4: Lineage

Documentación de trazabilidad:

| output_field | source_fields | formula_cell | voca_reference |
|--------------|---------------|--------------|----------------|
| H_A | SC, OKR, LC | Formulas!B2 | VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.H_org.H_A |
| H_B | TF1, STAFF, SKILL | Formulas!B3 | VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.H_org.H_B |
| H_C | DORA, FLOW_STAB, HANDOFF | Formulas!B4 | VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.H_org.H_C |
| H_D | DQ, MON_COV | Formulas!B5 | VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.H_org.H_D |
| H_E | DEC_LAT, GOV_CLAR | Formulas!B6 | VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.H_org.H_E |
| H_org | H_A, H_B, H_C, H_D, H_E | Formulas!B8 | VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.H_org |

### Hoja 5: Examples

Casos de validación:

#### Ejemplo 1: Caso 01 - Startup 50p

| Campo | Valor |
|-------|-------|
| strategic_clarity | 0.68 |
| okr_alignment | 0.70 |
| leadership_commitment | 0.65 |
| TF1_score | 0.70 |
| staffing_index | 0.68 |
| skill_index | 0.72 |
| DORA_score | 0.75 |
| flow_stability | 0.78 |
| handoff_ratio | 0.20 |
| data_quality | 0.75 |
| monitoring_coverage | 0.82 |
| decision_latency_score | 0.68 |
| governance_clarity | 0.72 |

**Resultado esperado:** H_org ≈ 72

#### Ejemplo 2: Caso 06 - GORE Ñuble

| Campo | Valor |
|-------|-------|
| strategic_clarity | 0.60 |
| okr_alignment | 0.65 |
| leadership_commitment | 0.62 |
| TF1_score | 0.65 |
| staffing_index | 0.75 |
| skill_index | 0.75 |
| DORA_score | 0.55 |
| flow_stability | 0.65 |
| handoff_ratio | 0.32 |
| data_quality | 0.58 |
| monitoring_coverage | 0.70 |
| decision_latency_score | 0.62 |
| governance_clarity | 0.65 |

**Resultado esperado:** H_org ≈ 66

## Implementación en Excel

### Paso 1: Crear workbook
1. Crear archivo `health_score_calculator.xlsx`
2. Crear 5 hojas: Inputs, Formulas, Defaults, Lineage, Examples

### Paso 2: Hoja Inputs
1. Añadir campos en columna A (filas 1-13)
2. Añadir valores en columna B
3. Definir named ranges para cada campo

### Paso 3: Hoja Formulas
1. Columna A: Labels (H_A, H_B, H_C, H_D, H_E, H_org)
2. Columna B: Fórmulas (usar named ranges)
3. Formatear como porcentaje o número según corresponda

### Paso 4: Hojas restantes
1. Defaults: Copiar tabla de defaults
2. Lineage: Copiar tabla de lineage
3. Examples: Implementar casos de validación con referencias a Inputs

## Validación

Ejecutar casos de prueba en hoja Examples y verificar:
- Caso 01: H_org = 72 ± 2
- Caso 06: H_org = 66 ± 2

Si los valores no coinciden, revisar:
1. Named ranges correctamente definidos
2. Fórmulas sin errores de tipeo
3. Valores de entrada correctos

## Referencias
- `impl_cap22_run.py` - Script de validación Python
- `40_implementacion_metodologia/ejemplos/01_startup_50p_completo/artefactos.md`
- `40_implementacion_metodologia/ejemplos/06_gore_nuble_completo/artefactos.md`
