# 01_team_structure_raci (draft)

## §0. Fundamento

- Layer_0: invariantes `I3` (Trazabilidad), `I5` (HAIC), `I6` (Trajectory-Awareness).
- Layer_1: métricas `H_org`, `eta_org`, `ROI_Habilitacion` (ver `VOCABULARIO_CONTROLADO.layer_1.metricas`).
- Layer_3: fases `F1`, `F3`, `F4`, `F5`, `F8`, `F9`, `F13`, `F14`, `F16`, `F17`; playbooks `P01`–`P04`, `P05`–`P07`, `P09`, `P10`, `P11`, `P15`; trayectorias `Survival`, `Minimal`, `Avanzada`.
- Health gates: `G1_H_org_Critico`, `G2_H_org_Bajo_Riesgo`, `G3_H_org_Bueno_Eficiencia_Baja`, `G4_Ready_For_Avanzada` (ver `13_metricas_validacion/02_health_gates.md`).

Propósito de este archivo:

- Definir, a nivel MVO (v0.1), quién **detecta**, quién **decide**, quién **ejecuta** y quién **audita** las acciones asociadas a G1–G4.
- Servir de referencia para E2–E3–E4 al escribir fases, playbooks y trayectorias, manteniendo trazabilidad con `DEPENDENCY_GRAPH.yaml`.

> Nota: los nombres de roles son descriptores organizacionales; las referencias a fases, métricas, playbooks y trayectorias se hacen siempre por ID canónico.

---

## §1. Roles de governance (descriptivo)

- **Role_Captain**: Capitán del Squad ORKO; responsable de decisiones finales de cambio de trayectoria (`F3`, `F17`) y aprobación de activaciones mayores de playbooks críticos (`P01`–`P04`, `P05`, `P07`, `P15`).
- **Role_SteeringCommittee**: instancia directiva/board de la organización que valida cambios estratégicos de trayectoria (`Minimal` ↔ `Avanzada`) y compromisos de presupuesto/plazo.
- **Role_HealthOwner**: responsable operativo de `F13` (Health Monitoring); administra dashboards de `H_org`, `eta_org`, `ROI_Habilitacion` y declara la activación de G1–G4.
- **Role_IncidentLead**: responsable de `F14` (Incident Response); coordina ejecución de `P01`–`P04` cuando G1 o incidentes asociados lo requieran.
- **Role_PlaybooksLead**: responsable de coherencia y mantenimiento de `P01`–`P15`; trabaja con E3.
- **Role_TrajectoryOwner**: responsable de `F3` y `F17` (Trajectory Selection / Adaptation); propone y ejecuta cambios de trayectoria `Survival`/`Minimal`/`Avanzada` usando evidencia de G1–G4.
- **Role_TeamsExecutionLead**: liderazgo de equipos de entrega afectados por los playbooks (equipos que ejecutan pasos de `P01`–`P04`, `P05`–`P07`, `P09`–`P11`, `P15`).
- **Role_AuditVG4**: responsable de validación final VG4 (Completion + Release); verifica que decisiones y ejecuciones asociadas a G1–G4 cumplen criterios de I1–I8 y WSLC.

> Estos roles pueden mapearse 1:N a personas o equipos reales; el objetivo aquí es la claridad de accountability, no la estructura organizacional detallada.

---

## §2. RACI por health gate

Formato RACI:

- **R** = Responsible (ejecuta acciones principales).
- **A** = Accountable (decisión final / ownership de resultado).
- **C** = Consulted (input necesario antes de decidir/ejecutar).
- **I** = Informed (debe ser informado cuando el gate se active o cierre).

### §2.1 G1_H_org_Critico

Contexto (resumen de `02_health_gates.md`): `H_org < 60`, nivel RED, foco en `P01`, `P02`, `P15`, trayectoria recomendada `Survival`.

| Rol / Artefacto | RACI | Notas |
|-----------------|------|-------|
| Role_HealthOwner (F13) | R | Detecta `H_org < 60` y registra activación de `G1_H_org_Critico`. |
| Role_IncidentLead (F14) | R | Orquesta ejecución de `P01`, `P02` y coordinación con equipos de entrega. |
| Role_Captain | A | Decide entrada formal en modo `Survival` y prioriza activación de `P01`/`P02`/`P15`. |
| Role_SteeringCommittee | C | Consultado si el impacto de G1 afecta compromisos estratégicos o requiere re-priorización mayor. |
| Role_TrajectoryOwner (F3/F17) | C | Usa evidencia de G1 (y P01/P02) para proponer ajustes de trayectoria `Survival` ↔ `Minimal`. |
| Role_PlaybooksLead | C | Asegura que `P01`, `P02`, `P15` se ejecutan según triggers y límites definidos. |
| Role_TeamsExecutionLead | R | Ejecuta acciones concretas de los playbooks activados. |
| Role_AuditVG4 | I | Recibe registro de activación G1 y resultados de P01/P02/P15 para trazabilidad VG4. |

