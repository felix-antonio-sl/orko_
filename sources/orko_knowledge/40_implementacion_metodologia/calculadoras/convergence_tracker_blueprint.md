# Convergence Tracker - Blueprint

Este documento describe la estructura y fórmulas para el archivo `convergence_tracker.xlsx`.

## Propósito
Calcular E6_current (estado arquitectónico actual), E6_target (estado objetivo) y convergence_score (progreso hacia el objetivo) para gestionar la convergencia organizacional.

## Fórmulas principales

### E6_current - Estado arquitectónico actual

```
Base = 0.60 * (H_org / 100) + 0.40 * ((TF1 + TF2 + TF3) / 3)
CF = clamp((context_complexity - 1) / 5, 0, 0.40)
E6_current = Base * (1 - CF)
```

**Componentes:**
- **Base:** Combinación ponderada de health organizacional (60%) y tissue fabrics (40%)
- **CF (Complexity Factor):** Penalización por complejidad contextual (0% a 40%)
- **context_complexity:** Escala 1-6 donde 1=simple, 6=altamente complejo

### E6_target - Estado arquitectónico objetivo

Depende de la trayectoria seleccionada:

| Trayectoria | Fórmula | Horizonte temporal |
|-------------|---------|-------------------|
| Survival | E6_current + 0.10 | 3 meses |
| Minimal | MIN(1.0, E6_current + 0.25) | 12 meses |
| Avanzada | MIN(1.0, E6_current + 0.50) | 24-36 meses |

**Nota:** E6 está acotado en el rango [0, 1]

### Convergence Score

```
Gap = E6_target - E6_current
Progress = (E6_current - E6_baseline) / (E6_target - E6_baseline)
Convergence_score = MAX(0, MIN(1, Progress))
```

**Donde:**
- **E6_baseline:** Valor de E6_current al inicio de la transformación
- **Progress:** Porcentaje de avance hacia el objetivo
- **Convergence_score:** 0 (no iniciado) a 1 (objetivo alcanzado)

### Métricas derivadas

```
Monthly_velocity = (E6_current - E6_baseline) / months_elapsed
Projected_months = Gap / Monthly_velocity  (si velocity > 0)
```

## Estructura del workbook

### Hoja 1: Inputs

| Parameter | Value | Type | Description |
|-----------|-------|------|-------------|
| H_org | 72 | numeric | Health score organizacional (0-100) |
| TF1_score | 0.70 | numeric | Tissue Fabric 1 - Capacity (0-1) |
| TF2_score | 0.68 | numeric | Tissue Fabric 2 - Flow (0-1) |
| TF3_score | 0.78 | numeric | Tissue Fabric 3 - Information (0-1) |
| context_complexity | 3 | numeric | Complejidad contextual (1-6) |
| trajectory | Minimal | categorical | Trayectoria seleccionada |
| E6_baseline | 0.40 | numeric | Valor inicial de E6 |
| months_elapsed | 6 | numeric | Meses transcurridos desde inicio |

**Named Ranges:** Definir cada parameter.

### Hoja 2: Calculations

#### Sección: E6_current

| Metric | Formula | Value |
|--------|---------|-------|
| Base | =0.6*(H_org/100) + 0.4*((TF1+TF2+TF3)/3) | 0.712 |
| CF | =MAX(0, MIN((context_complexity-1)/5, 0.40)) | 0.40 |
| E6_current | =Base*(1-CF) | 0.427 |

#### Sección: E6_target

| Trajectory | Formula | Value |
|------------|---------|-------|
| Survival | =E6_current + 0.10 | 0.527 |
| Minimal | =MIN(1, E6_current + 0.25) | 0.677 |
| Avanzada | =MIN(1, E6_current + 0.50) | 0.927 |
| **Selected** | =VLOOKUP(trajectory, ...) | 0.677 |

#### Sección: Convergence

| Metric | Formula | Value |
|--------|---------|-------|
| Gap | =E6_target - E6_current | 0.250 |
| Progress | =(E6_current - E6_baseline)/(E6_target - E6_baseline) | 0.097 |
| Convergence_score | =MAX(0, MIN(1, Progress)) | 0.097 |
| Monthly_velocity | =(E6_current - E6_baseline)/months_elapsed | 0.005 |
| Projected_months | =IF(Monthly_velocity>0, Gap/Monthly_velocity, 999) | 50 |

