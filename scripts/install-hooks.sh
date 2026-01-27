#!/bin/bash
# Instalar Git Hooks KODA (ORKO)
# Ejecutar desde raíz del repo: ./scripts/install-hooks.sh

set -e

echo "🪝 Instalando git hooks KODA (ORKO)..."

# Verificar que estamos en un repo git
if [ ! -d ".git" ]; then
  echo "❌ Error: No se detectó repositorio git"
  echo "   Ejecuta este script desde la raíz del repo"
  exit 1
fi

# Copiar hooks
if [ -f "hooks/pre-commit" ]; then
  cp hooks/pre-commit .git/hooks/pre-commit
  chmod +x .git/hooks/pre-commit
  echo "✅ Pre-commit hook instalado"
else
  echo "⚠️  hooks/pre-commit no encontrado (ok si no se requieren validaciones locales)"
fi

if [ -f "hooks/post-commit" ]; then
  cp hooks/post-commit .git/hooks/post-commit
  chmod +x .git/hooks/post-commit
  echo "✅ Post-commit hook instalado"
fi

echo ""
echo "🎉 Git hooks configurados"