### §2.2 G2_H_org_Bajo_Riesgo

Contexto: `60 <= H_org < 70`, nivel YELLOW, foco en `P01` (parcial) y `P09`, trayectoria recomendada `Minimal`.

| Rol / Artefacto | RACI | Notas |
|-----------------|------|-------|
| Role_HealthOwner (F13) | R | Monitorea tendencia de `H_org` hacia <70 y declara G2 cuando corresponde. |
| Role_TrajectoryOwner (F3/F17) | R | Analiza junto a `Role_HealthOwner` si se requiere ajuste dentro de `Minimal` o pre-G1. |
| Role_Captain | A | Decide si se mantienen parámetros de `Minimal` o se prepara transición a modo más defensivo. |
| Role_PlaybooksLead | C | Evalúa y activa `P09` para análisis de drift y `P01` focalizado si corresponde. |
| Role_TeamsExecutionLead | R | Implementa acciones de contención/ajuste derivadas de `P09` y P01 parcial. |
| Role_SteeringCommittee | I | Informado cuando G2 se mantiene por períodos prolongados o requiere posible cambio de presupuesto/scope. |
| Role_AuditVG4 | I | Registra evidencia de cómo se manejaron episodios G2 en el ciclo WSLC. |

### §2.3 G3_H_org_Bueno_Eficiencia_Baja

Contexto: `H_org >= 70` pero `eta_org` o `ROI_Habilitacion` bajos; foco en `P10`, `P11`, `P03`, trayectoria `Minimal`.

| Rol / Artefacto | RACI | Notas |
|-----------------|------|-------|
| Role_HealthOwner (F13) | R | Detecta patrones donde `H_org` está en verde pero `eta_org`/`ROI_Habilitacion` por debajo de objetivos. |
| Role_TrajectoryOwner (F3/F17) | C | Analiza si la trayectoria `Minimal` sigue siendo adecuada o requiere ajustes finos. |
| Role_Captain | A | Priorización de focos G3 (capacidades vs flujos vs OKR) según contexto. |
| Role_PlaybooksLead | R | Activa `P10` (Capacity Gap Resolution), `P11` (Flow Optimization) y coordina con dueños de `F4`/`F5`. |
| Role_TeamsExecutionLead | R | Ejecuta cambios en capacidades y flujos definidos por los playbooks. |
| Role_SteeringCommittee | C | Puede ser consultado cuando los cambios G3 implican reconfiguración significativa de capacidades o flujos críticos. |
| Role_AuditVG4 | I | Valida que las mejoras en `eta_org`/`ROI_Habilitacion` estén documentadas y trazables a G3. |

### §2.4 G4_Ready_For_Avanzada

Contexto: `H_org >= 70`, `eta_org >= 0.70`, `ROI_Habilitacion >= 1.2`; foco en `P05`, `P06`, `P07`, trayectoria recomendada `Avanzada`.

| Rol / Artefacto | RACI | Notas |
|-----------------|------|-------|
| Role_HealthOwner (F13) | R | Confirma condiciones cuantitativas de G4. |
| Role_TrajectoryOwner (F3/F17) | R | Propone formalmente transición desde `Minimal` hacia `Avanzada` basada en evidencia de G4. |
| Role_SteeringCommittee | A | Aprueba cambio de trayectoria `Minimal → Avanzada` y movimientos de presupuesto/plazo asociados. |
| Role_Captain | R | Traduce la decisión del SteeringCommittee en mandato operativo al Squad ORKO. |
| Role_PlaybooksLead | R | Planifica despliegue de `P05` (bounded autonomy), `P06` (pilot) y `P07` (scale) asegurando consistencia con `F3`, `F7`, `F9`, `F11`. |
| Role_TeamsExecutionLead | R | Ejecuta pilotos y escalamiento definidos en los playbooks. |
| Role_AuditVG4 | C | Se asegura de que el cambio de trayectoria y resultados de `P05`–`P07` queden documentados para validación VG4. |

---

## §3. Puntos abiertos v0.1

- Este RACI es un borrador MVO para SPRINT 1; los nombres de roles son placeholders que deberán mapearse a roles reales en `12_roles_governance` y en la organización.
- La granularidad de RACI por playbook (más allá de la vista por gate) se definirá cuando P01–P07, P09–P11 y P15 tengan §0–§1 consolidados.
- Cualquier cambio en `VOCABULARIO_CONTROLADO` (nuevas métricas o entidades relevantes para governance) requerirá actualización de esta tabla para mantener I3/I6.

