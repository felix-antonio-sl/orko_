# F1/F3 Mapping – 06_gore_nuble_completo

## Propósito

Mapeo explícito de cómo `context.yaml` y `trajectory.md` del caso **06_gore_nuble_completo** instancian los contratos F1/F3.

Versión: P0-COMPLETE (ORKO v1.0.0)

---

## §1 MAPEO F1 (Context Assessment)

### Inputs F1 → Fuentes

| Input F1 | Fuente | Notas |
|----------|--------|-------|
| `stakeholder_interviews` | **Implícito** | Perfil deriva de entrevistas con autoridades/directivos GORE |
| `org_documentation` | **Implícito** | `tech_stack_maturity: mixed_legacy_modern` sugiere mapeo de sistemas heredados + modernos |
| `regulatory_context` | `context.yaml::regulatory_context` | "Marco normativo... sector público chileno (ley de bases, compras públicas, transparencia)" |

### Outputs F1 → Artefactos

| Output F1 | Artefacto | Mapeo |
|-----------|-----------|-------|
| `context_profile_36_params` | `context.yaml` | 15 campos presentes; se asumen 21 campos adicionales implícitos (runway, presupuesto, métricas TF1/TF2/TF3) |
| `h_org_baseline` | **No explícito** | Gap: H_org debería calcularse con `health_score_calculator.xlsx`. Se infiere banda **G2/G3** (Minimal sin crisis) |
| `context_classification` | `tipo_contexto: enterprise`, `maturity_level: public_admin_mature`, `crisis_flags: false` | Clasificación: **G2/G3** (sin crisis, presión de accountability) |
| `regulatory_constraints` | `context.yaml::regulatory_context` | Marco completo de probidad pública → alto impacto en F8/F12 |
| `tech_debt_inventory` | **No presente** | Gap: `tech_stack_maturity: mixed_legacy_modern` indica deuda técnica significativa pero sin detalle |

---

## §2 MAPEO F3 (Trajectory Selection)

### Inputs F3 → Fuentes

| Input F3 | Fuente | Mapeo |
|----------|--------|-------|
| `F1.context_profile_36_params` | `context.yaml` | Ver §1 |
| `F1.h_org_baseline` | **Inferido** | H_org en banda G2/G3 |
| `F1.context_classification` | `context.yaml` | Enterprise público maduro, sin crisis |
| `F1.regulatory_constraints` | `context.yaml::regulatory_context` | Marco probidad pública chileno (alto) |
| `stakeholder_risk_tolerance` | **Implícito** en `risk_profile` | "Riesgo político y reputacional alto" → tolerancia **baja** al riesgo operativo |
| `budget_commitment` | **No explícito** | Gap: presupuesto público asignado no documentado. Se asume **limitado** por restricciones fiscales |
| `timeline_constraints` | **No explícito** | Gap: plazos políticos/administrativos no documentados. Se asume ciclo 12 meses (anual presupuestario) |

### Outputs F3 → Artefactos

| Output F3 | Artefacto | Mapeo |
|-----------|-----------|-------|
| `trajectory_selected` | `context.yaml::default_trajectory` + `trajectory.md` §1 | **Minimal** (explícito) |
| `timeline_commitment` | **Implícito** | 6–12 meses (Minimal) |
| `budget_allocation` | **No presente** | Gap |
| `phase_sequence` | **Implícito** en `trajectory.md` §2 | F13, F17, F4/F5 mencionados |
| `playbook_preselection` | `trajectory.md` §2 | P01, P03, P09, P10, P11 según G1–G4 |
| `trajectory_decision_rationale` | `trajectory.md` §1–§2 | **Presente:** consolidar prácticas, mejorar coordinación, elevar H_org sin grandes inversiones TF |

---

## §3 CONEXIÓN CON CONTEXT_DECISION_MATRIX

### Reglas aplicadas

| Regla DM | Aplicación en 06_gore_nuble | Evidencia |
|----------|----------------------------|-----------|
| **DM1_H_org_critical** | **No aplica** en baseline | `crisis_flags: false` |
| **DM2_runway_short** | **No aplica** directamente | Budget público estable; DM2 se activaría solo ante crisis política |
| **DM3_budget_minimal** | **Sí aplica** | Budget limitado + H_org >= G2 → **Minimal** coherente con DM3 |
| **DM4_ambition_high** | **No aplica** | No cumple G4 + budget avanzada |
| **DM5_regulatory_heavy** | **Aplica parcialmente** | Marco regulatorio alto extendería timeline (ya considerado en horizonte 12 meses) |

**Conclusión:** `trajectory_selected = Minimal` coherente con DM3 + DM5 (regulatory heavy).

---

## §4 CONEXIÓN CON HEALTH GATES G1–G4

`trajectory.md` §2 documenta decisiones F17 según gates:

| Health Gate | Uso en 06_gore_nuble |
|-------------|---------------------|
| **G1 (Crítico)** | Reservado para crisis severa (escándalos, fallas graves) → paso a Survival (DM1) |
| **G2 (Bajo/Riesgo)** | Monitoreo activo: si H_org cae por conflictos políticos/atrasos → P09 + P01 focalizado |
| **G3 (Bueno/Eficiencia baja)** | Estado actual inferido: ciclos de optimización P10/P11/P03 |
| **G4 (Ready for Avanzada)** | Módulos específicos (ej. gestión de datos) podrían operar en Avanzada si alcanzan G4 |

---

## §5 GAPS Y FORTALEZAS

### Gaps
1. H_org baseline no calculado
2. Schema T01 ausente (context.yaml no sigue 36 parámetros formales)
3. Inputs externos F3 no explícitos (budget, timeline, risk tolerance)
4. Calculadoras no aplicadas
5. `budget_allocation.yaml` ausente

### Fortalezas
1. Trayectoria Minimal bien justificada
2. Conexión clara con DM2/DM3/DM5 y G1–G4
3. Consideración explícita de marco regulatorio sector público
4. Adaptación F17 documentada por escenarios

---

## §6 CONCLUSIÓN

El caso **06_gore_nuble_completo** instancia razonablemente F1/F3 a nivel conceptual, con `context.yaml` como proxy de F1 outputs y `trajectory.md` materializando F3 outputs. Decisión Minimal coherente con DM3 (budget limited) + DM5 (regulatory heavy) + contexto público maduro. Faltan artefactos formales (H_org, calculadoras, budget_allocation) para cerrar loop completo F1→decision_matrix→F3.

---

**Versión:** P0-COMPLETE  
**Autor:** sq1/E1  
**Fecha:** 2025-11-18
