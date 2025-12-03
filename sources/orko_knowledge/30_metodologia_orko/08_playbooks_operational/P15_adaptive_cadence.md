# P15 – Adaptive Cadence

## §0. FUNDAMENTO

```yaml
playbook_id: P15
nombre_canonico: "Adaptive Cadence"
familia: "Operational"
estado: "stable"

vocabulos_referencia:
  axiomas:
    - A4_Contexto
    - A5_Cambio
  primitivos:
    - P2_Flujo
    - P4_Limite
  invariantes:
    - I6_Trajectory_Awareness
    - I8_Adaptacion_Contextual
  dominios:
    - D4_Operacion

metricas_canonicas:
  - H_org
  - eta_org
  - custom: handoff_ratio, WIP_level

health_gates_asociados:
  - G1_H_org_Critico
  - G2_H_org_Bajo_Riesgo

justificacion:
  "Ajustar cadencias operativas ante shocks contextuales (hypergrowth, crisis) para mantener continuidad sin colapsar eta_org"
```

---

## §1. INTERFAZ

```yaml
triggers:
  - condition: "context.growth_rate = hypergrowth AND handoff_ratio > 0.20"
    health_gate: "G2"
    description: "Crecimiento rápido genera handoffs excesivos"
  
  - condition: "H_org < 60 AND context.crisis_mode = true"
    health_gate: "G1"
    description: "Crisis requiere reducción WIP inmediata"
  
  - condition: "eta_org < 0.60 AND throughput_dropping = true"
    source: "F13"
    description: "Eficiencia colapsando requiere ajuste cadencia"

inputs:
  - F13.h_org_current
  - F13.eta_org
  - F15.execution_log
  - context.growth_rate
  - context.crisis_flag

outputs:
  - adaptive_cadence_policy.md
  - cadence_rebalancing_plan.xlsx
  - post_adaptation_review.md
  - wip_reduction_report.yaml

dependencies:
  reads_from: ["F13", "F15"]
  writes_to: ["F15", "F17"]
  may_trigger: ["P10", "P14"]

duracion_estimada: "P2W - P8W"
```

---

## §2. EJECUCIÓN

**Pasos**:
1. **Immediate cadence freeze**: Reducir WIP 40% en 2 semanas
2. **Triage**: Identificar backlogs críticos continuidad
3. **Capacity rebalancing**: Invocar P10 si gaps capacidad
4. **Communication plan**: P14 si impacto clientes
5. **Transition roadmap**: 4-8 semanas a steady cadence

**Modos adaptación**:
- **Crisis mode**: Sprint 1→2 semanas, deploy diario→semanal
- **Hypergrowth mode**: Aumentar parallelismo pero con handoff control

---

## §3. RACI

```yaml
raci:
  responsible: ["Delivery_Lead", "PMO"]
  accountable: "Sponsor_L1_Human"
  consulted: ["TF1_Lead", "TF2_Lead", "HR"]
  informed: ["Board_Governance"]
```

---

## §4. ACCEPTANCE

- WIP reducido >40% en fase inicial (2 semanas)
- DORA metrics (throughput, lead time) recuperan tendencia 8 semanas
- eta_org mejora >0.10 puntos post-adaptación
