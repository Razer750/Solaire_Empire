#!/bin/bash
################################################################################
# deploy.sh - Script de déploiement AWS pour Solaire Empire
#
# Prérequis:
# - AWS CLI installé et configuré (aws configure)
# - Permissions IAM: S3, CloudFront
#
# Usage:
#   ./aws/deploy.sh [environment]
#
# Exemples:
#   ./aws/deploy.sh production
#   ./aws/deploy.sh staging
################################################################################

set -e  # Exit on error

# Couleurs pour output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
ENVIRONMENT=${1:-production}
PROJECT_NAME="solaire-empire"
REGION="eu-west-3"  # Paris
S3_BUCKET="${PROJECT_NAME}-${ENVIRONMENT}"
SOURCE_DIR="src"
DEPLOY_DIR="dist"

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}   SOLAIRE EMPIRE - Déploiement AWS${NC}"
echo -e "${BLUE}================================================${NC}"
echo -e "${GREEN}Environment: ${ENVIRONMENT}${NC}"
echo -e "${GREEN}Region: ${REGION}${NC}"
echo -e "${GREEN}Bucket S3: ${S3_BUCKET}${NC}\n"

# Vérification AWS CLI
if ! command -v aws &> /dev/null; then
    echo -e "${RED}[ERREUR] AWS CLI n'est pas installé${NC}"
    echo "Installation: https://aws.amazon.com/cli/"
    exit 1
fi

# Vérification credentials AWS
if ! aws sts get-caller-identity &> /dev/null; then
    echo -e "${RED}[ERREUR] AWS credentials non configurées${NC}"
    echo "Exécutez: aws configure"
    exit 1
fi

echo -e "${YELLOW}[1/6] Vérification de l'environnement...${NC}"
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
echo -e "${GREEN}✓ AWS Account: ${ACCOUNT_ID}${NC}"

# Création du bucket S3 si nécessaire
echo -e "\n${YELLOW}[2/6] Configuration du bucket S3...${NC}"
if aws s3 ls "s3://${S3_BUCKET}" 2>&1 | grep -q 'NoSuchBucket'; then
    echo "Création du bucket ${S3_BUCKET}..."
    aws s3 mb "s3://${S3_BUCKET}" --region ${REGION}

    # Configuration du bucket en site web statique
    aws s3 website "s3://${S3_BUCKET}" \
        --index-document index.html \
        --error-document index.html

    # Politique publique pour le bucket
    cat > /tmp/bucket-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::${S3_BUCKET}/*"
    }
  ]
}
EOF
    aws s3api put-bucket-policy \
        --bucket ${S3_BUCKET} \
        --policy file:///tmp/bucket-policy.json

    echo -e "${GREEN}✓ Bucket S3 créé et configuré${NC}"
else
    echo -e "${GREEN}✓ Bucket S3 existe déjà${NC}"
fi

# Build du site
echo -e "\n${YELLOW}[3/6] Build du site...${NC}"
rm -rf ${DEPLOY_DIR}
mkdir -p ${DEPLOY_DIR}

# Copie des fichiers sources
cp -r ${SOURCE_DIR}/* ${DEPLOY_DIR}/

# Copie des données JSON
mkdir -p ${DEPLOY_DIR}/data
mkdir -p ${DEPLOY_DIR}/agents
if [ -f "data/catalogue.json" ]; then
    cp data/catalogue.json ${DEPLOY_DIR}/data/
fi
if [ -f "agents/results_gemini_web.json" ]; then
    cp agents/results_gemini_web.json ${DEPLOY_DIR}/agents/
fi

echo -e "${GREEN}✓ Build terminé${NC}"
echo "Fichiers dans ${DEPLOY_DIR}:"
ls -lh ${DEPLOY_DIR}/

# Upload vers S3
echo -e "\n${YELLOW}[4/6] Upload vers S3...${NC}"
aws s3 sync ${DEPLOY_DIR}/ "s3://${S3_BUCKET}/" \
    --region ${REGION} \
    --delete \
    --cache-control "public, max-age=31536000" \
    --exclude "*.html" \
    --exclude "*.json"

# HTML et JSON sans cache (pour mises à jour immédiates)
aws s3 sync ${DEPLOY_DIR}/ "s3://${S3_BUCKET}/" \
    --region ${REGION} \
    --cache-control "no-cache, no-store, must-revalidate" \
    --include "*.html" \
    --include "*.json"

echo -e "${GREEN}✓ Upload S3 terminé${NC}"

# Configuration CloudFront (optionnel)
echo -e "\n${YELLOW}[5/6] Configuration CloudFront...${NC}"
DISTRIBUTION_ID=$(aws cloudfront list-distributions \
    --query "DistributionList.Items[?Origins.Items[0].DomainName=='${S3_BUCKET}.s3-website.${REGION}.amazonaws.com'].Id" \
    --output text 2>/dev/null || echo "")

if [ -z "$DISTRIBUTION_ID" ]; then
    echo -e "${YELLOW}Aucune distribution CloudFront trouvée${NC}"
    echo "Pour créer une distribution CloudFront:"
    echo "1. Console AWS > CloudFront > Create Distribution"
    echo "2. Origin: ${S3_BUCKET}.s3-website.${REGION}.amazonaws.com"
    echo "3. Default Root Object: index.html"
    echo "4. Error Pages: 403, 404 -> /index.html (200)"
else
    echo -e "${GREEN}✓ Distribution CloudFront: ${DISTRIBUTION_ID}${NC}"
    echo "Invalidation du cache..."
    aws cloudfront create-invalidation \
        --distribution-id ${DISTRIBUTION_ID} \
        --paths "/*" > /dev/null
    echo -e "${GREEN}✓ Cache invalidé${NC}"
fi

# URLs finales
echo -e "\n${YELLOW}[6/6] Déploiement terminé !${NC}"
echo -e "${BLUE}================================================${NC}"
echo -e "${GREEN}✓ Site déployé avec succès${NC}"
echo -e "${BLUE}================================================${NC}\n"

echo "URLs d'accès:"
echo -e "${GREEN}S3 Website:${NC}"
echo "  http://${S3_BUCKET}.s3-website.${REGION}.amazonaws.com"

if [ ! -z "$DISTRIBUTION_ID" ]; then
    CLOUDFRONT_DOMAIN=$(aws cloudfront get-distribution \
        --id ${DISTRIBUTION_ID} \
        --query "Distribution.DomainName" \
        --output text)
    echo -e "\n${GREEN}CloudFront (HTTPS):${NC}"
    echo "  https://${CLOUDFRONT_DOMAIN}"
fi

echo -e "\n${YELLOW}Commandes utiles:${NC}"
echo "  # Logs S3"
echo "  aws s3 ls s3://${S3_BUCKET}/ --recursive --human-readable"
echo ""
echo "  # Supprimer un fichier"
echo "  aws s3 rm s3://${S3_BUCKET}/fichier.html"
echo ""
echo "  # Redéployer"
echo "  ./aws/deploy.sh ${ENVIRONMENT}"

# Nettoyage
rm -f /tmp/bucket-policy.json

echo -e "\n${GREEN}Déploiement terminé ! 🚀${NC}"
