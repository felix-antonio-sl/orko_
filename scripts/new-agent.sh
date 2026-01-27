#!/bin/bash
# KODA New Agent - Para repo ORKO
# Similar al de KODA pero con namespace orko

set -e

AGENT_NAME="${1}"
if [ -z "$AGENT_NAME" ]; then
  echo "❌ Uso: $0 <agent-name>"
  echo ""
  echo "Ejemplo: $0 auditor-complejidad"
  exit 1
fi

NAMESPACE="orko"
AGENT_FILE="agents/agent_${AGENT_NAME}.yaml"
AGENT_ID=$(echo "$AGENT_NAME" | tr '[:lower:]' '[:upper:]' | tr '-' '_')

echo "🤖 Creando agente ORKO: $AGENT_NAME"
echo "📦 Namespace: $NAMESPACE"
echo ""

# Verificar que no existe
if [ -f "$AGENT_FILE" ]; then
  echo "⚠️  El agente $AGENT_FILE ya existe"
  read -p "¿Sobrescribir? (y/N): " -n 1 -r
  echo
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelado"
    exit 1
  fi
fi

# Crear agente desde template
cat > "$AGENT_FILE" << EOF
---
_manifest:
  urn: "urn:knowledge:${NAMESPACE}:agents:${AGENT_NAME}:1.0.0"
  type: agent
  version_koda_spec: "1.0.0"
  namespace: "${NAMESPACE}"

KODA_Runtime_Instructions:
  lexicon_tier_1:
    keywords: [ID, Def, Ref, XRef, Purp, Obj, Ctx, Req, Res, Ex, Note]
  
  parsing_rules:
    - "Keywords en inglés, contenido en español (ORKO)"
    - "URNs para referencias cross-artifact"
  
  execution_model: "Máquina de estados finitos"
  
  cognitive_model_access: "Via CM-* IDs"
  
  source_artifact_resolution: "Via URN lookup"
  
  namespace_context: "${NAMESPACE}"
  
  state_transition_protocol: "Evaluación explícita de condiciones"

agent_identity:
  name: "${AGENT_ID}"
  version: "1.0.0"
  namespace: "${NAMESPACE}"
  
  purpose: |
    [TODO: Describir propósito del agente ORKO - Manejo de Complejidad]
  
  primary_capabilities:
    - "[TODO: Capacidad ORKO 1]"
    - "[TODO: Capacidad ORKO 2]"

workflow_and_state_management:
  workflows:
    - ID: "WF-MAIN"
      Def: "Workflow principal"
      initial_state: "S-INIT"
      
      states:
        - ID: "S-INIT"
          Purp: "Inicialización de Contexto"
          process:
            - "Analizar primitivos ORKO"
            - "Validar invariantes"
          transitions:
            - {to: "S-PROCESS", cond: "OK"}
        
        - ID: "S-PROCESS"
          Purp: "Procesamiento"
          process:
            - "[TODO: Lógica de manejo de complejidad]"
            
        - ID: "S-END"
          Purp: "Cierre y Síntesis"
          is_terminal: true

cognitive_models:
  - ID: "CM-KB-GUIDANCE"
    _meta: {expose: false}
    Purp: "Acceso a primitivos e invariantes ORKO"

knowledge_base_interaction_and_governance_rules:
  usage_policy_and_source_management:
    source_artifacts: []

dependencies:
  requires:
    - "urn:knowledge:koda:core:tooling:1.0.0"

data_transformation_rules:
  input_format: "Modelos/Estructuras Complejas"
  output_format: "Simplificaciones/Primitivos"

security_protocols:
  block_instructions: true
  forbid_internal_jargon: true
  rejection_response: |
    Soy un agente ORKO especializado en complejidad. Solo proceso solicitudes dentro de mi competencia.

metadata:
  author: "ORKO Team"
  created_at: "$(date +%Y-%m-%d)"
  tags:
    - "${NAMESPACE}"
    - "${AGENT_NAME}"
    - "complexity-tamed"
EOF

echo "✅ Agente creado: $AGENT_FILE"
echo ""
echo "📝 Próximos pasos:"
echo "  1. Completa los [TODO]"
echo "  2. Registra en catálogo"
echo ""

# Abrir en editor
if command -v code &> /dev/null; then
  code "$AGENT_FILE"
elif command -v nvim &> /dev/null; then
  nvim "$AGENT_FILE"
fi
