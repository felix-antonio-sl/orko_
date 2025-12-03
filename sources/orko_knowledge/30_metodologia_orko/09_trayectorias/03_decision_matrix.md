# 03_decision_matrix (draft)

## §0. Fundamento

- Fuente principal: `SPEC_ARQUITECTURA_DEFINITIVA.§1.5 Trayectorias_Core` y `30_metodologia_orko/13_metricas_validacion/02_health_gates.md`.
- Trayectorias consideradas: `Survival`, `Minimal`, `Avanzada` (ver `09_trayectorias/04_survival_0_10K.md`, `01_minimal_6_12_meses.md`, `02_avanzada_18_36_meses.md`).
- Health gates usados como entradas: `G1_H_org_Critico`, `G2_H_org_Bajo_Riesgo`, `G3_H_org_Bueno_Eficiencia_Baja`, `G4_Ready_For_Avanzada`.
- Métricas canónicas: `H_org`, `eta_org`, `ROI_Habilitacion` (VOCAB layer_1.metricas).
- Fases de decisión: `F3` (Trajectory Selection), `F17` (Adaptation), `F13` (Health Monitoring).

Propósito de este archivo:

- Proveer una matriz mínima de decisión para elegir o ajustar trayectoria (`Survival`/`Minimal`/`Avanzada`) basada en health gates G1–G4 y contexto.
- Servir de referencia MVO para `F3`/`F17` y para el Capitán al evaluar cambios de ruta en SPRINT 1.

---

## §1. Variables de decisión (v0.1)

- `H_org`: nivel de health organizacional.
- `eta_org`: eficiencia global.
- `ROI_Habilitacion`: retorno de inversión en habilitación.
- `gate_activo`: uno o más de `G1`, `G2`, `G3`, `G4` según `02_health_gates.md`.
- `runway_meses`: meses de caja/viabilidad (variable de contexto, no métrica canónica formal).
- `budget_disponible`: orden de magnitud de presupuesto (`0–10K`, `150–200K`, `2M+` aprox.).
- `complejidad_contexto`: baja / media / alta (ej. regulación, multi‑unidad, hipergrowth).

> Nota: solo `H_org`, `eta_org`, `ROI_Habilitacion` se tratan como métricas canónicas; las demás variables son descriptores de contexto.

---

## §2. Matriz de decisión por escenarios

