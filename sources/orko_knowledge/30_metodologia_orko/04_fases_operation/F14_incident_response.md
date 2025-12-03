# F14 – Incident Response

## §0 FUNDAMENTO

```yaml
fase_id: F14
nombre_canonico: "Incident Response"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F14"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A3_Flujo"
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A4_Contexto"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P2_Flujo"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P3_Informacion"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I5_HAIC"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I3_Trazabilidad"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D4_Operacion"
  metricas_canonicas:
    - "VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.H_org"
relacion_kernel:
  depende_de:
    - "F13"
    - "F11"
    - "TF2_Flow"
  prepara_a:
    - "F15"
trayectorias_soportadas:
  - "Survival"
  - "Minimal"
estado_fundamento: "STABLE"
notas_fundamento: |
  F14 define el proceso responsable por incidentes que afectan H_org o la integridad de E7.
  Outputs: incident_report.md, incident_RCA.md, recovery_plan.yaml.
  Integración: playbooks P01/P04/P09 previstos. Se usan T10_incident_report.md y TEMPLATE_PLAYBOOK.md.
referencias_formales:
  - "30_metodologia_orko/04_fases_operation/F13_Health_Monitoring.md"
```

---

## §1 INTERFAZ

```yaml
inputs:
  - id: "h_org_current"
    source: "F13.h_org_current"
    required: true
    description: "Salud organizacional actual (para detectar degradación)"
  
  - id: "playbook_triggers"
    source: "F13.playbook_triggers"
    required: true
    description: "Lista de playbooks triggerados por health gates"
  
  - id: "drift_alerts"
    source: "F13.drift_alerts"
    required: false
    description: "Alertas de drift arquitectónico"
  
  - id: "incident_notification"
    source: "external OR F13"
    required: true
    description: "Notificación de incidente (manual o automatizada)"

outputs:
  - id: "incident_report"
    artifact: "incident_report.md"
    template: "T10_incident_report.md"
    consumers: ["F16", "F17"]
    description: "Reporte formal de incidente con timeline y impacto"
    location: "artefactos/f14/"
  
  - id: "recovery_actions"
    artifact: "recovery_actions.yaml"
    consumers: ["F15", "P01", "P02", "P04", "P09"]
    description: "Plan de acciones de recuperación"
    location: "artefactos/f14/"
  
  - id: "post_mortem"
    artifact: "post_mortem.md"
    consumers: ["F16"]
    description: "Análisis root cause y learnings"
    location: "artefactos/f14/"

dependencies:
  reads_from: ["F13"]
  writes_to: ["F16", "F17"]
  triggers: ["P01", "P02", "P04", "P09"]

acceptance_criteria:
  - criterion: "Incident_report completado dentro de 4 horas desde detección"
    verification: "timestamp incident_detected vs incident_report_created"
    responsible: "Role_IncidentLead"
    bloqueante: true
  
  - criterion: "Recovery_actions incluye accountability humana (I5_HAIC)"
    verification: "cada acción tiene owner humano asignado"
    responsible: "Role_HealthOwner"
  
  - criterion: "Post_mortem publicado dentro de 48h post-resolución"
    verification: "timestamp"
    responsible: "Role_IncidentLead"
  
  - criterion: "Playbook asociado ejecutado (si aplica)"
    verification: "playbook_execution_log != null"
    responsible: "Role_PlaybooksLead"

templates:
  - T10_incident_report.md
```

---

## §2 DESCRIPCIÓN EJECUTIVA

F14 gestiona respuesta a incidentes que degradan H_org o interrumpen operación, siguiendo protocolo formal de detección → contención → resolución → post-mortem.

**Actividades principales**:
1. Recibir alerta de F13 o notificación manual
2. Clasificar severidad (P0/P1/P2 según impacto H_org)
3. Asignar Role_IncidentLead y equipo respuesta
4. Ejecutar recovery_actions (puede triggerar playbooks)
5. Documentar incident_report con timeline
6. Conducir post_mortem y extraer learnings

**Playbooks asociados**:
- P01: Low H_org recovery (si H_org < 60)
- P02: Capacity spike (si overload capacidades)
- P04: Stakeholder escalation (si impacto externo)
- P09: Drift detection (si incidente arquitectónico)

**Duración estimada**: 2-48 horas (según severidad)

**Owner**: Role_IncidentLead + Role_HealthOwner

**Nota**: F14 NO es parte de trajectory Avanzada (crisis management)
