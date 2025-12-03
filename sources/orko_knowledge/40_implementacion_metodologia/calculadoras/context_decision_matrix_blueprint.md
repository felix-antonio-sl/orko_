# Context Decision Matrix - Blueprint

Este documento describe la estructura y reglas para el archivo `context_decision_matrix.xlsx`.

## Propósito
Decidir automáticamente la trayectoria apropiada (Survival, Minimal, Avanzada) basándose en condiciones contextuales cuantificables.

## Reglas de decisión (DM1..DM8)

Las reglas se evalúan en orden de prioridad (menor número = mayor prioridad). La primera regla que aplica determina el resultado.

### DM1: Crisis crítica (Prioridad 10)
- **Condición:** `H_org < 35 OR regulatory_risk == 5`
- **Resultado:** Survival
- **Rationale:** Salud organizacional crítica o riesgo regulatorio máximo requiere modo supervivencia

### DM2: Restricciones financieras severas (Prioridad 20)
- **Condición:** `budget_per_person_yr < 500 OR runway_months < 9`
- **Resultado:** Survival
- **Rationale:** Presupuesto insuficiente o runway corto limitan opciones de transformación

### DM3: Crisis combinada (Prioridad 30)
- **Condición:** `H_org < 50 AND (runway_months < 12 OR hypergrowth_flag == true)`
- **Resultado:** Survival
- **Rationale:** Salud débil combinada con presión temporal o crecimiento descontrolado

### DM4: Health bajo pero estable (Prioridad 40)
- **Condición:** `H_org >= 35 AND H_org < 60 AND regulatory_risk <= 3`
- **Resultado:** Minimal
- **Rationale:** Organización funcional pero necesita consolidación antes de expandir

### DM5: Recursos limitados (Prioridad 50)
- **Condición:** `budget_per_person_yr >= 500 AND budget_per_person_yr < 2000 AND H_org >= 50`
- **Resultado:** Minimal
- **Rationale:** Recursos moderados permiten consolidación pero no transformación agresiva

### DM6: Alto potencial (Prioridad 60)
- **Condición:** `H_org >= 70 AND budget_per_person_yr >= 2000 AND maturity_level == 'high'`
- **Resultado:** Avanzada
- **Rationale:** Alta salud, recursos adecuados y madurez permiten transformación profunda

### DM7: Crecimiento sostenible (Prioridad 70)
- **Condición:** `H_org >= 60 AND H_org < 70 AND budget_per_person_yr >= 1500`
- **Resultado:** Avanzada
- **Rationale:** Organización sana con recursos puede aspirar a transformación gradual

### DM8: Default (Prioridad 80)
- **Condición:** `true` (siempre aplica si ninguna anterior lo hizo)
- **Resultado:** Minimal
- **Rationale:** Opción segura por default cuando el contexto es ambiguo

## Estructura del workbook

### Hoja 1: Rules

Tabla de reglas:

| priority | id | condition_text | condition_eval | result | rationale | examples |
|----------|-----|----------------|----------------|--------|-----------|----------|
| 10 | DM1 | H_org < 35 OR regulatory_risk == 5 | =OR(H_org<35, regulatory_risk=5) | Survival | Crisis crítica | Caso startup en crisis |
| 20 | DM2 | budget_per_person < 500 OR runway < 9 | =OR(budget_pp<500, runway<9) | Survival | Restricciones financieras | Empresa pre-seed |
| 30 | DM3 | H_org < 50 AND (runway < 12 OR hypergrowth) | =AND(H_org<50, OR(runway<12, hypergrowth)) | Survival | Crisis combinada | Scale-up descontrolado |
| 40 | DM4 | 35 <= H_org < 60 AND risk <= 3 | =AND(H_org>=35, H_org<60, risk<=3) | Minimal | Health bajo estable | Empresa tradicional |
| 50 | DM5 | 500 <= budget_pp < 2000 AND H_org >= 50 | =AND(budget_pp>=500, budget_pp<2000, H_org>=50) | Minimal | Recursos limitados | SME consolidada |
| 60 | DM6 | H_org >= 70 AND budget_pp >= 2000 AND maturity=high | =AND(H_org>=70, budget_pp>=2000, maturity="high") | Avanzada | Alto potencial | Empresa madura |
| 70 | DM7 | 60 <= H_org < 70 AND budget_pp >= 1500 | =AND(H_org>=60, H_org<70, budget_pp>=1500) | Avanzada | Crecimiento sostenible | Scale-up sano |
| 80 | DM8 | true | =TRUE() | Minimal | Default seguro | Cualquier otro caso |

