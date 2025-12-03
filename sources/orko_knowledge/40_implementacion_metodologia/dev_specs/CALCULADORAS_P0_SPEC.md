# ESPECIFICACIÓN P0 – CALCULADORAS ORKO v1.0.0

## §0 PROPÓSITO Y ALCANCE

**Objetivo:** Definir la estructura conceptual y fórmulas de las tres calculadoras ORKO sin modificar kernel, VOCAB, DEP_GRAPH ni introducir métricas canónicas nuevas.

**Alcance P0-COMPLETE:**
- Especificación textual de inputs/outputs/parámetros/fórmulas.
- Trazabilidad a `out/00_fundamentos_teoricos.md`, `out/20_tejidos.md`, `out/30_metodologia_orko.md`.
- Separación explícita: **genoma** (no modificable) vs **fenotipo** (parametrizable por contexto).
- NO se modifican los `.xlsx` existentes en esta fase.

**Calculadoras cubiertas:**
1. `health_score_calculator.xlsx` – H_org y componentes A/P/D_Score
2. `context_decision_matrix.xlsx` – Selección de trayectoria (Survival/Minimal/Avanzada)
3. `convergence_tracker.xlsx` – Convergencia E6_current → E6_target

---

## §1 HEALTH_SCORE_CALCULATOR

### 1.1 Propósito
Calcular **H_org** (salud organizacional) como métrica canónica de estado actual del sistema de trabajo, descompuesta en:
- **A_Score** (Alignment) – coherencia con propósito/estrategia
- **P_Score** (Performance) – desempeño operativo actual
- **D_Score** (Development) – capacidad de evolución y aprendizaje

### 1.2 Fundamento genómico
- **Métrica canónica:** `H_org` (definida en `out/00_fundamentos_teoricos.md` §4.3 Teorema T6)
- **Ecuación master:** `V_org = f(H_org, η_org, ROI_Habilitacion, t)`
- **Invariantes aplicables:** I1 (conservación de propósito), I3 (no-regresión de capacidad instalada), I6 (health gates obligatorios)
- **Tejidos tecnológicos:** TF1_Capacity, TF2_Flow, TF3_Information (`out/20_tejidos.md`)
- **Health gates:** G1–G4 (`30_metodologia_orko/13_metricas_validacion/02_health_gates.md`)

### 1.3 Estructura de hoja propuesta

**Tab 1: INPUTS**
- `org_size` (número de personas) – INT
- `context_complexity` (1–5) – valoración cualitativa de complejidad del contexto
- `budget_available` (CLP o USD) – presupuesto total disponible para habilitación
- `current_state_maturity` (1–5) – autoevaluación de madurez actual del WS
- `strategic_clarity` (0–100%) – % de claridad en propósito/estrategia
- `TF1_capacity_deployed` (0–100%) – % capacidades críticas desplegadas
- `TF2_flow_instrumented` (0–100%) – % flujos core instrumentados
- `TF3_info_governed` (0–100%) – % información bajo gobierno explícito

**Tab 2: PARÁMETROS (fenotipo)**
- `w_A`, `w_P`, `w_D` – pesos relativos de A/P/D en H_org (default: 0.33, 0.33, 0.34; suma=1.0)
- `TF1_weight`, `TF2_weight`, `TF3_weight` – ponderación de tejidos (default: 0.4, 0.35, 0.25)
- `maturity_floor` – piso mínimo de H_org considerado viable (default: 0.35)
- `critical_threshold_G1` – umbral de alerta temprana (default: H_org < 0.50)

**Tab 3: CÁLCULOS INTERMEDIOS**
- **TF1_Score** = `TF1_capacity_deployed / 100`
- **TF2_Score** = `TF2_flow_instrumented / 100`
- **TF3_Score** = `TF3_info_governed / 100`
- **A_Score** = `(strategic_clarity/100) * 0.6 + TF1_Score * 0.4`
- **P_Score** = `TF2_Score * 0.7 + current_state_maturity/5 * 0.3`
- **D_Score** = `TF3_Score * 0.5 + (1 - (org_size/max_org_size_in_sample)) * 0.3 + (budget_available/org_size > threshold_per_capita ? 0.2 : 0.0)`

**Tab 4: OUTPUTS**
- **H_org** = `w_A * A_Score + w_P * P_Score + w_D * D_Score`
- **Health_Band** = asignación a G1/G2/G3/G4 según rangos:
  - G1 (crítico): H_org < 0.35
  - G2 (bajo): 0.35 ≤ H_org < 0.55
  - G3 (aceptable): 0.55 ≤ H_org < 0.75
  - G4 (saludable): H_org ≥ 0.75
