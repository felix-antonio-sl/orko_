# Escalation Paths - Matriz de Decisión MVO

## Matriz de Escalamiento

| Evento / Trigger | Condición | Acción Inmediata | Escalado a | Tiempo Máx. |
|------------------|-----------|------------------|------------|-------------|
| **Caída H_org** | H_org < 50 (Survival) | Activar P01 Recovery | Role_Captain | 2 horas |
| **Drift Métrico** | Desviación > 10% vs Target | Activar P09 Drift Response | Role_HealthOwner | 24 horas |
| **Bloqueo Operativo** | Impedimento > 2 días | Convocar "War Room" | Role_Captain | 48 horas |
| **Bloqueo Político** | Conflicto de OKRs | Activar P13 Political Alignment | Role_SteeringCommittee | 3 días |
| **Incidente Seguridad** | Brecha confirmada | Activar P04 Security Remediation | CISO / Role_Captain | 15 minutos |

## Protocolo de Comunicación

1.  **Detectar:** Cualquier rol puede levantar la mano.
2.  **Clasificar:** Usar la matriz anterior para determinar severidad.
3.  **Notificar:** Usar canal oficial (Slack #orko-alerts / Email urgente).
4.  **Actuar:** El rol responsable DEBE acusar recibo en < Tiempo Máx.

## Regla de Oro

> "Si tienes duda de si debes escalar, **ESCALA**. El costo de una falsa alarma es menor que el costo de un silencio catastrófico."

---
*MVO v1.0.0 - Versión simplificada para operación ágil.*
