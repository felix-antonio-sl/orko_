# 02_avanzada_18_36_meses (draft)

## §0. Fundamento

- Fuente principal: `SPEC_ARQUITECTURA_DEFINITIVA.§1.5 Trayectorias_Core`.
- Trayectoria `Avanzada` asume ejecución completa de `F1`–`F18` y despliegue de `TF1`, `TF2`, `TF3`.
- Objetivo principal: aumentar `H_org` desde ~70 hasta ≥85 en un horizonte de 18–36 meses.
- Health gates relevantes: `G1_H_org_Critico`, `G2_H_org_Bajo_Riesgo`, `G3_H_org_Bueno_Eficiencia_Baja`, `G4_Ready_For_Avanzada` (G4 como condición de entrada principal).
- Fases clave adicionales respecto a `Minimal`: `F11` (Fabric Deployment), `F12` (State Transition), `F15` (Continuous Execution), `F18` (Convergence Check).
- Playbooks clave: `P05`, `P06`, `P07`, además de los playbooks de recuperación/optimización (`P01`–`P04`, `P09`–`P11`, `P15`).

## §1. Caracterización de la trayectoria Avanzada

- **Timeline:** 18–36 meses.
- **Budget:** `2M+` (según SPEC, típico enterprise/regulado/hipergrowth).
- **Scope:** `F1`–`F18` + despliegue completo de `TF1`, `TF2`, `TF3`.
- **Delta esperado:** `H_org 70 → 85`.
- **Contexto típico:** organizaciones enterprise, reguladas o en hipergrowth con alta complejidad y capacidad de inversión.

## §2. Relación con health gates (G1–G4)

### §2.1 Entrada a Avanzada vía G4

- Condición de entrada principal:
  - `H_org >= 70`, `eta_org >= 0.70`, `ROI_Habilitacion >= 1.2` (G4 en `02_health_gates.md`).
- Proceso típico:
  - `F13` (`Role_HealthOwner`) confirma que G4 está activo.
  - `F17` prepara propuesta de cambio de trayectoria de `Minimal` a `Avanzada`.
  - `Role_SteeringCommittee` aprueba la transición (accountable del cambio de trayectoria).
  - `Role_Captain` traduce la decisión a mandato operativo para el Squad (activación formal de `Avanzada`).
  - `P05`, `P06`, `P07` definen el camino operativo: bounded autonomy, piloto, escalamiento.

### §2.2 Gestión de G1 y G2 dentro de Avanzada

- Aunque `Avanzada` parte desde un `H_org` ya sólido, pueden aparecer episodios G1/G2:
  - **G2_H_org_Bajo_Riesgo:** se maneja principalmente dentro de `Avanzada` mediante `P09` + P01 focalizado; `F17` ajusta plan dentro de la misma trayectoria, sin necesidad inmediata de degradar a `Minimal`.
  - **G1_H_org_Critico:** si `H_org` cae bajo 60 de forma sostenida, `F13` y `F14` activan `P01`, `P02`, `P15` y `F17` debe evaluar seriamente una degradación de trayectoria (`Avanzada → Minimal` o incluso `Survival`) junto a `Role_SteeringCommittee`.

**Criterio:** G1 en contexto `Avanzada` es una señal fuerte de que la organización no está lista para sostener el nivel de complejidad/ambición actual; la decisión de degradar se toma a nivel de governance (Steering + Capitán + TrajectoryOwner).

### §2.3 G3 dentro de Avanzada (optimización continua)

- G3 (`H_org >= 70` con `eta_org`/`ROI_Habilitacion` bajos) sigue siendo relevante en `Avanzada`:
  - `P10`, `P11`, `P03` operan sobre un entorno donde `TF1`, `TF2`, `TF3` ya están desplegados.
  - `F15` y `F18` contribuyen a monitorear convergencia y ejecución continua.
  - `F16`–`F17` documentan ajustes en patrones de delegación (`P05`) y escalamiento (`P07`).

**Intención:** en `Avanzada`, G3 es una señal de optimización de segunda capa (no solo procesos y capacidades básicas, sino también tejidos y gobernanza compleja).

### §2.4 Permanencia o salida de Avanzada

- Permanencia:
  - Mientras se mantenga `H_org >= 70` y no existan episodios G1 prolongados, `Avanzada` se considera trayectoria activa por defecto.
- Salida o degradación:
  - Episodios G1 recurrentes o imposibilidad de sostener `eta_org`/`ROI_Habilitacion` pueden gatillar, vía `F17` + `Role_SteeringCommittee`, un cambio de trayectoria de vuelta a `Minimal`.

---

## §3. Puntos abiertos v0.1

- Los parámetros de duración (18–36 meses) y presupuesto (`2M+`) son referencias desde SPEC; pueden ajustarse según `Parametric` (`05_budget_parametric.md`).
- Este borrador no detalla aún el plan detallado por fase; se centra en la lógica de entrada/salida y relación con G1–G4.
- La interacción detallada con `TF1`, `TF2`, `TF3` se documentará en conjunto con `F11` y `40_implementacion_metodologia`.

