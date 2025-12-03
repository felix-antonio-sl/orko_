# GAPS CRÍTICOS – PLAYBOOKS P01-P15

**Versión**: v1.0.0 FINAL  
**Fecha**: 2025-11-18 (Actualizado post-remediación)

---

## ✅ ESTADO REMEDIACIÓN

```yaml
GAPS_P0_RESUELTOS: 2/2 (100%)
  ✅ GAP-P1: P14-P15 formalizados con §0-§4 completo
  ✅ GAP-P4: §3 RACI agregado en 15/15 playbooks

GAPS_PENDIENTES_BACKLOG_v1.1: 5
  ⏸️ GAP-P2: Métricas no canónicas en triggers (P1)
  ⏸️ GAP-P7: Schemas outputs playbooks (P1)
  ⏸️ GAP-P8: Lifecycle playbooks (P1)
  ⏸️ GAP-P3: Trayectoria hints (P2)
  ⏸️ GAP-P5: Tolerancia fallas (P2)

Estado_Playbooks_Post_Remediación:
  §0-§4_Completo: P01-P15 (100%) ✅
  RACI_Formal: P01-P15 (100%) ✅
  Output_Schemas: 0/15 → Backlog v1.1
```

---

## RESUMEN EJECUTIVO ORIGINAL

```yaml
Total_Gaps: 7
Severidad:
  P0_CRÍTICA: 2 → RESUELTOS 2/2 ✅
  P1_ALTA: 3 → Backlog v1.1
  P2_MEDIA: 2 → Backlog v1.1

Playbooks_Afectados: 15/15 (100%)
Estado_Actual:
  §0+§1_Completos: P01-P13 (87%)
  §0+§1_Informales: P14-P15 (13%)
  RACI_Formal: 0/15 (0%)
  Output_Schemas: 0/15 (0%)
```

---

## ~~GAP-P1: §0/§1 INCONSISTENTE EN P14-P15~~ ✅ **RESUELTO**

### ✅ REMEDIACIÓN APLICADA

**P14 y P15 formalizados con estructura completa**:

- §0. FUNDAMENTO: vocabulos_referencia, métricas, health_gates, justificación
- §1. INTERFAZ: triggers YAML, inputs, outputs, dependencies, duration
- §2. EJECUCIÓN: pasos detallados, criterios éxito
- §3. RACI: responsible, accountable, consulted, informed
- §4. ACCEPTANCE: criterios validación

**Problema original**: P14-P15 usan formato MVO informal, no §0 FUNDAMENTO + §1 INTERFAZ

**Evidencia**:

```markdown
# P14 actual
## Estado: mvo
### Propósito
### Trigger (informal)

# P01-P13 (correcto)
## §0. FUNDAMENTO
**Layer 0:** A1, A5...
## §1. INTERFAZ
```yaml
triggers: ...
```

**Impacto**: 🔴 P0 - Rompe homogeneidad catálogo, auditoría VG4 no puede validar

**Remediación**:

- P14: Crear §0 formal (A1, A5, P5, I3, I5), §1 con triggers YAML
- P15: Crear §0 formal (A4, P4, I6, I8), §1 con triggers YAML
- Validar contra `playbook_schema.yaml`

---

## GAP-P2: MÉTRICAS NO CANÓNICAS EN TRIGGERS

**Problema**: P14-P15 usan métricas fuera de {H_org, eta_org, ROI_Habilitacion}

**Evidencia**:

- P14: `NPS drop > 10 pts` (NPS no es métrica canónica)
- P15: `hypergrowth flag = true` (flag no es métrica canónica)

**Impacto**: 🟠 P1 - Violación contrato métricas VOCABULARIO_CONTROLADO.yaml

**Remediación**: Reescribir triggers usando SOLO métricas canónicas:

```yaml
P14_correcto:
  trigger: "H_org < 60 AND context.customer_feedback degraded"

P15_correcto:
  trigger: "H_org < 60 AND context.growth_rate = hypergrowth AND handoff_ratio > 0.20"
