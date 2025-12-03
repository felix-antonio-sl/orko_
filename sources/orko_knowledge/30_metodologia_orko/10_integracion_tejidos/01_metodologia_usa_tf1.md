# TF1 (Humano) - Integración con Metodología ORKO

## Tabla de Acción por Fase WSLC

| Fase | Acción sobre TF1 | Artefacto Salida | Criterio OK |
|------|------------------|------------------|-------------|
| F1 Context | Inventario capacidades humanas actuales | `capacity_baseline.yaml` | 100% team mapeado con substrate=Humano |
| F4 Capability Mapping | Clasificar C0-C3 por rol | `capacity_inventory.yaml` | Schema TF1.CapacityAsset validado |
| F7 Purpose Cascade | Asignar OKRs a personas | `okr_assignments.yaml` | Cada OKR tiene accountable human |
| F10 Quick Wins | Activar capacidades ociosas | `capacity_reallocation.md` | ≥1 capacidad movida de "Idle" a "Active" |
| F14 Incident | Auditar disponibilidad post-fallo | `capacity_health_report.yaml` | availability_rate calculado |

## Ejemplo Concreto: Startup 50p

**Input** (`context.yaml`):
```yaml
team_size: 15
context_complexity: 4
h_org_baseline: 48
```

**Proceso F1→F4**:
1. Listar 15 personas en `capacity_baseline.yaml`
2. Clasificar: 3 C2 (Architects), 5 C1 (Team Leads), 7 C0 (ICs)
3. Detectar gap: 0 capacidades en Testing (substrate=Humano, role=QA)
4. Output: `capacity_inventory.yaml` con 15 entradas + gap documentado

**Fórmula H1_Humano**:
```
H1 = (Capacidades_Activas / Capacidades_Totales) × (1 - Saturación_Promedio)
   = (12 / 15) × (1 - 0.75)
   = 0.80 × 0.25 = 0.20 (CRÍTICO)
```

## Escalation Path

**Bloqueo**: No existe capacidad crítica (ej: Security Engineer)
**Acción**: Escalar a Captain → Decisión: ¿Hire externo o Train interno?
**Timeout**: 3 días → Auto-escalate a Sponsor

---
*MVO v1.0.0 - Para TF2/TF3, ver archivos hermanos en este directorio*
