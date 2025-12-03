# P14 – Client Expectation Management

## §0. FUNDAMENTO

```yaml
playbook_id: P14
nombre_canonico: "Client Expectation Management"
familia: "Operational"
estado: "stable"

vocabulos_referencia:
  axiomas:
    - A1_Organizacion
    - A5_Cambio
  primitivos:
    - P4_Limite
    - P5_Proposito
  invariantes:
    - I3_Trazabilidad
    - I5_HAIC
    - I6_Trajectory_Awareness
  dominios:
    - D2_Percepcion
    - D3_Decision

metricas_canonicas:
  - H_org (componente H4_Percepcion)
  - custom: stakeholder_satisfaction

health_gates_asociados:
  - G2_H_org_Bajo_Riesgo
  - G3_H_org_Moderado

justificacion:
  "Mitigar brechas entre expectativas stakeholders y entregables que degradan H4_Percepcion (componente H_org)"
```

---

## §1. INTERFAZ

```yaml
triggers:
  - condition: "H4_Percepcion < 60 AND customer_feedback = degraded"
    health_gate: "G2"
    description: "Drop en satisfacción cliente impacta H_org"
  
  - condition: "stakeholder_escalation AND expectation_mismatch = true"
    source: "F13 o manual"
    description: "Escalamiento stakeholder requiere gestión expectativas"

inputs:
  - F13.h_org_current (componente H4_Percepcion)
  - F13.stakeholder_feedback
  - customer_satisfaction_metrics
  - case_instances.yaml

outputs:
  - client_expectation_action_plan.md
  - communication_pack.zip
  - postmortem_client_expectation.md
  - h4_percepcion_recovery_report.yaml

dependencies:
  reads_from: ["F13"]
  writes_to: ["F16"]
  may_trigger: ["P13"]

duracion_estimada: "P3D - P7D"
```

---

## §2. EJECUCIÓN

**Pasos**:
1. Confirmar gap con datos F13 + customer_feedback
2. Preparar runbook comunicación (interno/externo)
3. Alineamiento SAC/PO/Architecture
4. Priorizar acciones correctivas (P10/P11 técnico, P13 político)
5. Ejecutar plan + monitorear H4_Percepcion recovery

---

## §3. RACI

```yaml
raci:
  responsible: ["Product_Owner", "Delivery_Lead"]
  accountable: "Sponsor_L1_Human"
  consulted: ["Role_Architect", "TF3_Lead", "Communications"]
  informed: ["Board_Governance"]
```

---

## §4. ACCEPTANCE

- Comunicación confirmada por stakeholder clave
- Plan acciones priorizado y estimado
- H4_Percepcion mejora 30-90 días
