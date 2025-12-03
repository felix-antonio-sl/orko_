# GUÍA DE USO – CALCULADORAS ORKO v1.0.0

## §0 PROPÓSITO Y ALCANCE

### Objetivo
Esta guía documenta cómo usar las tres calculadoras críticas de ORKO para apoyar decisiones en las fases del Work System Life Cycle (WSLC). Las calculadoras operacionalizan métricas canónicas definidas en el genoma ORKO.

### Calculadoras cubiertas
1. **health_score_calculator.xlsx** – Calcula H_org (salud organizacional) y componentes A/P/D
2. **context_decision_matrix.xlsx** – Determina trayectoria óptima (Survival/Minimal/Avanzada)
3. **convergence_tracker.xlsx** – Mide convergencia E6_current → E6_target

### Audiencia
- Practicantes ORKO (consultores, facilitadores, arquitectos organizacionales)
- Equipos de transformación que requieren métricas objetivas
- Auditores que validan coherencia con invariantes I1-I8

### Principios de uso
- **Trazabilidad GENOMA→FENOTIPO:** Fórmulas derivan de axiomas, primitivos, invariantes y tejidos
- **No modificar genoma:** Calculadoras son fenotipo parametrizable
- **Uso secuencial:** F1→F3→F9→F13→F18 según flujo WSLC
- **Health gates obligatorios:** G1-G4 deben revisarse antes de avanzar

---

## §1 HEALTH_SCORE_CALCULATOR

### Propósito
Calcular **H_org** (salud organizacional) en tres dimensiones:
- **A_Score:** Coherencia con propósito/estrategia
- **P_Score:** Desempeño operativo
- **D_Score:** Capacidad de evolución

**Fundamento:** Métrica `H_org` de `out/00_fundamentos_teoricos.md` §4.3 (T6), ecuación `V_org = f(H_org, η_org, ROI_Habilitacion, t)`, invariantes I1/I3/I6, tejidos TF1/TF2/TF3.

### Inputs
**Desde F1:**
- `org_size`, `context_complexity`, `budget_available`, `strategic_clarity`

**Autoevaluación:**
- `current_state_maturity`, `TF1/TF2/TF3_deployed` (%)

**Cómo obtener:** Desde `context.yaml`, talleres F1, auditorías de tejidos.

### Parámetros ajustables
- `w_A/w_P/w_D`: Pesos A/P/D (default: 0.33, 0.33, 0.34)
- `TF1/TF2/TF3_weight`: Ponderación tejidos (default: 0.4, 0.35, 0.25)
- `maturity_floor`, `critical_threshold_G1`

### Outputs
- **H_org** (0-1), **A/P/D_Score** (0-1), **TF1/TF2/TF3_Score** (0-1)
- **Health_Band:** G1 (<0.35), G2 (0.35-0.55), G3 (0.55-0.75), G4 (≥0.75)
- **Recomendaciones:** Playbooks según banda

### Ejemplo caso 01_startup_50p
**Inputs:** org_size=50, complexity=3, budget=25M CLP, strategic_clarity=70%, maturity=2, TF1=40%, TF2=30%, TF3=20%

**Resultado:** H_org=0.43 → **G2 (bajo)** → Trayectoria Survival/Minimal, playbooks P01/P02

---

## §2 CONTEXT_DECISION_MATRIX

### Propósito
Determinar **trayectoria** (Survival/Minimal/Avanzada) desde:
- H_org, budget, complejidad/riesgo, madurez

**Fundamento:** Primitivo P6 (WSLC), invariante I6 (health gates), teorema T7 (trayectorias válidas).

### Inputs
- `H_org` (desde calculator), `budget_total`, `org_size`, `context_risk`, `strategic_horizon`, `current_maturity`

### Reglas DM1-DM5
**DM1:** Si H_org<0.35 O riesgo=5 → Survival  
**DM2:** Si budget/persona < 500 USD/año → Survival  
**DM3:** Si H_org<0.65 Y madurez≤3 → Minimal  
**DM4:** Si H_org≥0.65 Y budget/persona≥2000 Y madurez≥4 → Avanzada  
**DM5:** Otro caso → Minimal (default)

