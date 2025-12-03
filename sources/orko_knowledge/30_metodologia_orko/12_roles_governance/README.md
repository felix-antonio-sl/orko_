# 12 – Roles y governance

## §0. Propósito del bloque

- Este bloque describe cómo se distribuyen **roles, responsabilidades y paths de escalamiento** alrededor de la metodología ORKO.
- Conecta health gates, playbooks P01–P15, CAP-x y el `board_coordinación.md` con estructuras humanas concretas.

## §1. Componentes actuales

- `01_team_structure_raci.md`
  - Documento principal de estructura de equipo y RACI.
  - Define quién **detecta**, quién **decide**, quién **ejecuta** y quién **audita** en escenarios clave (gates G1–G4, CAP-14–CAP-20, operación de playbooks).

- `02_capacity_planning.md` (esqueleto)
  - Espacio reservado para detallar cómo se planifica capacidad humana frente a trayectorias y playbooks.

- `03_escalation_paths.md` (esqueleto)
  - Destinado a documentar paths claros de escalamiento cuando los equipos no pueden resolver un problema en su nivel.

- `04_multi_authority_patterns.md` (esqueleto)
  - Para patrones donde coexisten múltiples autoridades (negocio/tecnología/regulador) y cómo se gobierna sin bloquear la evolución.

- `05_non_traditional_roles.md` (esqueleto)
  - Para roles no clásicos (p.ej. facilitadores, stewards de métricas, curadores de casos) que emergen en ORKO.

## §2. Relación con health gates, playbooks y board

- **Health gates (`30_metodologia_orko/13_metricas_validacion/02_health_gates.md`):**
  - Cada gate define no solo métricas y umbrales, sino también **quién** tiene autoridad para activar playbooks, pausar trabajo o escalar.

- **Playbooks P01–P15:**
  - Los playbooks describen acciones; este bloque define qué roles deben ejecutarlas o aprobarlas.
  - El objetivo es mantener **accountability humana (I5)** clara cuando se usan artefactos automatizados o agentes.

- **Board de coordinación (`30_metodologia_orko/00_wip_desarrollo_metodologia/board_coordinación.md`):**
  - Centraliza INTENT/OUTCOME/NEED/MANDATO/DECISIÓN.
  - Los roles definidos aquí explican quién puede registrar eventos, quién debe leerlos y quién responde a `[NEED]`.

## §3. Lineamientos para ORKO v1.0.0

- `01_team_structure_raci.md` se considera el contrato principal de governance para esta versión.
- Los demás archivos (`02`–`05`) pueden estar en estado esquelético; su desarrollo posterior debe respetar RACI, health gates y VG3 sin introducir nuevos roles canónicos sin pasar por VOCAB/CAP.
- Cualquier cambio que afecte directamente a quién decide/ejecuta/audita en playbooks o gates debe pasar por CAP-x y quedar reflejado en el board.