```yaml
decision_matrix:

  - scenario_id: "DM1_G1_Survival"
    descripcion: "Crisis crítica de health (G1 activo), requiere trayectoria Survival."
    condiciones:
      gate_activo: "G1_H_org_Critico"
      reglas_v0_1:
        - "H_org < 60 (ver 02_health_gates.G1)"
        - "runway_meses <= 3"  # contexto típico Survival
    trayectoria_recomendada: "Survival"
    fases_implicadas:
      - "F13"  # detección
      - "F14"  # incidencia
      - "F3"   # selección de trayectoria
      - "F17"  # adaptación
    playbooks_clave:
      - "P01"  # Low H_org Recovery
      - "P02"  # Handoff Reduction
      - "P04"  # Security Remediation (si aplica)
      - "P15"  # Adaptive Cadence
    notas:
      - "F3/F17 deben registrar cambio explícito hacia trayectoria Survival."
      - "Minimal/Avanzada se consideran congeladas mientras G1 esté activo."

  - scenario_id: "DM2_G2_Minimal_Defensiva"
    descripcion: "Zona de riesgo (G2) con runway suficiente; se mantiene Minimal con acciones correctivas."
    condiciones:
      gate_activo: "G2_H_org_Bajo_Riesgo"
      reglas_v0_1:
        - "60 <= H_org < 70"
        - "runway_meses > 3"
    trayectoria_recomendada: "Minimal"
    fases_implicadas:
      - "F13"
      - "F17"
    playbooks_clave:
      - "P09"  # Drift Detection Response
      - "P01"  # Low H_org Recovery (focalizado)
    notas:
      - "El objetivo es corregir rumbo dentro de Minimal sin cambiar a Survival."
      - "Si G2 persiste y runway cae, reconsiderar DM1 (Survival)."

  - scenario_id: "DM3_G3_Minimal_Optimización"
    descripcion: "H_org aceptable (>=70) pero eficiencia/ROI bajos (G3); se usa Minimal para optimizar capacidades y flujos."
    condiciones:
      gate_activo: "G3_H_org_Bueno_Eficiencia_Baja"
      reglas_v0_1:
        - "H_org >= 70"
        - "eta_org < 0.60 OR ROI_Habilitacion < 1.0"
    trayectoria_recomendada: "Minimal"
    fases_implicadas:
      - "F4"   # Capacity Mapping
      - "F5"   # Flow Design
      - "F13"  # Health Monitoring
      - "F16"  # Learning Loops
      - "F17"  # Adaptation
    playbooks_clave:
      - "P10"  # Capacity Gap Resolution
      - "P11"  # Flow Optimization
      - "P03"  # OKR Alignment (si el problema es desalineamiento)
    notas:
      - "Escenario natural antes de considerar transición a Avanzada."
      - "F17 debe dejar registro de decisiones sobre foco (capacidades vs flujos vs OKR)."

  - scenario_id: "DM4_G4_Ready_For_Avanzada"
    descripcion: "Organización lista para trayectoria Avanzada (G4 cumplido)."
    condiciones:
      gate_activo: "G4_Ready_For_Avanzada"
      reglas_v0_1:
        - "H_org >= 70"
        - "eta_org >= 0.70"
        - "ROI_Habilitacion >= 1.2"
        - "budget_disponible >= '2M+'"
    trayectoria_recomendada: "Avanzada"
    fases_implicadas:
      - "F3"   # Trajectory Selection
      - "F13"  # Health Monitoring
      - "F17"  # Adaptation
    playbooks_clave:
      - "P05"  # Bounded Autonomy M6
      - "P06"  # Pilot Transformation
      - "P07"  # Scale Transformation
    notas:
      - "Requiere decisión explícita de Role_SteeringCommittee (ver RACI)."
      - "Si G4 se cumple pero budget_disponible o complejidad_contexto no permiten Avanzada, permanecer en Minimal y revisar parámetros."

  - scenario_id: "DM5_Survival_Minimal_Fallback"
    descripcion: "Escenario de salida de Survival de vuelta a Minimal cuando se recupera H_org."
    condiciones:
      gate_activo: "G1_H_org_Critico"  # en remisión hacia G2/G3
      reglas_v0_1:
        - "H_org sube por encima de umbral crítico de G1 y se mantiene en banda G2/G3 por n ciclos"
    trayectoria_recomendada: "Minimal"
    fases_implicadas:
      - "F13"
      - "F17"
    playbooks_clave:
      - "P01"  # cierre de acciones de recuperación
      - "P09"  # análisis de drift residual
    notas:
      - "F17 documenta el cierre de Survival y la re-entrada a Minimal."

```

---

## §3. Uso en F3/F17 (guía rápida)

- `F3` puede usar esta matriz al inicio de un engagement para seleccionar trayectoria inicial según H_org, contexto (runway/budget/complejidad) y presencia de G1–G4.
- `F17` debe consultar la matriz cuando:
  - Se active o desactive un gate G1–G4.
  - Cambie de forma relevante el contexto (runway, budget, complejidad_contexto).
- La matriz no reemplaza juicio experto ni casos de uso; ofrece un contrato mínimo de decisión para SPRINT 1.

## §4. Puntos abiertos v0.1

- Los rangos numéricos y reglas (`reglas_v0_1`) son propuestas iniciales SPRINT 1; pueden ajustarse tras obtener datos reales y ejemplos de `40_implementacion_metodologia/ejemplos`.
- La integración con artefactos paramétricos (`05_budget_parametric.md`, `budget_parametric_allocator.xlsx`) se definirá en una iteración posterior.
- Este archivo no modifica el `DEPENDENCY_GRAPH`; cualquier futura extensión que introduzca nuevas dependencias deberá pasar por `dependency_closure_script.py`.

