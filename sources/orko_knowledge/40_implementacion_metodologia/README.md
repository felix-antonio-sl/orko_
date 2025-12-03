# Layer 4: Implementación y Herramientas (Dev)

> **⚠️ Zona de Desarrollo:**
> Este directorio contiene el código fuente (Python) y las especificaciones técnicas para **generar** las herramientas de usuario.
> No intente ejecutar estos scripts a menos que esté desarrollando el framework.

---

## Contenido
*   **`calculadoras/`**: Archivos `.xlsx` generados (Output).
*   **`dev_specs/`**: Especificaciones técnicas y scripts de generación.
    *   `scripts/generate_calculadoras_cap22.py`: El script maestro que crea `T00_Inventario_Maestro.xlsx` y `health_score_calculator.xlsx`.
*   **`ejemplos/`**: Casos de uso de referencia (Stubs/WIP).

## Cómo Regenerar Herramientas
Si realizaste cambios en la lógica de cálculo (Layer 0/1) y necesitas actualizar los Excel:

1.  Activa el entorno virtual:
    ```bash
    source dev_specs/.venv_cap22/bin/activate
    ```
2.  Ejecuta el generador:
    ```bash
    python dev_specs/scripts/generate_calculadoras_cap22.py
    ```
3.  Verifica los outputs en `calculadoras/`.
