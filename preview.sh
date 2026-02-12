#!/bin/bash
################################################################################
# preview.sh - Script de Preview - Solaire Empire
# Lance le serveur local et ouvre le navigateur
################################################################################

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}============================================================${NC}"
echo -e "${BLUE}   SOLAIRE EMPIRE - Preview Local${NC}"
echo -e "${BLUE}============================================================${NC}\n"

# Vérification Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERREUR] Python n'est pas installé${NC}"
    exit 1
fi

echo -e "${GREEN}[OK] Python détecté${NC}"
echo ""

# Changement de répertoire
cd "$(dirname "$0")/src"
echo "Répertoire: $(pwd)"
echo ""

echo -e "${YELLOW}[1/2] Démarrage du serveur...${NC}"
echo -e "${GREEN}URL: http://localhost:8000${NC}"
echo ""
echo -e "${YELLOW}[2/2] Ouverture du navigateur dans 3 secondes...${NC}"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter le serveur"
echo -e "${BLUE}============================================================${NC}\n"

# Attendre 3 secondes et ouvrir le navigateur
sleep 3

# Ouvrir le navigateur selon l'OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open http://localhost:8000
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    xdg-open http://localhost:8000 2>/dev/null || true
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows Git Bash
    start http://localhost:8000
fi

# Lancer le serveur Python
python3 -m http.server 8000
