#!/bin/bash
################################################################################
# test-local.sh - Test du site en local avant déploiement AWS
#
# Usage:
#   ./aws/test-local.sh
################################################################################

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}   SOLAIRE EMPIRE - Test Local${NC}"
echo -e "${BLUE}================================================${NC}\n"

# Vérification des fichiers critiques
echo -e "${YELLOW}[1/4] Vérification des fichiers...${NC}"

REQUIRED_FILES=(
    "src/index.html"
    "src/styles.css"
    "src/app.js"
    "src/components/VideoHero.js"
    "src/components/VideoHero.css"
    "data/catalogue.json"
    "agents/results_gemini_web.json"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓ $file${NC}"
    else
        echo -e "${RED}✗ $file manquant${NC}"
        exit 1
    fi
done

# Validation JSON
echo -e "\n${YELLOW}[2/4] Validation JSON...${NC}"

for json_file in data/catalogue.json agents/results_gemini_web.json; do
    if python3 -m json.tool "$json_file" > /dev/null 2>&1; then
        echo -e "${GREEN}✓ $json_file valide${NC}"
    else
        echo -e "${RED}✗ $json_file invalide${NC}"
        exit 1
    fi
done

# Build test
echo -e "\n${YELLOW}[3/4] Build test...${NC}"
mkdir -p dist-test/data dist-test/agents dist-test/components

cp src/index.html dist-test/
cp src/styles.css dist-test/
cp src/app.js dist-test/
cp -r src/components/* dist-test/components/
cp data/catalogue.json dist-test/data/
cp agents/results_gemini_web.json dist-test/agents/

echo -e "${GREEN}✓ Build test réussi${NC}"
echo "Fichiers générés:"
du -sh dist-test/*

# Lancement serveur local
echo -e "\n${YELLOW}[4/4] Lancement serveur local...${NC}"
echo -e "${GREEN}Serveur démarré sur: http://localhost:8000${NC}"
echo -e "${YELLOW}Appuyez sur Ctrl+C pour arrêter${NC}\n"

cd dist-test && python3 -m http.server 8000
