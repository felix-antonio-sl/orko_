# trajectory – 03_enterprise_2000p_completo

## §0 CONTEXTO

- Contexto desde `context.yaml` (`enterprise_regulada_2000p_avanzada`): enterprise regulada ~2000 personas, `public_company`, jurisdicción `us`, alto riesgo regulatorio y operacional.
- Presión por cumplimiento estricto, estabilidad operacional y, al mismo tiempo, mejora de eficiencia y habilitación de tejidos.

## §1 TRAYECTORIA BASE (Avanzada)

- **Trayectoria base:** `Avanzada` (ver `09_trayectorias/02_avanzada_18_36_meses.md`).
- **Relación con `03_decision_matrix.md`:**
  - Entrada natural vía `DM4_G4_Ready_For_Avanzada` cuando se cumplen G4 y hay `budget_disponible >= '2M+'` para el programa de transformación.
  - `DM3_G3_Minimal_Optimización` sigue siendo relevante como sub-espacio dentro de Avanzada para ciclos de optimización sobre capacidades y flujos.
- **Health gates relevantes:** G1–G4, con G4 como condición de entrada principal; G1/G2 como señales de degradación que pueden requerir cambio de trayectoria.

## §2 DECISIONES F3/F17 (v0.1)

- **Selección inicial (`F3` – Trajectory Selection):**
  - El caso parte de la hipótesis de que la organización ya cumple condiciones cercanas a G4 (H_org y eficiencia en banda aceptable, capacidad de inversión alta).
  - `F3` documenta la decisión de adoptar `Avanzada` para desplegar `TF1`–`TF3` en 18–36 meses, siguiendo el patrón de `02_avanzada_18_36_meses.md`.

- **Adaptación (`F17`) y posibles cambios de trayectoria:**
  - **Operación normal bajo Avanzada:**
    - Con G4 activo y sin G1 recurrente, `F17` coordina ajustes dentro de `Avanzada` usando playbooks de optimización (`P10`, `P11`, `P03`) y de gobernanza (`P05`, `P06`, `P07`).
  - **Escenarios G3 en Avanzada (`DM3_G3_Minimal_Optimización` dentro de Avanzada):**
    - Si `H_org >= 70` pero `eta_org`/`ROI_Habilitacion` bajan, `F13` marca G3.
    - `F17` activa ciclos de optimización sobre capacidades y flujos, sin cambiar de trayectoria, apoyándose en P10/P11/P03 y en F15/F18.
  - **Episodios G2 (`G2_H_org_Bajo_Riesgo`):**
    - Se manejan inicialmente dentro de Avanzada con `P09` + P01 focalizado.
    - Si G2 persiste y señales de riesgo aumentan, `F17` puede proponer degradar el alcance de Avanzada (pausar escalamiento, reducir despliegues TF) manteniendo la trayectoria, o incluso evaluar regreso a `Minimal`.
  - **Episodios G1 (`G1_H_org_Critico`):**
    - Si `H_org < 60` de manera sostenida, `F13`/`F14` activan playbooks de crisis (P01, P02, P04, P15) y `F17` eleva a `Role_SteeringCommittee` la decisión de degradar trayectoria (`Avanzada → Minimal` o incluso `Survival`) siguiendo `DM1_G1_Survival`.
    - Una vez superada la crisis y con H_org estabilizado en G2/G3, `F17` puede proponer retorno a `Minimal` estable o, tras nuevo ciclo de éxito, evaluar reentrada a `Avanzada` vía G4.

