
# P09_drift_detection_response

**Tipo:** Playbook Recovery  
**ID:** P09  
**Trigger:** Drift relevante en `H_org`/`eta_org` detectado por F13 respecto a valores esperados por trayectoria  
**Estimación Ejecución:** `P3D`

---

## §0. FUNDAMENTO

**Layer 0:** `A1`, `A3`, `A5`, `P1`, `P2`, `P5`, `I3`, `I6`, `I8`  
**Layer 1:** `D2`, `D4`, `E6`, `E7`  
**Layer 2:** `TF1`, `TF2`

**Justificación:** P09 aborda situaciones donde el estado actual (`E6_ArchitecturalState`) se aleja del estado objetivo y las métricas `H_org`/`eta_org` se degradan respecto a lo esperado para la trayectoria activa (`Survival`/`Minimal`/`Avanzada`). Su rol es diagnosticar y contener el drift, generando hipótesis y acciones correctivas que luego se ejecutan vía P01, P02, P08, P10, P11 o P12 según el caso.

---

## §1. INTERFAZ

### Trigger Conditions

```yaml
triggers:
  - condition: "F13 detecta degradación sostenida de H_org/eta_org respecto a baseline esperado por trayectoria"
    metric: "H_org"
    threshold: "por_debajo_rango_esperado"
    source: "F13.h_org_dashboard"
  - condition: "Alertas de drift arquitectónico/operativo sobre E6/E7"
    metric: "eta_org"
    threshold: "tendencia_negativa"
    source: "F13.eta_org_dashboard"
  - condition: "Transición prolongada en G2/G3 sin mejora pese a playbooks activos"
    metric: "H_org"
    threshold: "G2/G3_persistente"
    source: "02_health_gates.md"
```

### Outputs

```yaml
outputs:
  - report: "P09_drift_analysis_report.md"
    consumers: ["F13", "F16", "F17", "E4_governance"]
  - artifact: "drift_correction_backlog.yaml"
    consumers: ["P01", "P02", "P08", "P10", "P11", "P12", "F16"]
  - metric_update: "H_org_eta_org_post_drift_response"
    consumers: ["F13", "G1", "G2", "G3"]
```


---

## §2. EJECUCIÓN
**Pasos**: 1) Detectar drift E6_current vs E6_target, 2) Clasificar severidad, 3) Plan corrección, 4) Ejecutar, 5) Validar convergencia

---

## §3. RACI
```yaml
raci:
  responsible: ["Role_Architect", "Role_HealthOwner"]
  accountable: "Role_Captain"
  consulted: ["TF1_Lead", "TF2_Lead", "TF3_Lead"]
  informed: ["Sponsor_L1_Human"]
```