- **Recommended_Actions** (lookup desde health gates)
- **Next_Assessment_Date** (F13 recomienda cada 3–6 meses según banda)

### 1.4 Validaciones internas
- Suma de pesos `w_A + w_P + w_D = 1.0` ± 0.01
- Todos los scores intermedios ∈ [0, 1]
- H_org ∈ [0, 1]
- Si H_org < `maturity_floor`, marcar flag de alerta crítica

### 1.5 Conexión con fases WSLC
- **F1** (Context Assessment): provee `org_size`, `context_complexity`, `strategic_clarity`
- **F13** (Health Monitoring): consume H_org y health_band para decisiones de intervención
- **F3** (Trajectory Selection): usa H_org como input crítico para decidir trayectoria

---

## §2 CONTEXT_DECISION_MATRIX

### 2.1 Propósito
Determinar la **trayectoria** recomendada (`Survival`, `Minimal`, `Avanzada`) a partir de:
- H_org (salud actual)
- Budget disponible
- Complejidad/riesgo del contexto
- Madurez del WS

Alineado con `30_metodologia_orko/09_trayectorias/03_decision_matrix.md` y health gates G1–G4.

### 2.2 Fundamento genómico
- **Primitivo P6:** Work System Life Cycle (WSLC) – las trayectorias son instancias fenotípicas de WSLC
- **Invariante I6:** Health gates obligatorios antes de avanzar de fase
- **Teorema T7:** Trayectorias válidas (`out/00_fundamentos_teoricos.md`)
- **Health gates G1–G4:** Bandas de riesgo/capacidad (`02_health_gates.md`)

### 2.3 Estructura de hoja propuesta

**Tab 1: INPUTS**
- `H_org` (desde health_score_calculator o manual) – REAL ∈ [0,1]
- `budget_total` (CLP/USD)
- `org_size` (personas)
- `context_risk` (1–5) – 1=bajo riesgo, 5=alto riesgo/urgencia
- `strategic_horizon` (meses) – horizonte de planificación
- `current_maturity` (1–5)

**Tab 2: PARÁMETROS (fenotipo)**
- `budget_per_capita_threshold_minimal` (ej: 500 USD/persona/año)
- `budget_per_capita_threshold_avanzada` (ej: 2000 USD/persona/año)
- `h_org_floor_survival` (default: 0.35)
- `h_org_floor_minimal` (default: 0.50)
- `h_org_floor_avanzada` (default: 0.65)

**Tab 3: REGLAS DE DECISIÓN (DM1–DM5)**

Lógica secuencial:

**DM1 (Crisis inmediata):**
```
IF H_org < h_org_floor_survival OR context_risk = 5 THEN
  trajectory_selected = "Survival"
  rationale = "Salud crítica o contexto de crisis"
END IF
```

**DM2 (Presupuesto insuficiente):**
```
IF (budget_total / org_size) < budget_per_capita_threshold_minimal THEN
  trajectory_selected = "Survival"
  rationale = "Presupuesto bajo umbral mínimo"
END IF
```

**DM3 (Madurez y salud baja-media):**
```
IF H_org < h_org_floor_avanzada AND current_maturity ≤ 3 THEN
  trajectory_selected = "Minimal"
  rationale = "Salud aceptable pero madurez limitada"
END IF
```

**DM4 (Presupuesto y salud permiten avanzada):**
```
IF H_org ≥ h_org_floor_avanzada 
   AND (budget_total / org_size) ≥ budget_per_capita_threshold_avanzada
   AND current_maturity ≥ 4 THEN
  trajectory_selected = "Avanzada"
  rationale = "Alta salud, presupuesto robusto, madurez sólida"
END IF
```

**DM5 (Default: Minimal):**
```
ELSE
  trajectory_selected = "Minimal"
  rationale = "Condiciones intermedias, enfoque balanceado"
END IF
```

**Tab 4: OUTPUTS**
- `trajectory_selected` (Survival | Minimal | Avanzada)
- `rationale` (texto explicativo de la regla aplicada)
- `health_band_used` (G1/G2/G3/G4 derivada de H_org)
- `estimated_duration_months` (lookup desde `03_decision_matrix.md`)
- `key_constraints` (lista de restricciones detectadas: budget, madurez, riesgo)

**Tab 5: MAPPING A PLAYBOOKS**
Para cada trayectoria, listar playbooks recomendados:
- **Survival:** P01, P02, P13 (contexto, quick-wins, health mínimo)
- **Minimal:** P01–P06, P13 (Initiation + Development core + Health)
- **Avanzada:** P01–P15 (ciclo completo WSLC)

