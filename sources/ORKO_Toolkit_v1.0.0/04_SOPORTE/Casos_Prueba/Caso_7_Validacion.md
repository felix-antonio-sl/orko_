# Caso 7: Validación de Campo (Scenario "Fintech Caos")

## 🎯 Objetivo
Validar que un usuario nuevo puede diagnosticar correctamente una organización y encontrar las herramientas adecuadas en menos de 30 minutos.

## 🏢 Contexto: "Fintech X"
Usted acaba de ser contratado como consultor para "Fintech X", una startup de pagos que creció demasiado rápido.
*   **Situación:** El CEO está estresado. Los clientes se quejan de errores. El equipo de ingeniería está "quemado".
*   **Misión:** Usar ORKO para estabilizar la situación.

## 📝 Datos para el Inventario (T00)

Abra `01_DIAGNOSTICO/1.1_Inventario_Maestro.xlsx` e ingrese estos datos aproximados:

### Pestaña P1_PERSONAS
*   Liste **30 personas** con rol "Humano" (Invente nombres o use "Dev 1", "Dev 2"...).
*   Marque **10** como "Activo".
*   Marque **20** como "Saturado" o "Ocioso".
*   *Resultado esperado:* TF1 Score bajo (aprox 33%).

### Pestaña P2_FLUJOS
*   Liste **5 flujos críticos** (ej: Onboarding, Pagos, Soporte, Reembolsos, Reportes).
*   Marque "Documentado?" = **No** en todos.
*   Marque "Automatizado?" = **0%** en todos.
*   *Resultado esperado:* TF2 Score = 0%.

### Pestaña P3_DATOS
*   Liste **3 fuentes de datos** (CRM, Base de Datos, Excel Finanzas).
*   Calidad = **2** (en escala 1-5).
*   *Resultado esperado:* TF3 Score bajo.

## 🧮 Cálculo de Salud

1.  Vaya a `01_DIAGNOSTICO/1.2_Calculadora_Salud.xlsx`.
2.  Use el **WIZARD** para copiar los totales del Inventario.
3.  Verifique el resultado en la pestaña `Outputs`.

### Resultado Esperado
*   **H_org:** Debería estar entre **0.20 y 0.40**.
*   **Banda:** **G1-Crítico**.
*   **Recomendación:** **Survival Mode**.

## 🚀 Ejecución

Basado en el resultado, vaya a `02_EJECUCION` y abra la carpeta correcta.
*   ¿Qué carpeta abrió? (Debería ser `A_Kit_Survival`).
*   ¿Qué Playbook debe ejecutar primero? (Debería ser `P01_Low_H_org_Recovery`).

---
*Si logró llegar aquí sin preguntar al autor, ¡Felicidades! El sistema funciona.*
