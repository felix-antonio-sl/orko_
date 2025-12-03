# 01_minimal_6_12_meses (draft)

## §0. Fundamento

- Fuente principal: `SPEC_ARQUITECTURA_DEFINITIVA.§1.5 Trayectorias_Core`.
- Trayectoria `Minimal` usa las 18 fases WSLC (`F1`–`F18`) en modo tool-agnostic (sin despliegue completo de `TF1`–`TF3`).
- Objetivo principal: aumentar `H_org` desde ~45 hasta ≥70 en un horizonte de 6–12 meses.
- Health gates relevantes: `G1_H_org_Critico`, `G2_H_org_Bajo_Riesgo`, `G3_H_org_Bueno_Eficiencia_Baja`, `G4_Ready_For_Avanzada`.
- Fases clave: `F1`, `F3`, `F4`, `F5`, `F6`, `F8`, `F9`, `F10`, `F11`, `F12`, `F13`, `F16`, `F17`, `F18`.
- Playbooks clave: `P01`, `P02`, `P03`, `P05`, `P09`, `P10`, `P11`, `P15`.

## §1. Caracterización de la trayectoria Minimal

- **Timeline:** 6–12 meses.
- **Budget:** ~`150–200K` (referencia desde SPEC, sujeto a ajuste por `Parametric`).
- **Scope:** `F1`–`F18` ejecutadas en modo tool-agnostic (sin requerir despliegue completo de `TF1`–`TF3`).
- **Delta esperado:** `H_org 45 → 70`.
- **Contexto típico:** startup/scaleup con presupuesto acotado, pero sin crisis extrema.

## §2. Relación con health gates (G1–G4)

Esta sección describe cómo `Minimal` interactúa con los health gates definidos en `13_metricas_validacion/02_health_gates.md`.

### §2.1 G1_H_org_Critico (`H_org < 60`)

- G1 indica una caída severa de `H_org` (nivel RED), normalmente incompatible con la ejecución estándar de `Minimal`.
- Cuando se activa G1 durante la trayectoria `Minimal`:
  - `F13` (`Role_HealthOwner`) declara G1.
  - `P01` y `P02` se activan bajo coordinación de `F14`.
  - `F17` abre un ciclo de adaptación que puede proponer un cambio temporal a trayectoria `Survival`.
  - `Role_Captain` y `Role_SteeringCommittee` deciden si se suspende o re-encuadra el plan `Minimal` hasta salir de G1.

**Regla práctica:** si G1 se mantiene por más de 1–2 ciclos de medición, `Minimal` pasa a modo **congelado** y la organización opera bajo los parámetros de `Survival` hasta estabilizar `H_org`.

### §2.2 G2_H_org_Bajo_Riesgo (`60 <= H_org < 70`)

- G2 indica zona de riesgo, pero no crisis crítica.
- En trayectoria `Minimal`:
  - `F13` detecta tendencia descendente de `H_org` hacia <70.
  - Se activa `P09` para análisis de drift y, si corresponde, `P01` en modo focalizado.
  - `F17` puede ajustar actividades dentro de `Minimal` (no cambio de trayectoria), priorizando acciones correctivas en dominios con mayor contribución a la caída.

**Intención:** `Minimal` debe ser capaz de absorber episodios G2 sin cambiar de trayectoria, usando `P09` + P01 parcial para corregir rumbo.

### §2.3 G3_H_org_Bueno_Eficiencia_Baja (`H_org >= 70` con `eta_org`/`ROI_Habilitacion` bajos)

- G3 representa la situación donde `H_org` ya alcanzó valores aceptables, pero `eta_org` y/o `ROI_Habilitacion` siguen por debajo de objetivos.
- En `Minimal`:
  - `F13` detecta la combinación `H_org` en verde + eficiencia/ROI bajos.
  - `P10` y `P11` se usan para abordar gaps de capacidades (`F4`) y flujos (`F5`).
  - `P03` puede emplearse cuando el problema es desalineamiento de OKR vs ejecución.
  - `F16` captura aprendizajes y `F17` ajusta la planificación dentro de `Minimal` (sin cambiar a `Avanzada`).

**Intención:** G3 es el espacio natural de optimización dentro de `Minimal` previo a considerar `Avanzada`.

### §2.4 G4_Ready_For_Avanzada (condición de upgrade)

- G4 se activa cuando se cumplen simultáneamente:
  - `H_org >= 70`.
  - `eta_org >= 0.70`.
  - `ROI_Habilitacion >= 1.2`.
- En trayectoria `Minimal`:
  - `F13` confirma las métricas.
  - `F17` (junto a `Role_TrajectoryOwner`) propone transición `Minimal → Avanzada`.
  - `Role_SteeringCommittee` (a través de `F3` re-evaluado) decide si se adopta trayectoria `Avanzada` con mayor inversión.
  - `P05`, `P06`, `P07` se planifican como parte del plan de entrada a `Avanzada`.

**Regla práctica:** `Minimal` no se considera "completa" mientras no se haya evaluado explícitamente G4 y tomado decisión documentada en `F3`/`F17` sobre permanecer en `Minimal` o cambiar a `Avanzada`.

---

## §3. Puntos abiertos v0.1

- Los umbrales numéricos de G1–G4 son v0.1 y pueden ajustarse en fases posteriores (VG2–VG4) con datos reales.
- Este documento no detalla aún el plan completo `F1`–`F18`; se centra en la interacción con health gates y decisiones de trayectoria. El detalle por fase se completará en coordinación con E2.
- La relación con `Parametric` (`05_budget_parametric.md`) se definirá después de validar el uso real de esta trayectoria en casos concretos.