### 2.4 Validaciones internas
- `trajectory_selected` debe ser uno de {Survival, Minimal, Avanzada}
- Si H_org < 0.35, forzar Survival independiente de otros parámetros
- Alertar si presupuesto/persona < umbral mínimo pero trayectoria != Survival

### 2.5 Conexión con fases WSLC
- **F3** (Trajectory Selection): esta calculadora ES el artefacto ejecutable de F3
- **F1** (Context Assessment): provee inputs de contexto, riesgo, madurez
- **F4–F9** (Development): la trayectoria seleccionada determina el alcance de diseño

---

## §3 CONVERGENCE_TRACKER

### 3.1 Propósito
Medir la **convergencia** entre el estado arquitectónico actual (`E6_current`) y el estado objetivo (`E6_target`) a lo largo del ciclo de habilitación.

Usado en:
- **F9** (Transition Planning)
- **F18** (Continuous Evolution)
- Validación de que el sistema converge hacia el diseño objetivo (invariante I3).

### 3.2 Fundamento genómico
- **Primitivo P5:** Architectural State (E6 en `20_tejidos/07_architectural_state_management.md`)
- **Invariante I3:** No-regresión de capacidad instalada
- **Tejidos TF1/TF2/TF3:** Capacidad/Flow/Info como dimensiones de E6
- **Ecuación master:** V_org debe crecer o estabilizarse, no decrecer sin justificación

### 3.3 Estructura de hoja propuesta