### Hoja 3: Dashboard

Visualización resumida:

```
┌─────────────────────────────────────────┐
│  CONVERGENCE TRACKER                    │
├─────────────────────────────────────────┤
│  Current State (E6_current): 0.43       │
│  Target State (E6_target):   0.68       │
│  Gap:                        0.25       │
│                                          │
│  Progress: [████░░░░░░] 9.7%            │
│  Convergence Score:     0.10            │
│                                          │
│  Velocity: 0.005/month                  │
│  Projected: 50 months to target         │
└─────────────────────────────────────────┘
```

Usar conditional formatting para barra de progreso.

### Hoja 4: Examples

#### Ejemplo 1: Caso 01 - Startup 50p (Trayectoria Minimal)

**Inputs:**
- H_org: 72
- TF1: 0.70, TF2: 0.68, TF3: 0.78
- context_complexity: 3
- trajectory: Minimal
- E6_baseline: 0.40
- months_elapsed: 6

**Resultados esperados:**
- E6_current: 0.43 ± 0.02
- E6_target: 0.68 (Minimal: +0.25)
- Gap: 0.25
- Convergence_score: ~0.10

#### Ejemplo 2: Caso 06 - GORE Ñuble (Trayectoria Survival)

**Inputs:**
- H_org: 66
- TF1: 0.65, TF2: 0.62, TF3: 0.62
- context_complexity: 4
- trajectory: Survival
- E6_baseline: 0.35
- months_elapsed: 3

**Resultados esperados:**
- E6_current: 0.38 ± 0.02
- E6_target: 0.48 (Survival: +0.10)
- Gap: 0.10
- Convergence_score: ~0.30

## Implementación en Excel

### Paso 1: Crear workbook
1. Crear archivo `convergence_tracker.xlsx`
2. Crear 4 hojas: Inputs, Calculations, Dashboard, Examples

### Paso 2: Hoja Inputs
1. Tabla parámetro-valor
2. Definir named ranges
3. Validación de datos (dropdown para trajectory)

### Paso 3: Hoja Calculations
1. Sección E6_current: Base, CF, E6_current
2. Sección E6_target: Tabla por trayectoria + VLOOKUP
3. Sección Convergence: Gap, Progress, Score, Velocity, Projected

### Paso 4: Hoja Dashboard
1. Diseño visual con celdas formateadas
2. Referencias a Calculations
3. Conditional formatting para barra de progreso
4. Gráfico de línea temporal (opcional)

### Paso 5: Hoja Examples
1. Sección por ejemplo con inputs
2. Botones/links para cargar en Inputs
3. Comparación resultado esperado vs. calculado

## Validación

Ejecutar los 2 ejemplos y verificar:

**Ejemplo 1 (Startup):**
- E6_current ≈ 0.43 (tolerancia ±0.02)
- E6_target = 0.68
- Convergence_score razonable

**Ejemplo 2 (GORE Ñuble):**
- E6_current ≈ 0.38 (tolerancia ±0.02)
- E6_target = 0.48
- Convergence_score razonable

Si los valores no coinciden:
1. Revisar fórmulas Base y CF
2. Verificar named ranges
3. Confirmar valores de TF1/TF2/TF3

## Uso operacional

### Actualización mensual
1. Actualizar H_org y TF scores desde dashboards
2. Incrementar months_elapsed
3. Revisar convergence_score y velocity
4. Si velocity < 0.005, activar P09 (Drift Detection)

### Triggers de playbooks
- **convergence_score < 0.20 después de 6 meses:** Activar P09
- **Gap aumentando:** Revisar E6_target o ejecutar P14/P15
- **velocity estancada:** Revisar playbooks de optimización (P11)

## Referencias
- `F9_target_state_design.md` - Fase que produce E6_target
- `F13_health_monitoring.md` - Fuente de H_org y TF scores
- `F18_convergence_check.md` - Fase que consume convergence_score
- `impl_cap22_run.py` - Script de validación Python
