# MAPEO DOMINIOS (D1-D4) → FASES METODOLOGÍA

**Propósito:** Trazabilidad Layer 1 → Layer 3 (I3)  
**Tipo:** Mapeo Estructural  
**ID:** ORKO-L3-MAP-D-F

---

## §0. FUNDAMENTO

**Layer 0:** A1, A2, A3 | P1-P5 | I2, I3  
**Layer 1:** D1, D2, D3, D4 | C1-C5  
**Layer 2:** — (No aplica, mapeo conceptual)

**Justificación:** Este documento operacionaliza I3 (Trazabilidad) al proyectar dominios ortogonales D1-D4 (Layer 1 Arquitectura) sobre fases metodológicas F1-F18 (Layer 3 Metodología). Mapeo auditable preserva I2 (Ortogonalidad) demostrando que dominios cruzan fases independientemente. Es índice estructural, NO duplicación contenido.

**Definiciones:** `../00_fundamentos_teoricos/` | `../10_arquitectura_orko/`

---

## §1. FUNDAMENTO CONCEPTUAL

### Layer 1: Dominios Ortogonales

```yaml
D1_Arquitectura:
  Definición: "Diseño estructura sistemas trabajo (P1, P2, P3, P4, P5)"
  Alcance: Modelado, especificación, blueprints
  Output: Contratos C1-C5, entidades E6-E7

D2_Percepción:
  Definición: "Captura información entorno organizacional"
  Alcance: Sensing, assessment, monitoring, feedback
  Output: Métricas, context profiles, health scores

D3_Decisión:
  Definición: "Elección informada bajo constraints P4"
  Alcance: Trade-offs, priorización, trajectory selection
  Output: ADRs, roadmaps, playbook triggers

D4_Operación:
  Definición: "Ejecución transformaciones P2 (flows)"
  Alcance: Implementación, delivery, rituals
  Output: Artifacts, releases, ceremonies
```

### Layer 3: 18 Fases WSLC

Fases implementan metodología ejecutable derivada Layer 0→1→2.  
**Este documento traza D→F explícitamente (I3 compliance).**

---

## §2. MATRIZ MAPEO D×F

| Fase | D1_Arq | D2_Perc | D3_Dec | D4_Oper | Primitivos Primarios |
|------|--------|---------|--------|---------|----------------------|
| **F1** Context Assessment | ◐ | ●●● | ◐ | ○ | P1-P5 (scan) |
| **F2** Vision Definition | ◐ | ◐ | ●● | ○ | P5 (propósito) |
| **F3** Trajectory Selection | ○ | ◐ | ●●● | ○ | Decision |
| **F4** Capability Mapping | ●● | ◐ | ○ | ○ | P1 (capacidad) |
| **F5** Flow Design | ●● | ◐ | ○ | ○ | P2 (flujo) |
| **F6** Information Architecture | ●●● | ◐ | ○ | ○ | P3 (información) |
| **F7** Purpose Cascade | ● | ○ | ○ | ○ | P5 (OKR) |
| **F8** Limits Definition | ● | ◐ | ●● | ○ | P4 (límites) |
| **F9** Target State Design | ●●● | ○ | ●● | ○ | E6 (target) |
| **F10** Quick Wins | ○ | ○ | ● | ●● | Delivery |
| **F11** Fabric Deployment | ●● | ○ | ● | ●● | TF1-TF3 |
| **F12** State Transition | ○ | ● | ● | ●● | E6 evolve |
| **F13** Health Monitoring | ○ | ●●● | ○ | ●● | H_org sensing |
| **F14** Incident Response | ○ | ●● | ●● | ●●● | Remediation |
| **F15** Continuous Execution | ○ | ◐ | ● | ●●● | Xanpan |
| **F16** Learning Loops | ○ | ●● | ● | ● | Retrospectives |
| **F17** Adaptation | ◐ | ●● | ●●● | ○ | I6 trajectory |
| **F18** Convergence Check | ○ | ●● | ● | ○ | E6 validation |

**Leyenda:**  
- ●●● Primario (75-100% fase)  
- ●● Secundario (40-70% fase)  
- ● Terciario (15-35% fase)  
- ◐ Implícito (<15%)  
- ○ No aplica

---

## §3. DESCRIPCIÓN MAPEOS CRÍTICOS

