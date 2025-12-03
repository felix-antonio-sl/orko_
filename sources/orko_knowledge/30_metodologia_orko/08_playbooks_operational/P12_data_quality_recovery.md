
# P12_data_quality_recovery

**Tipo:** Playbook Recovery  
**ID:** P12  
**Trigger:** Problemas de calidad de datos en TF3/F6 que afectan `H_org`/`eta_org`/`ROI_Habilitacion`  
**Estimación Ejecución:** `P2W`

---

## §0. FUNDAMENTO

**Layer 0:** `A1`, `A3`, `A5`, `P3`, `P5`, `I3`, `I6`, `I8`  
**Layer 1:** `D2`, `D4`, `E6`, `C3`  
**Layer 2:** `TF3`

**Justificación:** Sin datos confiables, ningún playbook puede operar correctamente. P12 se activa cuando problemas en activos `C3_Informacion` (completitud, consistencia, frescura) degradan `H_org`, `eta_org` o `ROI_Habilitacion`. Su objetivo es restaurar la calidad de datos que soporta decisiones en F6/F11/F13 y evitar que otros playbooks tomen decisiones basadas en señales corruptas.

---

## §1. INTERFAZ

### Trigger Conditions

```yaml
triggers:
  - condition: "F6/F11 reportan problemas de calidad de datos que impactan métricas de resultado"
    metric: "H_org"
    threshold: "impacto_en_H_org"
    source: "F13.h_org_dashboard"
  - condition: "Indicadores de eta_org/ROI_Habilitacion se vuelven poco confiables por issues de datos en TF3"
    metric: "eta_org"
    threshold: "inconsistencia_datos"
    source: "F13.eta_org_dashboard"
```

### Outputs

```yaml
outputs:
  - report: "P12_data_quality_recovery_report.md"
    consumers: ["F6", "F11", "F13", "F16", "E4_governance"]
  - artifact: "data_quality_recovery_plan.yaml"
    consumers: ["F6", "F11", "P09", "P10"]
```


---

## §2. EJECUCIÓN
**Pasos**: 1) Auditar calidad datos TF3, 2) Priorizar gaps críticos, 3) Plan remediación, 4) Ejecutar, 5) Validar quality improvement

---

## §3. RACI
```yaml
raci:
  responsible: ["Data_Quality_Owner", "TF3_Lead"]
  accountable: "Role_Captain"
  consulted: ["Data_Engineers", "Business_Analysts"]
  informed: ["Sponsor_L1_Human", "Data_Consumers"]
```
