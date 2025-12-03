# trajectory – 04_fintech_500p_completo

## §0 CONTEXTO

- Contexto desde `context.yaml` (`fintech_regulada_500p_avanzada`): fintech regulada ~500 personas, etapa `series_d`, operación en `eu`/`uk`, fuerte supervisión financiera y multi‑jurisdicción.
- Riesgo regulatorio alto y necesidad de escalar productos financieros cumpliendo estrictamente KYC/AML y protección de datos.

## §1 TRAYECTORIA BASE (Avanzada)

- **Trayectoria base:** `Avanzada` (ver `09_trayectorias/02_avanzada_18_36_meses.md`).
- **Relación con `03_decision_matrix.md`:**
  - Se asume entrada a `Avanzada` cuando se cumple `DM4_G4_Ready_For_Avanzada` (G4 + presupuesto suficiente) y la organización decide consolidar tejidos y governance sofisticada.
  - `DM3_G3_Minimal_Optimización` también aplica como zona de optimización continua dentro de esta trayectoria.
- **Health gates relevantes:** todos los gates G1–G4, con énfasis en G3 (eficiencia/ROI) y G4 (readiness), y alta sensibilidad a G1/G2 en dominios de riesgo regulatorio.

## §2 DECISIONES F3/F17 (v0.1)

- **Selección inicial (`F3` – Trajectory Selection):**
  - `F3` documenta la decisión de usar `Avanzada` para orquestar un programa multianual de habilitación (TF1–TF3) que soporte crecimiento y compliance.
  - Se basan en lectura de G4 (o proximidad) y en la capacidad de sostener inversión 2M+ en transformación.

- **Adaptación (`F17`) con decision_matrix + G1–G4:**
  - **Bajo `G3_H_org_Bueno_Eficiencia_Baja`:**
    - Si `H_org >= 70` pero `eta_org` o `ROI_Habilitacion` son bajos, `F13` marca G3.
    - `F17` prioriza ciclos de optimización en dominios claves (riesgo, onboarding, pagos) usando P10/P11/P03 y reforzando governance y procesos críticos.
  - **Bajo `G2_H_org_Bajo_Riesgo`:**
    - Caídas de `H_org` a banda G2 (por incidentes menores o saturación de equipos) se abordan con P09 + P01 focalizado, manteniendo la trayectoria `Avanzada` mientras el riesgo sea contenido.
  - **Episodios `G1_H_org_Critico`:**
    - Si ocurren incidentes graves (p.ej. fallas regulatorias o de seguridad), `F13`/`F14` activan `Survival` según `DM1_G1_Survival` con P01, P02, P04, P15.
    - `F17` eleva a `Role_SteeringCommittee` la decisión de degradar temporalmente la trayectoria (`Avanzada → Minimal` o `Survival`) y documenta la transición de salida luego con `DM5_Survival_Minimal_Fallback`.
  - **Evaluación de permanencia en Avanzada (G4):**
    - Mientras G4 se mantenga, `Avanzada` sigue siendo la trayectoria por defecto; F15/F18 y F16/F17 vigilan convergencia, madurez y sostenibilidad.

