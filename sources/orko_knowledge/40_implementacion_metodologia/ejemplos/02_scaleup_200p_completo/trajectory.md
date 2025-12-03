# trajectory – 02_scaleup_200p_completo

## §0 CONTEXTO

- Contexto desde `context.yaml` (`scaleup_saas_200p_minimal`): scaleup SaaS B2B ~200 personas, etapa `series_b`, operación en `eu`/`uk`, hipercrescimiento (`hypergrowth_flags.contratacion_rapida = true`, `hypergrowth_flags.expansion_geografica = true`).
- No se asume crisis G1 activa al inicio, pero sí presión fuerte por eficiencia y escalamiento.

## §1 TRAYECTORIA BASE (Minimal)

- **Trayectoria base:** `Minimal` (ver `09_trayectorias/01_minimal_6_12_meses.md`).
- **Relación con `03_decision_matrix.md`:**
  - Escenario dominante esperado: `DM3_G3_Minimal_Optimización` (H_org >= 70, pero `eta_org` y/o `ROI_Habilitacion` por debajo de objetivos), con foco en optimizar capacidades (`F4`) y flujos (`F5`).
  - Escenario defensivo: `DM2_G2_Minimal_Defensiva` cuando `H_org` cae a banda G2 (`60 <= H_org < 70`) pero runway y budget siguen siendo suficientes para sostener Minimal.
  - Escenario de upgrade futuro: `DM4_G4_Ready_For_Avanzada` cuando se cumpla G4 (`H_org`, `eta_org`, `ROI_Habilitacion` en verde) y `budget_disponible` sea compatible con `Avanzada` (2M+).
- **Health gates relevantes (ver `02_health_gates.md`):** `G1_H_org_Critico`, `G2_H_org_Bajo_Riesgo`, `G3_H_org_Bueno_Eficiencia_Baja`, `G4_Ready_For_Avanzada`.

## §2 DECISIONES F3/F17 (v0.1)

- **Selección inicial (`F3` – Trajectory Selection):**
  - `F3` documenta la elección de `Minimal` como trayectoria base para `scaleup_200p`, dado que el contexto requiere elevar/estabilizar `H_org` y mejorar eficiencia antes de comprometerse con `Avanzada`.
  - La decisión se basa en que el caso encaja mejor con escenarios `DM2`/`DM3` de la matriz (riesgo/optimización) que con `Survival` (`DM1`) o `Avanzada` inmediata (`DM4`).

- **Adaptación continua (`F17` – Adaptation) usando decision_matrix + G1–G4:**
  - **Cuando se activa `G2_H_org_Bajo_Riesgo` (`DM2_G2_Minimal_Defensiva`):**
    - `F13` detecta tendencia de `H_org` hacia <70.
    - `F17` ajusta la ejecución dentro de `Minimal` activando `P09` (Drift Detection) y, si corresponde, `P01` (Low H_org Recovery) en modo focalizado, sin cambiar de trayectoria.
  - **Cuando se activa `G3_H_org_Bueno_Eficiencia_Baja` (`DM3_G3_Minimal_Optimización`):**
    - `F13` confirma `H_org >= 70` con `eta_org`/`ROI_Habilitacion` bajos.
    - `F17` prioriza ciclos de optimización apoyados en `F4`/`F5` y playbooks `P10` (Capacity Gap Resolution), `P11` (Flow Optimization) y `P03` (OKR Alignment) según la causa raíz.
    - `F16` (`F16_learning_loops`) captura aprendizajes recurrentes para que el caso pueda escalar posteriormente.
  - **Cuando se cumple `G4_Ready_For_Avanzada` (`DM4_G4_Ready_For_Avanzada`):**
    - `F13` verifica umbrales de `H_org`, `eta_org` y `ROI_Habilitacion` y contexto de budget.
    - `F17`, junto a `Role_TrajectoryOwner` y `Role_SteeringCommittee`, propone y decide transición de `Minimal` a `Avanzada`, activando `P05`, `P06`, `P07` según `02_avanzada_18_36_meses.md`.
  - **Episodios G1 (`DM1_G1_Survival` y `DM5_Survival_Minimal_Fallback`):**
    - Si `H_org` cae en zona G1 de forma sostenida, `F13`/`F14` pueden forzar un paso temporal a trayectoria `Survival` (`04_survival_0_10K.md`), ejecutando `P01`, `P02`, `P04`, `P15` en modo crisis.
    - `F17` documenta luego la salida hacia `Minimal` usando las reglas de `DM5_Survival_Minimal_Fallback` cuando H_org se estabiliza en G2/G3.