```

---

## GAP-P3: ESTADO "draft/mvo/stable" SIN CRITERIOS

**Problema**: Campo `estado` sin definición de criterios de avance

**Evidencia**:

- P01: "mvo" (único Recovery)
- P02-P13: "draft"
- P14-P15: "mvo"
- NINGUNO: "stable"

**Impacto**: 🟡 P2 - Lifecycle unclear, no se sabe cuándo promover

**Remediación**: Crear `playbook_lifecycle_policy.md`:

```yaml
draft: §0+§1 completo, no usado en casos reales
mvo: §0+§1 validado, 1+ casos, métricas definidas, RACI asignado
stable: 3+ casos documentados, acceptance criteria medidos
```

---

## ~~GAP-P4: RACI AUSENTE O INFORMAL~~ ✅ **RESUELTO**

### ✅ REMEDIACIÓN APLICADA

**§3 RACI agregado en 15/15 playbooks (100%)**:

**Recovery (P01-P04)**:

- Estructura: responsible, accountable, consulted, informed
- Roles específicos: HealthOwner, Delivery_Lead, Captain, Sponsor

**Transformation (P05-P08)**:

- Roles: Transformation_Lead, Architect, Team_Leads
- Accountability clara en cambios estructurales

**Operational (P09-P15)**:

- Roles: FlowOwner, CapacityOwner, Data_Quality_Owner
- RACI por tipo operación

**Problema original**: P01-P13 SIN RACI, P14-P15 RACI informal (no YAML)

**Impacto**: 🔴 P0 - Violación I5_HAIC, accountability no trazable

**Remediación**: Agregar §3 RACI formal en TODOS los playbooks:

```yaml
## §3. RACI

```yaml
raci:
  responsible: ["Delivery_Lead", "PMO"]
  accountable: "Sponsor_L1_Human"  # Siempre humano (I5)
  consulted: ["Architect", "TF1_Lead"]
  informed: ["Board_Governance"]
```

```

**Prioridad**: P01, P02, P09-P15 (Recovery + Operational)

---

## GAP-P5: OUTPUTS SIN SCHEMA FORMAL

**Problema**: Outputs como strings sin schema validable

**Evidencia**:
```yaml
P01_outputs:
  - report: "P01_execution_report.md"  # ¿Qué contiene?
  - artifact: "h_org_recovery_plan.yaml"  # ¿Qué schema?
```

**Impacto**: 🟡 P2 - Artefactos no estandarizados

**Remediación**: Crear `contracts/schemas/playbook_outputs.yaml`:

```yaml
P01_execution_report:
  type: markdown
  sections: [executive_summary, h_org_before, h_org_after, actions_taken, metrics_impact]

h_org_recovery_plan:
  type: yaml
  fields: [playbook_id, h_org_baseline, h_org_target, actions[]]
```

---

## GAP-P6: DURACIONES SIN JUSTIFICACIÓN

**Problema**: `duracion_estimada` arbitrarias (P1D, P2D, P4W...)

**Impacto**: ⚪ BAJA - Orientativo, no crítico v1.0.0

**Remediación backlog v1.1**: Calibrar con casos reales en `40_implementacion_metodologia/ejemplos/`

---

## GAP-P7: CIRCULARIDAD PLAYBOOKS ↔ FASES

**Problema**: P09 escribe a F13 que lo triggerea (loop potencial)

**Evidencia**:

```yaml
P09_drift_detection:
  reads_from: [F13]
  writes_to: [F13, F16, F17]  # ← Escribe a quien lo triggerea
```

**Impacto**: 🟠 P1 - Riesgo loops infinitos sin convergencia

**Remediación**: Protocolo gestión circularidad:

```yaml
Regla_Convergencia:
  max_iterations: 3 por playbook por episodio (7 días)
  escalation: "Si 3 intentos fallan → P13 Political Alignment o Survival forzado"
```

---

## GAP-P8: PLAYBOOKS EN DIFERENTES ESTADOS

**Problema**: Inconsistencia estado dentro de familias

**Evidencia**:

- Recovery: P01 "mvo", P02-P04 "draft" (¿por qué diferencia?)
- Transformation: TODOS "draft"
- Operational: P09-P13 "draft", P14-P15 "mvo"

**Impacto**: 🟠 P1 - Gestión madurez inconsistente

**Remediación**: Auditar justificación estados + aplicar lifecycle_policy consistentemente

---

## PRIORIZACIÓN v1.0.0

**BLOQUEANTES (P0)**:

1. GAP-P1: Formalizar P14-P15 §0/§1
2. GAP-P4: RACI en P01-P15

**RECOMENDADOS (P1)**:
3. GAP-P2: Métricas canónicas
4. GAP-P7: Protocolo convergencia
5. GAP-P8: Lifecycle consistente

**BACKLOG v1.1 (P2)**:
6. GAP-P3: Criterios estado
7. GAP-P5: Output schemas
8. GAP-P6: Calibrar duraciones