**Tab 1: INPUTS – E6_CURRENT**
- `TF1_current_capacity_count` (# capacidades desplegadas hoy)
- `TF2_current_flow_count` (# flujos instrumentados hoy)
- `TF3_current_info_artifacts` (# artefactos info bajo gobierno hoy)
- `H_org_current` (salud actual, desde health_score_calculator)
- `timestamp_current` (fecha de medición)

**Tab 2: INPUTS – E6_TARGET**
- `TF1_target_capacity_count` (# capacidades en diseño objetivo)
- `TF2_target_flow_count` (# flujos en diseño objetivo)
- `TF3_target_info_artifacts` (# artefactos info en diseño objetivo)
- `H_org_target` (salud esperada post-habilitación)
- `timestamp_target` (fecha objetivo de convergencia)

**Tab 3: PARÁMETROS (fenotipo)**
- `convergence_threshold` (default: 0.85) – % mínimo para considerar "converged"
- `weight_TF1`, `weight_TF2`, `weight_TF3` (ponderación de tejidos; default: 0.4, 0.35, 0.25)
- `weight_H_org` (default: 0.30) – peso de delta de salud en métrica de convergencia

**Tab 4: CÁLCULOS INTERMEDIOS**
- **TF1_convergence_ratio** = `TF1_current_capacity_count / TF1_target_capacity_count` (cap en 1.0)
- **TF2_convergence_ratio** = `TF2_current_flow_count / TF2_target_flow_count` (cap en 1.0)
- **TF3_convergence_ratio** = `TF3_current_info_artifacts / TF3_target_info_artifacts` (cap en 1.0)
- **H_org_convergence_ratio** = `H_org_current / H_org_target` (cap en 1.0)

**Tab 5: OUTPUTS**
- **Convergence_Score** = 
  ```
  weight_TF1 * TF1_convergence_ratio +
  weight_TF2 * TF2_convergence_ratio +
  weight_TF3 * TF3_convergence_ratio +
  weight_H_org * H_org_convergence_ratio
  ```
- **Convergence_Status** = 
  - `"Converged"` si Convergence_Score ≥ convergence_threshold
  - `"In Progress"` si 0.50 ≤ Convergence_Score < convergence_threshold
  - `"Lagging"` si Convergence_Score < 0.50
- **Delta_TF1, Delta_TF2, Delta_TF3, Delta_H_org** (valores absolutos de gap)
- **Estimated_Time_To_Target** (meses restantes, interpolación lineal desde velocity histórica si disponible)
- **Recommendations** (texto): qué tejido/dimensión priorizar para acelerar convergencia

**Tab 6: TREND ANALYSIS (opcional)**
Si hay mediciones previas de E6_current:
- **Velocity_TF1/TF2/TF3** (cambio promedio por mes)
- **Trajectory_Projection** (¿llegará a E6_target antes de `timestamp_target`?)

### 3.4 Validaciones internas
- Todos los ratios de convergencia ∈ [0, 1]
- Convergence_Score ∈ [0, 1]
- Si algún ratio > 1.0, capear a 1.0 y marcar nota de "sobre-delivery"
- Alerta si Convergence_Status = "Lagging" y fecha objetivo < 6 meses

### 3.5 Conexión con fases WSLC
- **F9** (Transition Planning): define E6_target inicial
- **F13** (Health Monitoring): provee H_org_current periódicamente
- **F18** (Continuous Evolution): consume Convergence_Score para decidir ajustes de diseño o de trayectoria

---

## §4 INTEGRACIÓN Y FLUJO DE USO

### 4.1 Secuencia típica en un caso completo

1. **F1 (Context Assessment):**  
   Captura inputs de contexto → alimenta `health_score_calculator` (H_org inicial) y `context_decision_matrix`.

2. **F3 (Trajectory Selection):**  
   Ejecuta `context_decision_matrix` → obtiene `trajectory_selected` (Survival/Minimal/Avanzada).

3. **F4–F9 (Development):**  
   Diseña capacidades, flujos, info (TF1/TF2/TF3) → define E6_target para `convergence_tracker`.

4. **F10–F12 (Implementation):**  
   Despliega capacidades/flujos/info → actualiza `TF1_current`, `TF2_current`, `TF3_current` en `convergence_tracker`.

5. **F13 (Health Monitoring):**  
   Re-calcula H_org periódicamente → alimenta `convergence_tracker` con H_org_current.

6. **F18 (Continuous Evolution):**  
   Monitorea `Convergence_Score` → ajusta E6_target o trayectoria si hay drift.

### 4.2 Dependencias entre calculadoras

- `health_score_calculator` → `context_decision_matrix` (H_org como input crítico)
- `context_decision_matrix` → alcance de F4–F9 (trayectoria determina profundidad de diseño)
- `health_score_calculator` + F4–F9 → `convergence_tracker` (H_org_current + E6_current/target)

### 4.3 Restricciones genómicas (no modificables en P0)

**De `out/00_fundamentos_teoricos.md`:**
- H_org, η_org, ROI_Habilitacion son métricas canónicas → no cambiar definición de H_org.
- Invariantes I1, I3, I6 deben respetarse en fórmulas.

**De `out/20_tejidos.md`:**
- TF1/TF2/TF3 scores deben derivarse de % deployment de capacidades/flows/info, no de proxies arbitrarios.

**De `VOCABULARIO_CONTROLADO.yaml` y `DEPENDENCY_GRAPH.yaml`:**
- Usar IDs canónicos: `health_score`, `trajectory_selected`, `architectural_state`, etc.
- Respetar dependencias explícitas F1→F3, F3→F4–F9, F9→F10–F12, F13→F18.

---

## §5 PRÓXIMOS PASOS (POST P0-COMPLETE)

Una vez aprobada esta especificación P0:

1. **Implementación en `.xlsx`:**  
   Bajo un CAP dedicado (ej. CAP-22), actualizar los archivos existentes en `40_implementacion_metodologia/calculadoras/` siguiendo estas especificaciones.

2. **Validación en casos:**  
   Aplicar las calculadoras a `01_startup_50p_completo` y `06_gore_nuble_completo`, verificar coherencia con `context.yaml`, `trajectory.md` y health gates.

3. **Automatización:**  
   Evaluar si alguna de estas calculadoras puede implementarse como script Python (ej. `health_score_calculator.py`) para uso en pipelines de validación.

4. **Documentación de uso:**  
   Crear guías cortas (micro-playbooks) para facilitar que equipos externos usen estas calculadoras en talleres F1/F3/F13.

---

## §6 REFERENCIAS CANÓNICAS

- `out/00_fundamentos_teoricos.md` – Axiomas, primitivos, invariantes, teoremas, ecuación master V_org
- `out/20_tejidos.md` – TF1_Capacity, TF2_Flow, TF3_Information, scores por tejido
- `out/30_metodologia_orko.md` – Fases WSLC F1–F18, playbooks, trayectorias
- `30_metodologia_orko/13_metricas_validacion/02_health_gates.md` – Bandas G1–G4, umbrales críticos
- `30_metodologia_orko/09_trayectorias/03_decision_matrix.md` – Reglas de selección de trayectoria
- `20_tejidos/07_architectural_state_management.md` – Primitivo E6 (Architectural State)
- `40_implementacion_metodologia/dev_specs/VOCABULARIO_CONTROLADO.yaml` – IDs canónicos
- `40_implementacion_metodologia/dev_specs/DEPENDENCY_GRAPH.yaml` – Dependencias entre entidades

---

**Versión:** P0-COMPLETE (ORKO v1.0.0)  
**Estado:** Especificación textual aprobada para sq2, pendiente de implementación en `.xlsx` bajo CAP post-1.0.0  
**Autor:** sq2 (squad de calculadoras)  
**Fecha:** 2025-11-18