### F1_Context_Assessment → D2_Percepción (Primario)

```yaml
Relación:
  F1 implementa D2 Percepción capturando 36 parámetros organizacionales
  
Método:
  - Workshops stakeholders
  - Interviews key personas
  - Metrics analysis (si disponible)
  - Document review
  
Output:
  - context_profile_36_params.yaml
  - h_org_estimation (baseline)
  - Compliance burden assessment
  
Primitivos:
  Sensing P1 (capacity inventory)
  Sensing P2 (flow analysis)
  Sensing P3, P4, P5 (limits, purpose)
```

### F3_Trajectory_Selection → D3_Decisión (Primario)

```yaml
Relación:
  F3 implementa D3 Decisión eligiendo Survival/Minimal/Avanzada
  
Método:
  - Decision matrix scoring
  - Compliance overlay application
  - Budget-timeline trade-offs
  
Accountability:
  Sponsor + Transformation Lead (I5 human-accountable)
  
Output:
  - trajectory_selected.yaml
  - Roadmap 6-36 months
  - Quick wins 0-6 months
  
Constraints_P4:
  Budget, regulatory, timeline, H_org baseline
```

### F6_Information_Architecture → D1_Arquitectura (Primario)

```yaml
Relación:
  F6 implementa D1 Arquitectura diseñando P3 Information structures
  
Método:
  - Data modeling (entities, relationships)
  - Lakehouse architecture (TF3)
  - MGDE compliance mapping (Chile gov)
  
Output:
  - information_blueprint.drawio
  - TF3_schema.yaml
  - MGDE_compliance_appendix.md
  
Contracts:
  C3 InformationAsset implementation
```

### F9_Target_State_Design → D1_Arquitectura (Primario) + D3_Decisión (Secundario)

```yaml
Relación:
  F9 implementa D1 diseñando E6 Target + D3 decisiones arquitectónicas
  
Método:
  - Blueprint completo system
  - Architecture Decision Records (ADRs)
  - Tech stack selection
  
Output:
  - E6_target_state_complete.yaml
  - ADRs_architecture/
  - Tech_stack_rationalization.md
  
Primitivos:
  Integra P1-P5 todos en visión coherente
```

### F13_Health_Monitoring → D2_Percepción (Primario) + D4_Operación (Secundario)

```yaml
Relación:
  F13 implementa D2 sensing continuo + D4 operación dashboard
  
Método:
  - H_org calculation automática
  - Drift detection (E6 current vs target)
  - Alert triggering (thresholds)
  
Output:
  - health_dashboard.html (live)
  - alerts_queue.json
  - Drift_report weekly
  
Triggers:
  H_org <70 → P01 playbook
  Handoff >30% → P02 playbook
  OKR misalignment → P03 playbook
```

### F14_Incident_Response → D4_Operación (Primario) + D3_Decisión (Secundario)

```yaml
Relación:
  F14 implementa D4 ejecución remediation + D3 playbook selection
  
Pattern_OODA:
  Observe: F13 detecta drop H_org (D2)
  Orient: F14 analiza causa root (D2+D3)
  Decide: F14 selecciona playbook (D3)
  Act: Ejecuta P01-P04 recovery (D4)
  
Output:
  - incident_log.yaml
  - Remediation actions ejecutadas
  - Post-mortem (F16 learning)
```

### F15_Continuous_Execution → D4_Operación (Primario)

```yaml
Relación:
  F15 implementa D4 operación continua vía Xanpan workflows
  
Método:
  - Sprint planning (2-week cycles)
  - Daily standups (15min)
  - Kanban board (WIP limits)
  - Retrospectives (F16)
  
Output:
  - Incremental delivery continuo
  - Velocity metrics
  - Burndown/burnup charts
```

### F17_Adaptation → D3_Decisión (Primario) + D2_Percepción (Secundario)

```yaml
Relación:
  F17 implementa D3 trajectory adjustments + D2 drift sensing
  
Trigger:
  I6 Trajectory-awareness detecta misalignment
  
Decisiones:
  - Cambio Minimal → Avanzada (H_org mejora)
  - Downgrade Avanzada → Minimal (crisis)
  - Pivot scope (budget cuts)
  
Output:
  - trajectory_adjustment_ADR.md
  - Roadmap updated
```

