
# P13_political_alignment

**Tipo:** Playbook Recovery  
**ID:** P13  
**Trigger:** Conflictos entre stakeholders o decisiones políticas degradan `H_org` sin causas técnicas evidentes  
**Estimación Ejecución:** `P2W`

---

## §0. FUNDAMENTO

**Layer 0:** `A1`, `A3`, `A5`, `P5`, `I3`, `I5`, `I6`  
**Layer 1:** `D1`, `D3`, `E6`  
**Layer 2:** `TF1`, `TF2`

**Justificación:** Muchas caídas de `H_org` provienen de conflictos políticos, decisiones contradictorias o falta de alineamiento entre actores clave, no de problemas puramente técnicos. P13 busca restaurar alineamiento político/organizacional en torno a propósito, trayectorias y compromisos, usando como marco `03_decision_matrix.md` y el RACI de `12_roles_governance`.

---

## §1. INTERFAZ

### Trigger Conditions

```yaml
triggers:
  - condition: "H_org cae y análisis técnico (P01–P04, P09–P12) no explica completamente la degradación"
    metric: "H_org"
    threshold: "por_debajo_baseline"
    source: "F13.h_org_dashboard"
  - condition: "Conflictos explícitos entre stakeholders o decisiones políticas divergentes documentadas en governance"
    metric: "H_org"
    threshold: "impacto_politico"
    source: "12_roles_governance/01_team_structure_raci.md"
```

### Outputs

```yaml
outputs:
  - report: "P13_political_alignment_report.md"
    consumers: ["F1", "F3", "F7", "F13", "F17", "E4_governance"]
  - artifact: "political_alignment_actions.yaml"
    consumers: ["F3", "F7", "F17", "trayectorias.Survival", "trayectorias.Minimal", "trayectorias.Avanzada"]
```


---

## §2. EJECUCIÓN
**Pasos**: 1) Identificar stakeholders clave, 2) Mapear intereses y resistencias, 3) Plan influencia, 4) Ejecutar engagements, 5) Validar alignment

---

## §3. RACI
```yaml
raci:
  responsible: ["Role_Captain", "Stakeholder_Manager"]
  accountable: "Sponsor_L1_Human"
  consulted: ["Communications", "Change_Management"]
  informed: ["Board_Governance", "Key_Stakeholders"]
```
