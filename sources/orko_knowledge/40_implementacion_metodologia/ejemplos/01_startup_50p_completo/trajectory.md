# trajectory – 01_startup_50p_completo

## §0 CONTEXTO

- Contexto desde `context.yaml` (`startup_saas_50p_minimal`): startup SaaS B2B ~50 personas, etapa `series_a`, jurisdicción principal `us`, con `hypergrowth_flags.contratacion_rapida = true`.
- Presión alta por encontrar/afinar product–market fit, mejorar H_org y preparar una posible ronda posterior.

## §1 TRAYECTORIA BASE (Minimal)

- **Trayectoria base:** `Minimal` (ver `09_trayectorias/01_minimal_6_12_meses.md`).
- **Relación con `03_decision_matrix.md`:**
  - Escenario frecuente: combinación de `DM2_G2_Minimal_Defensiva` y `DM3_G3_Minimal_Optimización` según la evolución de `H_org` y eficiencia.
  - `DM2` se activa cuando `H_org` cae a banda G2 (`60 <= H_org < 70`) pero la startup mantiene runway razonable.
  - `DM3` se activa cuando `H_org >= 70` pero `eta_org` o `ROI_Habilitacion` son bajos (típico en startups con crecimiento rápido y sistemas inmaduros).
- **Health gates relevantes (ver `02_health_gates.md`):** G1–G4, con foco operativo en G2 y G3; G1 se trata como excepción grave y G4 como horizonte futuro.

## §2 DECISIONES F3/F17 (v0.1)

- **Selección inicial (`F3` – Trajectory Selection):**
  - `F3` documenta la elección de `Minimal` como trayectoria base dado que el contexto requiere elevar `H_org` y ordenar capacidades/flujo sin la inversión/inercia de `Avanzada`.
  - La decisión se justifica principalmente con la lectura de `DM2`/`DM3`: riesgo moderado y necesidad de optimización, no crisis Survival ni readiness para Avanzada.

- **Adaptación continua (`F17` – Adaptation) usando decision_matrix + G1–G4:**
  - **Si aparece `G2_H_org_Bajo_Riesgo` (`DM2_G2_Minimal_Defensiva`):**
    - `F13` detecta caída de `H_org` hacia banda 60–70.
    - `F17` ajusta el plan activando `P09` (Drift Detection) para entender fuentes de deterioro y `P01` (Low H_org Recovery) de forma focalizada (por dominio/equipo).
  - **Si se mantiene `G3_H_org_Bueno_Eficiencia_Baja` (`DM3_G3_Minimal_Optimización`):**
    - `F13` confirma `H_org >= 70` con problemas de eficiencia/ROI.
    - `F17` prioriza ciclos de `F4`/`F5` para capacidades/flujos, apoyados en `P10` (Capacity Gap Resolution), `P11` (Flow Optimization) y, cuando es desalineamiento de foco, `P03` (OKR Alignment).
  - **Si se activa `G1_H_org_Critico` (`DM1_G1_Survival`):**
    - En caso de crisis severa (runway muy corto, incidentes críticos), `F13`/`F14` pueden forzar paso temporal a trayectoria `Survival` (`04_survival_0_10K.md`) con `P01`, `P02`, `P04`, `P15`.
    - `F17` documenta luego la salida hacia `Minimal` usando el escenario `DM5_Survival_Minimal_Fallback` cuando H_org se estabiliza.
  - **Cuando se cumpla `G4_Ready_For_Avanzada` (`DM4_G4_Ready_For_Avanzada`):**
    - Aunque poco frecuente en este tamaño, si la startup alcanza G4 (H_org, eta_org y ROI_Habilitacion en verde y budget suficiente), `F17` propone junto al Capitán y `Role_SteeringCommittee` la transición hacia `Avanzada`, activando P05–P07.

