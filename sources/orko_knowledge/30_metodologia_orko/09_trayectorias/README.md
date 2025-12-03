# 09 – Trayectorias y decision matrix

## §0. Propósito del bloque

- Este bloque describe cómo ORKO razona sobre **trayectorias de evolución organizacional** y cómo se seleccionan/ajustan en el tiempo.
- Proporciona el contrato conceptual que conecta contexto (`context.yaml`), health gates (G1–G4), playbooks P01–P15 y decisiones de F3/F17.

## §1. Componentes principales

- `01_minimal_6_12_meses.md`
  - Describe la trayectoria **Minimal**: foco en estabilizar y mejorar la organización en un horizonte de 6–12 meses, con cambios acotados y bajo riesgo.

- `02_avanzada_18_36_meses.md`
  - Describe la trayectoria **Avanzada**: cambios más profundos en un horizonte de 18–36 meses, con mayor inversión y complejidad.

- `04_survival_0_10K.md`
  - Describe la trayectoria **Survival**: escenarios de alta presión/limitaciones extremas, donde el objetivo es preservar continuidad mínima.

- `03_decision_matrix.md`
  - Documento central que define cómo se elige una trayectoria en F3 (`Trajectory Selection`) y cómo se revisa en F17 (`Adaptation`).
  - Usa señales de G1–G4 (estado de `H_org`, `eta_org`, `ROI_Habilitacion`) y características de contexto para recomendar combinaciones de trayectorias/playbooks.

- `05_budget_parametric.md` y `06_transition_minimal_avanzada.md`
  - Documentos de apoyo para modelar presupuesto paramétrico y transiciones entre trayectorias (por ejemplo, pasar de Minimal a Avanzada).

## §2. Relación con fases WSLC y casos

- **F3 – Trajectory Selection:**
  - Toma como input el contexto (`context.yaml`), la decisión de negocio y las señales de health gates.
  - Usa `03_decision_matrix.md` para seleccionar una trayectoria base (Survival/Minimal/Avanzada).

- **F17 – Adaptation:**
  - Revisa periódicamente si la trayectoria sigue siendo adecuada.
  - Usa health gates, outputs de F16 (`F16_learning_loops.md`) y resultados de playbooks para decidir si mantener, ajustar o cambiar de trayectoria.

- **Casos (`40_implementacion_metodologia/ejemplos/*_completo`):**
  - Cada `trajectory.md` por caso explica qué trayectoria se eligió y por qué, referenciando explícitamente `03_decision_matrix.md` y G1–G4.
  - `artefactos.md` muestra qué fases y playbooks se activan según la trayectoria elegida.

## §3. Relación con playbooks y health gates

- Las trayectorias no son playbooks; definen **rutas de evolución** sobre las que se encadenan playbooks P01–P15.
- `03_decision_matrix.md` codifica mapeos de alto nivel del tipo:
  - Survival → mayor peso en playbooks Recovery (P01–P04) y Operational de contención (P09, P12).
  - Minimal → combinación balanceada de Recovery/Operational/Transformation según contexto.
  - Avanzada → uso intensivo de Transformation (P05–P08) una vez que health gates lo permiten.
- `30_metodologia_orko/13_metricas_validacion/02_health_gates.md` define los estados G1–G4 que alimentan estas decisiones.

## §4. Lineamientos para ORKO v1.0.0

- Tratar las trayectorias Survival/Minimal/Avanzada y la `decision_matrix` como **contratos estables** de esta versión.
- No introducir nuevas trayectorias ni modificar la semántica de las existentes sin un nuevo CAP que actualice VOCAB, DEP_GRAPH y casos.
- Usar este README como mapa para navegar el bloque; los detalles normativos están en los archivos individuales.