### Outputs
- `trajectory_selected`, `rationale`, `health_band_used`, `estimated_duration_months`, `key_constraints`
- **Playbooks:** Survival (P01/P02/P13), Minimal (P01-P06+P13), Avanzada (P01-P15)

### Ejemplo caso 01_startup_50p
**Input:** H_org=0.43, budget=50K USD, org_size=50, risk=3, maturity=2  
**Regla aplicada:** DM3 (H_org<0.65 Y madurez=2≤3)  
**Resultado:** **Minimal** (12-18 meses, playbooks P01-P06+P13)

---

## §3 CONVERGENCE_TRACKER

### Propósito
Medir **convergencia** E6_current → E6_target durante habilitación.

**Fundamento:** Primitivo P5 (Architectural State), invariante I3 (no-regresión), tejidos TF1/TF2/TF3.

### Inputs
**E6_CURRENT:** TF1/TF2/TF3_current_count, H_org_current, timestamp_current  
**E6_TARGET:** TF1/TF2/TF3_target_count, H_org_target, timestamp_target

**Cómo obtener:** E6_current desde auditoría F13, E6_target desde diseño F4-F9.

### Parámetros
- `weight_TF1/TF2/TF3`, `weight_H_org`, `convergence_threshold` (default: 0.85)

### Outputs
- **Convergence_Score** (0-1), **Convergence_Status** (Converged/In Progress/Lagging)
- **Deltas:** Delta_TF1/TF2/TF3/H_org
- **Proyecciones:** Estimated_Time_To_Target, Recommendations

### Ejemplo caso 06_gore_nuble (3 meses post-F12)
**E6_current:** TF1=12, TF2=8, TF3=15, H_org=0.58  
**E6_target:** TF1=18, TF2=14, TF3=25, H_org=0.75  
**Resultado:** Convergence_Score=0.65 → **In Progress** (6 meses restantes, priorizar TF2/TF3)

---

## §4 FLUJO INTEGRADO

### Secuencia típica
1. **F1** → captura inputs → **health_score_calculator** (H_org)
2. **F3** → **context_decision_matrix** (trayectoria)
3. **F4-F9** → diseña TF1/TF2/TF3 → define E6_target
4. **F9** → **convergence_tracker** (inicialización)
5. **F10-F12** → despliega → actualiza E6_current
6. **F13** → re-calcula H_org → actualiza **convergence_tracker**
7. **F17** (opcional) → re-evalúa trayectoria si drift
8. **F18** → monitorea convergencia → ajusta/itera

### Dependencias
- health_score → context_decision (H_org input crítico)
- context_decision → F4-F9 (trayectoria determina alcance)
- health_score + F4-F9 → convergence (H_org + E6 target/current)

---

## §5 REFERENCIAS AL GENOMA

### Vínculos FENOTIPO→GENOMA
**Métricas canónicas:**
- H_org → `out/00_fundamentos_teoricos.md` §4.3 (T6)
- η_org, ROI_Habilitacion → ecuación master V_org
- TF1/TF2/TF3 → `out/20_tejidos.md`

**Invariantes validados:**
- I1 (conservación propósito) → A_Score mide alignment
- I3 (no-regresión) → convergence_tracker valida
- I6 (health gates) → Health_Band G1-G4

**Fases WSLC:**
- F1 (Context) → inputs para health_score/context_decision
- F3 (Trajectory) → usa context_decision
- F9 (Transition) → define E6_target
- F13 (Health) → mide H_org periódicamente
- F18 (Evolution) → monitorea convergence

**Contratos kernel:**
- `VOCAB_CONTROLADO.yaml`: IDs canónicos (health_score, trajectory_selected, architectural_state)
- `DEPENDENCY_GRAPH.yaml`: F1→F3, F3→F4-F9, F9→F10-F12, F13→F18
- §0 FUNDAMENTO: F1/F3/F9/F13/F18 documentan relación con calculadoras

---

**Versión:** CAP-22 (ORKO v1.0.0 post-release)  
**Estado:** Guía de uso operativa  
**Autor:** sq4/E4 (coordinación/completion)  
**Fecha:** 2025-11-18  
**Refs:** `CALCULADORAS_P0_SPEC.md`, `P0_calculadoras_y_templates_map.md`
