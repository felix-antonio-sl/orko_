
# P10_capacity_gap_resolution

**Tipo:** Playbook Transformation  
**ID:** P10  
**Trigger:** Gaps críticos de capacidad en F4/F10 que explican baja `H_org`/`eta_org` o bajo `ROI_Habilitacion`  
**Estimación Ejecución:** `P4W`

---

## §0. FUNDAMENTO

**Layer 0:** `A1`, `A3`, `A5`, `P1`, `P2`, `P5`, `I3`, `I6`  
**Layer 1:** `D1`, `D4`, `E6`  
**Layer 2:** `TF1`, `TF2`

**Justificación:** P10 se activa cuando la degradación de `H_org`/`eta_org` o el bajo `ROI_Habilitacion` se explican por gaps de capacidad (skills, FTE, plataformas) identificados en `F4`/`F10`. Su objetivo es diseñar y ejecutar un plan de cierre de gaps que restaure la eficiencia y prepare a la organización para escenarios G3/G4, en coordinación con P05, P06 y P11.

---

## §1. INTERFAZ

### Trigger Conditions

```yaml
triggers:
  - condition: "F4/F10 identifican gaps críticos de capacidad que explican baja H_org/eta_org o bajo ROI_Habilitacion"
    metric: "H_org"
    threshold: "por_debajo_objetivo_trayectoria"
    source: "F13.h_org_dashboard"
  - condition: "G3_H_org_Bueno_Eficiencia_Baja activo con evidencia de falta de capacidades"
    metric: "eta_org"
    threshold: "G3_activo"
    source: "02_health_gates.md"
```

### Outputs

```yaml
outputs:
  - report: "P10_capacity_gap_resolution_report.md"
    consumers: ["F4", "F10", "F13", "F17", "E4_governance"]
  - artifact: "capacity_gap_resolution_plan.yaml"
    consumers: ["F10", "F17", "P05", "P06"]
```


---

## §2. EJECUCIÓN
**Pasos**: 1) Identificar gap capacidad (TF1), 2) Evaluar opciones (hire/buy/build/borrow), 3) Ejecutar adquisición, 4) Onboard, 5) Validar gap cerrado

---

## §3. RACI
```yaml
raci:
  responsible: ["Role_CapacityOwner", "TF1_Lead", "HR"]
  accountable: "Role_Captain"
  consulted: ["Role_Architect", "Finance"]
  informed: ["Sponsor_L1_Human", "Affected_Teams"]
```