### Hoja 2: Inputs

Valores de entrada para evaluación:

| parameter | value | type |
|-----------|-------|------|
| H_org | 72 | numeric |
| budget_per_person_yr | 1200 | numeric |
| runway_months | 18 | numeric |
| regulatory_risk | 2 | numeric (1-5) |
| maturity_level | mid | categorical |
| hypergrowth_flag | false | boolean |

**Named Ranges:** Definir cada parameter como named range.

### Hoja 3: Evaluation

Tabla de evaluación automática:

| rule_id | applies | result_if_applies |
|---------|---------|-------------------|
| DM1 | =Rules!D2 | =IF(B2, Rules!E2, "") |
| DM2 | =Rules!D3 | =IF(B3, Rules!E3, "") |
| ... | ... | ... |
| DM8 | =Rules!D10 | =IF(B10, Rules!E10, "") |

**Selected Trajectory (celda destacada):**
```
=INDEX(C:C, MATCH(TRUE, B:B, 0))
```

Esta fórmula retorna el resultado de la primera regla que aplica.

### Hoja 4: Examples

Casos de prueba:

#### Ejemplo 1: Startup en crisis
- H_org: 32
- budget_per_person_yr: 800
- runway_months: 6
- regulatory_risk: 3
- maturity_level: low
- hypergrowth_flag: false

**Resultado esperado:** Survival (DM1)

#### Ejemplo 2: SME consolidada
- H_org: 58
- budget_per_person_yr: 1500
- runway_months: 24
- regulatory_risk: 2
- maturity_level: mid
- hypergrowth_flag: false

**Resultado esperado:** Minimal (DM4)

#### Ejemplo 3: Empresa madura
- H_org: 75
- budget_per_person_yr: 3000
- runway_months: 36
- regulatory_risk: 1
- maturity_level: high
- hypergrowth_flag: false

**Resultado esperado:** Avanzada (DM6)

## Implementación en Excel

### Paso 1: Crear workbook
1. Crear archivo `context_decision_matrix.xlsx`
2. Crear 4 hojas: Rules, Inputs, Evaluation, Examples

### Paso 2: Hoja Rules
1. Crear tabla con columnas: priority, id, condition_text, condition_eval, result, rationale, examples
2. Llenar con las 8 reglas DM1..DM8
3. Ordenar por priority ascendente

### Paso 3: Hoja Inputs
1. Crear tabla parámetro-valor
2. Definir named ranges para cada parámetro
3. Validar tipos (numeric, categorical, boolean)

### Paso 4: Hoja Evaluation
1. Columna A: rule_id (DM1..DM8)
2. Columna B: applies (fórmula que evalúa condition_eval)
3. Columna C: result_if_applies (IF que retorna resultado solo si aplica)
4. Celda destacada: Primera regla que aplica usando INDEX/MATCH

### Paso 5: Hoja Examples
1. Crear sección para cada ejemplo
2. Botones/links para cargar valores en Inputs
3. Verificar resultado en Evaluation

## Validación

Probar los 3 ejemplos y verificar:
1. Ejemplo 1 → Survival
2. Ejemplo 2 → Minimal
3. Ejemplo 3 → Avanzada

Si alguno falla:
1. Verificar condition_eval sin errores sintácticos
2. Verificar named ranges correctos
3. Verificar orden de prioridades

## Referencias
- `F3_trajectory_selection.md` - Fase que consume esta matriz
- `context_pattern_schema.yaml` - Schema de contextos
- `case_instances.yaml` - Casos reales para calibración
