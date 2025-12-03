
# P05_bounded_autonomy_m6

**Tipo:** Playbook Transformation  
**ID:** P05  
**Trigger:** `eta_org` y/o `ROI_Habilitacion` subóptimos con `H_org` suficiente para aumentar autonomía (M6)  
**Estimación Ejecución:** `P4W`

---

## §0. FUNDAMENTO

**Layer 0:** `A1`, `A3`, `A5`, `P1`, `P2`, `P5`, `I3`, `I5`, `I6`  
**Layer 1:** `D1`, `D2`, `D4`, `E6`, `E7`  
**Layer 2:** `TF1`, `TF2`

**Justificación:** Cuando `H_org` es suficientemente alto pero `eta_org` y/o `ROI_Habilitacion` no alcanzan el potencial esperado, una causa recurrente es un modelo de autonomía/decisión pobremente diseñado. P05 define cómo pasar a modos de autonomía más avanzados (en especial `M6_BoundedAutonomy`) articulando capacidades (`P1`), flujos (`P2`) y propósito (`P5`) sin romper límites (`P4`) ni invariantes de trazabilidad (`I3`), accountability (`I5`) y adaptación (`I6`).

---

## §1. INTERFAZ

### Trigger Conditions

```yaml
triggers:
  - condition: "H_org >= 70 AND eta_org < target_minimal"
    metric: "eta_org"
    threshold: "target_minimal"
    source: "F13.eta_org_dashboard"
  - condition: "H_org >= 70 AND ROI_Habilitacion < 1.2"
    metric: "ROI_Habilitacion"
    threshold: 1.2
    source: "F13.roi_habilitacion"
  - condition: "Trayectoria Minimal lista para mayor autonomía (decisión F3/F17)"
    metric: "eta_org"
    threshold: "Minimal->Avanzada"
    source: "F3.trayectoria_decision"
```

### Outputs

```yaml
outputs:
  - report: "P05_autonomy_design_report.md"
    consumers: ["F3", "F7", "F11", "F17", "E4_governance"]
  - artifact: "bounded_autonomy_m6_playbook.yaml"
    consumers: ["F11", "F15", "trayectorias.Avanzada"]
  - metric_update: "eta_org_autonomy_expected_delta"
    consumers: ["F13", "F17"]
```

---

## §2. EJECUCIÓN
**Pasos**: 1) Diseñar modelo M6 autonomía, 2) Pilotear con 1-2 equipos, 3) Escalar, 4) Monitorear eta_org

---

## §3. RACI
```yaml
raci:
  responsible: ["Role_Architect", "Transformation_Lead"]
  accountable: "Role_Captain"
  consulted: ["Team_Leads", "TF1_Lead", "TF2_Lead"]
  informed: ["Sponsor_L1_Human", "All_Teams"]
```