---

## §4. PATTERNS TRANS-DOMINIO

### Pattern 1: OODA Loop (Observe-Orient-Decide-Act)

```yaml
Secuencia:
  D2_Percepción (Observe) → 
  D2+D3 (Orient) → 
  D3_Decisión (Decide) → 
  D4_Operación (Act) → 
  D2_Feedback (Loop)

Ejemplo_F14_Incidents:
  1. Observe: F13 detecta H_org drop a 65 (D2)
  2. Orient: F14 analiza: handoff ratio 35%, capacity shortage (D2+D3)
  3. Decide: F14 selecciona P02 Handoff Reduction (D3)
  4. Act: Ejecuta P02 steps (consolidate teams, refactor) (D4)
  5. Loop: F13 monitorea H_org recovery → 72 (D2)

Invariante_Preservado: A3 (flujo red, no jerarquía estática)
```

### Pattern 2: Architecture Feedback Loop

```yaml
Secuencia:
  D1_Arquitectura (F9 design) →
  D4_Implementación (F11-F12 deploy) →
  D2_Percepción (F13 monitoring) →
  D3_Ajuste (F17 adaptation) →
  D1_Refinamiento (next iteration)

Ejemplo_TF3_Lakehouse:
  1. F9: Diseña TF3 Lakehouse (D1)
  2. F11: Deploy Delta Lake + Spark (D4)
  3. F13: Monitorea query performance (D2)
  4. F17: Detecta bottleneck en transformations (D3)
  5. F9 (next): Re-arquitectura partitioning strategy (D1)

Invariante_Preservado: I6 (mejora continua trajectory-aware)
```

### Pattern 3: Percepción-Decisión Coupling

```yaml
Principio:
  D3_Decisión SIEMPRE requiere D2_Percepción antecedente
  NO existe decisión sin sensing previo

Ejemplos:
  F3 Trajectory: D2 (F1 context) → D3 (selection)
  F8 Limits: D2 (compliance scan) → D3 (threshold definition)
  F17 Adaptation: D2 (drift detection) → D3 (trajectory change)

Anti-Pattern:
  Decisión sin percepción = Blind decision (violación A2, propósito sin fundamento)
```

---

## §5. VALIDACIÓN I3 TRAZABILIDAD

### Checklist Completitud

```yaml
Coverage_Dominios:
  D1_Arquitectura: [F4, F5, F6, F7, F8, F9, F11]
  D2_Percepción: [F1, F12, F13, F14, F16, F17, F18]
  D3_Decisión: [F2, F3, F8, F9, F14, F17]
  D4_Operación: [F10, F11, F12, F13, F14, F15]

Coverage_Fases:
  Todas F1-F18 cubiertas por al menos un dominio

Ortogonalidad_I2:
  Test: ¿Dominios cruzan fases independientemente?
  Resultado: Verificado
  Ejemplo: F14 usa D2+D3+D4 simultáneamente (OODA loop)

Bidireccionalidad:
  Layer 1 → Layer 3: D{N} navegable a F{M} vía matriz
  Layer 3 → Layer 1: F{M} §0.Fundamento traza D{N}
  
Validación_Completitud:
  - Todos los dominios mapeados a fases
  - Todas las fases mapeadas a dominios
  - Matriz auditable
  - Patterns documentados
  - Ortogonalidad I2 implica que NO todas las combinaciones son aplicables
  - Ejemplo: F7 Purpose Cascade NO requiere D4 Operación
```

---

## §6. NAVEGACIÓN

← **Anterior:** [00_introduccion_metodologia.md](00_introduccion_metodologia.md)  
→ **Siguiente:** [01_fases_initiation/README.md](01_fases_initiation/README.md)  
↑ **Índice:** [README.md](README.md)  
⊕ **Relacionados:**  
  - `../10_arquitectura_orko/01_contratos.md` (D1-D4 definiciones)
  - `../10_arquitectura_orko/02_diseño.md` (Patterns arquitectura)
  - `dependency_graph.yaml` (mapeo F↔F complementario)

---

## CHANGELOG

- [2025-11-13]: Creación inicial post gap I3 identificado
- [Descripción]: Mapeo explícito D→F para completar trazabilidad Layer 1→Layer 3
