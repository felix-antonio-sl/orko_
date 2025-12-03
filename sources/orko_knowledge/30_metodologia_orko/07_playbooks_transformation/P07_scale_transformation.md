
# P07_scale_transformation

**Tipo:** Playbook Transformation  
**ID:** P07  
**Trigger:** Piloto (P06) exitoso con mejora sostenida en `H_org`/`eta_org` y decisión de escalar a más dominios  
**Estimación Ejecución:** `P8W`

---

## §0. FUNDAMENTO

**Layer 0:** `A1`, `A3`, `A5`, `P1`, `P2`, `P5`, `I3`, `I6`  
**Layer 1:** `D1`, `D2`, `D4`, `E6`, `E7`  
**Layer 2:** `TF1`, `TF2`

**Justificación:** Tras un piloto exitoso (P06) que mejora `H_org` y `eta_org` en un dominio acotado, P07 define cómo escalar la transformación a más unidades/dominos sin perder trazabilidad (`I3`) ni capacidad de adaptación (`I6`), manteniendo el alineamiento con propósito (`P5`) y capacidades (`P1`).

---

## §1. INTERFAZ

### Trigger Conditions

```yaml
triggers:
  - condition: "P06 demuestra mejora sostenida en H_org y eta_org en dominio piloto"
    metric: "H_org"
    threshold: "mejora_confirmada"
    source: "F13.h_org_dashboard"
  - condition: "Evaluación F9/F11 recomienda escalar el diseño piloto a más dominios"
    metric: "eta_org"
    threshold: "por_sobre_target_piloto"
    source: "F13.eta_org_dashboard"
```

### Outputs

```yaml
outputs:
  - report: "P07_scale_transformation_report.md"
    consumers: ["F9", "F11", "F12", "F15", "F17", "E4_governance"]
  - artifact: "scale_transformation_plan.yaml"
    consumers: ["F11", "F12", "F15", "trayectorias.Minimal", "trayectorias.Avanzada"]
```

### Casos típicos

- **CT1 – Escala post‑G4:** G4 activo, piloto (P06) exitoso en un dominio core y decisión de ampliar a varias unidades/regiones.  
- **CT2 – Escala gradual:** se decide secuenciar la escala en waves para no comprometer `H_org` mientras se incrementa `eta_org` y `ROI_Habilitacion`.

### Inputs adicionales

- Resultados consolidados de P06 (`P06_pilot_transformation_report.md`).  
- `F11` – blueprint de ejecución de flujos a escala.  
- `F13` – métricas de `H_org`, `eta_org`, `ROI_Habilitacion` pre/post piloto.  
- `F16` – aprendizajes clave del piloto y riesgos identificados.

### Riesgos y mitigación

- **R1 – Sobre‑escala:** escalar demasiado rápido y degradar `H_org` a pesar de mejoras locales en `eta_org`.  
  - Mitigación: usar G1–G4 como frenos de seguridad; si G2/G3 se activan, ralentizar escala y activar P01/P09.  
- **R2 – Heterogeneidad de contextos:** dominios adicionales con contexto distinto al piloto (ver `context_pattern_schema`).  
  - Mitigación: coordinar con E2 para validar patrones de contexto y ajustar el plan de escala.


---

## §2. EJECUCIÓN
**Pasos**: 1) Validar piloto éxitoso, 2) Planificar escala multi-dominio, 3) Secuenciar rollout, 4) Monitorear H_org durante escala, 5) Ajustar según feedback

---

## §3. RACI
```yaml
raci:
  responsible: ["Transformation_Lead", "Program_Manager"]
  accountable: "Role_Captain"
  consulted: ["Domain_Leads", "Role_HealthOwner"]
  informed: ["Sponsor_L1_Human", "All_Organization"]
```
