
# P11_flow_optimization

**Tipo:** Playbook Transformation  
**ID:** P11  
**Trigger:** Eficiencia de flujos degradada; cuellos de botella localizables en `E7_FlowExecution`  
**Estimación Ejecución:** `P3W`

---

## §0. FUNDAMENTO

**Layer 0:** `A1`, `A3`, `A5`, `P2`, `P5`, `I3`, `I6`  
**Layer 1:** `D2`, `D4`, `E7`  
**Layer 2:** `TF1`, `TF2`

**Justificación:** P11 se ocupa de optimizar flujos de trabajo cuando `eta_org` y/o `ROI_Habilitacion` se degradan por cuellos de botella en `E7_FlowExecution`. Complementa a P02 (reducción de handoffs) y P10 (gaps de capacidad), enfocándose en rediseñar flujos, load balancing y secuencias de trabajo en F5/F11 sin comprometer `H_org`.

---

## §1. INTERFAZ

### Trigger Conditions

```yaml
triggers:
  - condition: "Eficiencia de flujos (eta_org/ROI_Habilitacion) se degrada y cuellos de botella se localizan en E7_FlowExecution"
    metric: "eta_org"
    threshold: "por_debajo_target"
    source: "F13.eta_org_dashboard"
  - condition: "G3_H_org_Bueno_Eficiencia_Baja activo con evidencia de cuellos de botella de flujo"
    metric: "ROI_Habilitacion"
    threshold: "G3_activo"
    source: "02_health_gates.md"
```

### Outputs

```yaml
outputs:
  - report: "P11_flow_optimization_report.md"
    consumers: ["F5", "F11", "F13", "F16", "E4_governance"]
  - artifact: "flow_optimization_plan.yaml"
    consumers: ["F11", "F16", "P02", "P08"]
```


---

## §2. EJECUCIÓN
**Pasos**: 1) Analizar flujos TF2, 2) Identificar cuellos botella, 3) Rediseñar, 4) Implementar, 5) Medir eta_org improvement

---

## §3. RACI
```yaml
raci:
  responsible: ["Role_FlowOwner", "TF2_Lead"]
  accountable: "Role_Captain"
  consulted: ["Role_Architect", "Process_Owners"]
  informed: ["Sponsor_L1_Human", "All_Teams"]
```
