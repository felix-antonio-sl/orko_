# 🚨 Kit Survival - Recuperación de Crisis

## ¿Dónde Estoy?
Usted está en el **Kit Survival** porque su Health Score (`H_org`) es **menor a 50**.
Esto significa que su organización tiene **riesgo crítico** en al menos una dimensión (capacidad, flujo o datos).

## ¿Qué Hago Aquí?
**NO** intente ejecutar la metodología completa. **FOCO**: Estabilizar en 2-4 semanas.

### Tareas Inmediatas
1.  **Recuperar Capacidad:** Ejecute `Playbooks/P01_Low_H_org_Recovery.md`. Identifique qué rol falta o está saturado y soluciónelo en 5 días.
2.  **Reducir Fricción:** Ejecute `Playbooks/P02_Handoff_Reduction.md`. Elimine pasos innecesarios en sus flujos críticos.
3.  **Asegurar:** Si tiene brechas de seguridad, use `Playbooks/P04_Security_Remediation.md`.

### Herramientas
*   Use `Templates/T10_Incident_Report.md` para documentar cualquier fuego que apague. Esto genera datos para evitar que se repita.

## ¿Qué Sigue?
Una vez que ejecute **al menos 1 playbook** y su `H_org` suba por encima de 50:
1.  Vuelva a `01_DIAGNOSTICO`.
2.  Recalcule su salud.
3.  Si `H_org >= 50`, ¡Felicidades! Gradúese al **Kit Minimal**.
