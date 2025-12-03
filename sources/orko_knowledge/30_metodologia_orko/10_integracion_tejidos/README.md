# 10_integracion_tejidos – Layer 2 ↔ Layer 3

> ⚠️ **DISCLAIMER v1.0.0**: Los archivos `01_metodologia_usa_tf1.md`, `02_metodologia_usa_tf2.md`, `03_metodologia_usa_tf3.md` y `04_casos_integracion_e2e.md` son **PLACEHOLDERS** en esta versión. El contenido descrito en este README está en desarrollo para v1.1.0.  
> **Estado actual**: Este directorio documenta la intención y estructura de integración Layer 2↔3, pero la implementación detallada está en backlog. Para v1.0.0, los casos reales en `/40_implementacion_metodologia/ejemplos/` demuestran la integración práctica de tejidos con fases WSLC.

## Propósito del bloque

- Explicar **cómo se conectan los tejidos tecnológicos** (`TF1_Capacity`, `TF2_Flow`, `TF3_Information`) definidos en `20_tejidos/` con:
  - las fases WSLC F1–F18 (`30_metodologia_orko/01–05_fases_*`), y
  - los playbooks P01–P15 (`06–08_playbooks_*`).
- Servir como puente entre la **arquitectura de tejidos (Layer 2)** y la **metodología ejecutable (Layer 3)** sin redefinir contratos ni métricas del kernel.

 Referencias de detalle:

- `20_tejidos/00_introduccion_tejidos.md` – definición y derivación de TF1/TF2/TF3.
- `20_tejidos/05_integracion_tejidos.md` – patterns de integración TF1↔TF2↔TF3 y casos end-to-end.
- `40_implementacion_metodologia/dev_specs/KERNEL_READINESS.md` – kernel F1/F3/F7/F9/F13 y reglas de uso de métricas canónicas.

## Cómo se usa este directorio

 Este bloque se organiza en documentos que describen **cómo la metodología usa cada tejido** y cómo se integran en casos end-to-end:

- `01_metodologia_usa_tf1.md`  
  - Conecta TF1_Capacity (capacidades humanas/algorítmicas/mecánicas) con fases como F1/F4/F7/F10/F14 y con playbooks de recuperación y transformación (P01–P07).  
  - Se apoya en contratos de capacidades descritos en `20_tejidos/01_TF1_capacity.md` y en las instrucciones de kernel de `KERNEL_READINESS.md`.

- `02_metodologia_usa_tf2.md`  
  - Relaciona TF2_Flow (orquestación de flujos) con fases de diseño/ejecución (F5/F10–F12/F15) y con playbooks orientados a incidentes, flujo y cadencias (por ejemplo P02, P09–P15).  
  - Usa los patterns de integración "Capacity_Assignment" y "Event_Triggered_Flow" documentados en `20_tejidos/05_integracion_tejidos.md`.

- `03_metodologia_usa_tf3.md`  
  - Describe cómo TF3_Information (ciclo de vida de información y lakehouse) soporta fases de arquitectura y monitoreo (F6/F13) y casos como RAG pipelines, CI/CD e investigación multi‑agente.  
  - Se apoya en los subdominios Foundation/Analytics/Semantic descritos en `20_tejidos/03_TF3_information.md`.

- `04_casos_integracion_e2e.md`  
  - Vincula los patterns de `20_tejidos/05_integracion_tejidos.md` con ejemplos concretos en `40_implementacion_metodologia/ejemplos/*_completo/` (por ejemplo, pipelines de datos, RAG, CI/CD, multi‑agente).  
  - Su objetivo es mostrar la cadena completa: **contexto → fases WSLC → playbooks → tejidos TF1/TF2/TF3 → métricas/health gates**.

## Relación con fases y playbooks

- Fases WSLC donde la integración con tejidos es más explícita (ver `out/30_metodologia_orko.md` y `KERNEL_READINESS.md`):
  - F4/F5/F6/F7/F9 – diseño de capacidades, flujos, información y estado objetivo (se apoyan en contratos TF1/TF2/TF3).  
  - F11/F12 – deployment y transición de estado (orquestación TF2 + capacidades TF1 + artefactos TF3).  
  - F13–F15 – monitoreo, respuesta a incidentes y ejecución continua (observabilidad sobre TF1/TF2/TF3 y gatillos para playbooks).

- Playbooks P01–P15 usan tejidos como **infraestructura tecnológica** para ejecutar las decisiones tomadas en las fases WSLC, pero sus contratos (IDs, triggers, métricas canónicas) se mantienen congelados según CAP‑16/CAP‑18.

 Este README no introduce nuevos contratos; solo indica **dónde mirar** para entender la integración Layer 2 ↔ Layer 3 al trabajar con los demás documentos de `10_integracion_tejidos/`.
