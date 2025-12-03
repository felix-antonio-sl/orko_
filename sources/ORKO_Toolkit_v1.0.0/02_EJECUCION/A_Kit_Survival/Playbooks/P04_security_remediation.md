# P04_security_remediation

**Tipo:** Playbook Recovery  
**ID:** P04  
**Trigger:** Incidente de seguridad o gap de cumplimiento que amenaza `H_org`/`ROI_Habilitacion`  
**Estimación Ejecución:** `P2D`

---

## §0. FUNDAMENTO

**Layer 0:** `A1`, `A4`, `P3`, `P4`, `I3`, `I5`, `I6`  
**Layer 1:** `D2`, `D4`, `E6`  
**Layer 2:** `TF3`

**Justificación:** Los incidentes de seguridad o gaps regulatorios (`P4`) impactan directamente la salud organizacional (`H_org`) y el retorno de habilitación (`ROI_Habilitacion`). P04 define respuesta inmediata y trazable (`I3`) preservando responsabilidad humana (`I5`) y aprendizaje para ajustes posteriores (`I6`).

---

## §1. INTERFAZ

### Trigger Conditions

```yaml
triggers:
  - condition: "Security incident confirmado por F11"
    metric: "H_org"
    threshold: "impacto en H_org"
    source: "F13.incident_reports"
  - condition: "Compliance gap crítico detectado en F8"
    metric: "ROI_Habilitacion"
    threshold: "impacto en ROI"
    source: "F13.roi_habilitacion"
  - condition: "G1/G2 escalado por riesgo de seguridad"
    metric: "H_org"
    threshold: "G1/G2"
    source: "13_metricas_validacion/02_health_gates.md"
```

### Outputs

```yaml
outputs:
  - report: "P04_security_report.md"
    consumers: ["F13", "F16", "F17", "E4_governance"]
  - artifact: "remediation_plan_security.yaml"
    consumers: ["F8", "F11", "F14"]
  - metric_update: "H_org_security_delta"
    consumers: ["F13", "G1", "G2"]
```

---

## §2. EJECUCIÓN

**Pasos**:
1. **Contención** (inmediato): Mitigar riesgo security/compliance
2. **Análisis impacto** (4h): Evaluar impacto H_org y ROI_Habilitacion
3. **Plan remediación** (1 día): Definir acciones correctivas
4. **Implementación** (2-5 días): Ejecutar remediation plan
5. **Post-mortem** (4h): Documentar learnings y prevención

**Criterios éxito**:
- Incident cerrado
- Compliance gap remediado
- H_org recovery
- Post-mortem publicado

---

## §3. RACI

```yaml
raci:
  responsible: ["Role_SecurityOwner", "Role_ComplianceOfficer"]
  accountable: "Role_Captain"
  consulted: ["TF3_Lead", "Legal", "Infosec_Team"]
  informed: ["Sponsor_L1_Human", "Board_Governance", "Regulators"]
```
