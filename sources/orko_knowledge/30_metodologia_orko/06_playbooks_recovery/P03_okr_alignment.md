# P03_okr_alignment

**Tipo:** Playbook Recovery  
**ID:** P03  
**Trigger:** Desalineamiento entre propósito/OKR y resultados (`H_org`, `eta_org`)  
**Estimación Ejecución:** `P3D`

---

## §0. FUNDAMENTO

**Layer 0:** `A2`, `A5`, `P5`, `I3`, `I5`, `I6`  
**Layer 1:** `D1`, `D3`, `E6`  
**Layer 2:** —

**Justificación:** Cuando `H_org` y/o `eta_org` caen por debajo de objetivos pese a contar con propósito y arquitectura definidos (F7, F9), se evidencia una ruptura en la cascada de propósito (`P5`). P03 restablece alineamiento OKR preservando trazabilidad (`I3`), accountability humana (`I5`) y ajustes de trayectoria (`I6`).

---

## §1. INTERFAZ

### Trigger Conditions

```yaml
triggers:
  - condition: "H_org < target definido en F7/F9"
    metric: "H_org"
    threshold: "target_fase"
    source: "F13.h_org_dashboard"
  - condition: "eta_org < 0.60 con OKR aprobados"
    metric: "eta_org"
    threshold: 0.60
    source: "F13.eta_org_tracking"
  - condition: "Alertas G2 sobre desalineamiento OKR"
    metric: "H_org"
    threshold: "G2"
    source: "13_metricas_validacion/02_health_gates.md"
```

### Outputs

```yaml
outputs:
  - report: "P03_alignment_report.md"
    consumers: ["F7", "F9", "F13", "F17"]
  - artifact: "okr_alignment_plan.yaml"
    consumers: ["F7", "trayectorias.Avanzada", "E4_governance"]
  - metric_update: "H_org_alignment_delta"
    consumers: ["F13", "G2"]
```

---

## §2. EJECUCIÓN

**Pasos**:
1. **Auditoría OKR** (4h): Revisar cascade F7 vs resultados actuales
2. **Gap analysis** (4h): Identificar desconexión propósito-ejecución
3. **Realinear OKRs** (1 día): Ajustar o refinar OKRs con stakeholders
4. **Communication plan** (4h): Comunicar cambios a equipos
5. **Tracking** (continuo): Monitorear alineamiento post-ajuste

**Criterios éxito**:
- 90% OKRs L4-L1 alineados
- H_org improvement >5 puntos en 30 días
- Sponsor approval

---

## §3. RACI

```yaml
raci:
  responsible: ["Role_Captain", "Role_PurposeOwner"]
  accountable: "Sponsor_L1_Human"
  consulted: ["Role_Architect", "Area_Leads"]
  informed: ["All_Stakeholders", "Board_Governance"]
```
