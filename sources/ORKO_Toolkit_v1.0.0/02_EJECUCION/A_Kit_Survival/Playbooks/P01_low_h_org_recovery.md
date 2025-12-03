# P01_low_h_org_recovery

**Tipo:** Playbook Recovery  
**ID:** P01  
**Trigger:** `H_org` en zona crítica (G1/G2)  
**Estimación Ejecución:** `P1D`

---

## §0. FUNDAMENTO

**Layer 0:** `A1`, `A5`, `P1`, `P4`, `I3`, `I6`  
**Layer 1:** `D2`, `D4`, `E6`  
**Layer 2:** `TF1`, `TF2`

**Justificación:** Cuando `H_org` cae por debajo de los umbrales definidos en G1/G2, la organización entra en riesgo operativo. Este playbook articula capacidades (`P1`) y límites (`P4`) para ejecutar una respuesta rápida (F14) basada en las señales de `F13` y asegurar trazabilidad (`I3`) y adaptación controlada (`I6`).

---

## §1. INTERFAZ

### Trigger Conditions

```yaml
triggers:
  - condition: "H_org < 60"
    metric: "H_org"
    threshold: 60
    source: "F13.h_org_dashboard"
  - condition: "H_org cayendo 2 cortes consecutivos"
    metric: "H_org"
    threshold: "tendencia negativa"
    source: "F13.trend_analysis"
  - condition: "G1 o G2 activados"
    metric: "H_org"
    threshold: "G1/G2"
    source: "13_metricas_validacion/02_health_gates.md"
```

### Outputs

```yaml
outputs:
  - report: "P01_execution_report.md"
    consumers: ["F13", "F16", "F17", "E4_governance"]
  - artifact: "h_org_recovery_plan.yaml"
    consumers: ["F14", "F16", "trayectorias.Minimal"]
  - metric_update: "H_org_post_recovery"
    consumers: ["F13", "G1", "G2"]
```

---

## §2. EJECUCIÓN

**Pasos**:
1. **Diagnóstico inmediato** (2-4h): Identificar componentes H_org degradados (H1-H4)
2. **Priorizar acciones** (2h): Top-3 gaps críticos por impacto×urgencia
3. **Plan recuperación** (4h): Crear h_org_recovery_plan.yaml con timeline
4. **Ejecutar quick wins** (1-3 días): Acciones inmediatas (P10, P11, P12)
5. **Monitoreo recovery** (continuo): Track H_org improvement vía F13

**Criterios éxito**:
- H_org > 65 en 7-14 días
- Ningún componente H1-H4 < 50
- Recovery plan aprobado por Sponsor_L1_Human

---

## §3. RACI

```yaml
raci:
  responsible: ["Role_HealthOwner", "Role_Delivery_Lead"]
  accountable: "Sponsor_L1_Human"
  consulted: ["Role_Captain", "TF1_Lead", "TF2_Lead", "TF3_Lead"]
  informed: ["Board_Governance", "All_Stakeholders"]
```
