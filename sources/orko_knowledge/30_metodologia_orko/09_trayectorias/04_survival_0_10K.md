# 04_survival_0_10K (draft)

## §0. Fundamento

- Fuente principal: `SPEC_ARQUITECTURA_DEFINITIVA.§1.5 Trayectorias_Core`.
- Trayectoria `Survival` está diseñada para contextos de crisis extrema, con presupuesto `0–10K` y horizonte corto (`8–12 semanas`).
- Scope mínimo: `F1`–`F3` + `F10` en modo micro, centrado en estabilizar `H_org` y recuperar viabilidad básica.
- Health gate principal: `G1_H_org_Critico` (aunque G2 también puede aparecer como antesala de entrada/salida).
- Playbooks clave: `P01`, `P02`, `P04`, `P15`.

## §1. Caracterización de la trayectoria Survival

- **Timeline:** 8–12 semanas (en sprints cortos).
- **Budget:** `0–10K` (mínimo posible).
- **Scope:**
  - `F1` (Context Assessment) para entender la crisis.
  - `F3` (Trajectory Selection) en modo de emergencia.
  - `F10` (Quick Wins) en versión micro para generar alivio rápido.
  - Uso intensivo de playbooks de recuperación (`P01`–`P04`) y ajuste de cadencias (`P15`).
- **Contexto típico:** runway <3 meses, incidentes severos, pivote urgente.

## §2. Relación con health gates (G1–G4)

### §2.1 Entrada natural a Survival: G1_H_org_Critico

- `Survival` es la trayectoria natural cuando se activa `G1_H_org_Critico`:
  - `F13` detecta `H_org < 60` de forma significativa.
  - `F14` y `P01`/`P02`/`P04` abordan incidentes y problemas de cumplimiento/seguridad.
  - `P15` ajusta cadencias para poder operar en modo crisis.
  - `F3` y `F17` documentan el cambio de trayectoria desde `Minimal` o `Avanzada` hacia `Survival`.

### §2.2 Operar bajo G1 (modo Survival)

- Mientras G1 se mantenga activo:
  - El foco es evitar colapso de `H_org` y restablecer condiciones mínimas de operación.
  - Se priorizan quick wins (`F10` micro) y mitigación de riesgos (`P04`).
  - Se difieren iniciativas de mayor alcance propias de `Minimal`/`Avanzada`.

### §2.3 Salida de Survival hacia Minimal (G2/G3)

- `Survival` NO es una trayectoria permanente; su objetivo es devolver a la organización a condiciones donde `Minimal` sea viable.
- Señales de salida:
  - `H_org` se estabiliza por sobre el umbral crítico de G1 y entra en banda G2/G3.
  - `F13` deja de reportar eventos G1 recurrentes.
- Proceso de salida:
  - `F17` propone transición de `Survival` a `Minimal`.
  - `Role_Captain` aprueba el cambio de trayectoria, documentado en `F3`.
  - A partir de ahí, los health gates G2/G3/G4 se evalúan bajo las reglas de la trayectoria `Minimal`.

### §2.4 Relación con G4

- G4 no aplica directamente en `Survival` (por definición, `H_org` está por debajo de los umbrales de entrada a `Avanzada`).
- El camino típico es:
  - `Survival` → (salida mediante G2/G3) → `Minimal` → (cuando G4 se cumple) → `Avanzada`.

---

## §3. Puntos abiertos v0.1

- Este borrador no detalla aún el set completo de quick wins (`F10` micro); se espera coordinación con la fase `F10_quick_wins.md`.
- La relación detallada con `P04_security_remediation` se completará una vez que P04 tenga §0–§1 consolidados.
- Los criterios exactos de "salida" de `Survival` (número de sprints, umbrales finos de `H_org`) se ajustarán con experiencia en casos reales.

