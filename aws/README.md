# 🚀 Déploiement AWS - Solaire Empire

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    UTILISATEURS                         │
└───────────────────┬─────────────────────────────────────┘
                    │
                    ▼
        ┌──────────────────────┐
        │   Route 53 (DNS)     │  solaire-empire.fr
        │   (Optionnel)        │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │   CloudFront (CDN)   │  HTTPS, Cache Global
        │   + SSL Certificate  │  Latence réduite
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │   S3 Bucket          │  solaire-empire-prod
        │   (Static Website)   │  src/* + data/* + agents/*
        │   eu-west-3 (Paris)  │
        └──────────────────────┘
```

## Prérequis

### 1. AWS CLI
```bash
# Installation (Windows)
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi

# Installation (Mac/Linux)
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Vérification
aws --version
```

### 2. Configuration AWS
```bash
aws configure
# AWS Access Key ID: AKIAIOSFODNN7EXAMPLE
# AWS Secret Access Key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
# Default region name: eu-west-3
# Default output format: json
```

### 3. Permissions IAM
Votre utilisateur AWS doit avoir ces permissions:
- `s3:*` (S3 full access)
- `cloudfront:*` (CloudFront full access)
- `route53:*` (Route53 - optionnel)

## Déploiement Rapide

### Déploiement Complet
```bash
# Rendre le script exécutable
chmod +x aws/deploy.sh

# Déployer en production
./aws/deploy.sh production

# Ou en staging
./aws/deploy.sh staging
```

### Étapes Manuelles

#### 1. Créer le bucket S3
```bash
aws s3 mb s3://solaire-empire-prod --region eu-west-3
```

#### 2. Configurer le bucket en website
```bash
aws s3 website s3://solaire-empire-prod \
  --index-document index.html \
  --error-document index.html
```

#### 3. Rendre le bucket public
```bash
cat > bucket-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "PublicReadGetObject",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::solaire-empire-prod/*"
  }]
}
EOF

aws s3api put-bucket-policy \
  --bucket solaire-empire-prod \
  --policy file://bucket-policy.json
```

#### 4. Build et upload
```bash
# Build
rm -rf dist && mkdir -p dist
cp -r src/* dist/
cp data/catalogue.json dist/data/
cp agents/results_gemini_web.json dist/agents/

# Upload
aws s3 sync dist/ s3://solaire-empire-prod/ \
  --delete \
  --cache-control "public, max-age=31536000"
```

#### 5. Créer distribution CloudFront (Console AWS)
1. Console AWS > CloudFront > Create Distribution
2. **Origin**:
   - Origin Domain: `solaire-empire-prod.s3-website.eu-west-3.amazonaws.com`
   - Protocol: HTTP only (S3 website endpoint)
3. **Default Cache Behavior**:
   - Viewer Protocol Policy: Redirect HTTP to HTTPS
   - Allowed HTTP Methods: GET, HEAD, OPTIONS
   - Compress Objects: Yes
4. **Settings**:
   - Price Class: Use Only North America and Europe
   - Default Root Object: `index.html`
5. **Custom Error Responses**:
   - 403 → /index.html (200)
   - 404 → /index.html (200)

## Structure Déployée

```
s3://solaire-empire-prod/
├── index.html
├── styles.css
├── app.js
├── components/
│   ├── VideoHero.js
│   └── VideoHero.css
├── data/
│   └── catalogue.json
└── agents/
    └── results_gemini_web.json
```

## URLs

### S3 Website
```
http://solaire-empire-prod.s3-website.eu-west-3.amazonaws.com
```

### CloudFront (après création)
```
https://d1234567890abc.cloudfront.net
```

### Custom Domain (après Route53)
```
https://solaire-empire.fr
https://www.solaire-empire.fr
```

## Commandes Utiles

### Gestion S3

```bash
# Lister les fichiers
aws s3 ls s3://solaire-empire-prod/ --recursive --human-readable

# Télécharger un fichier
aws s3 cp s3://solaire-empire-prod/index.html ./

# Supprimer un fichier
aws s3 rm s3://solaire-empire-prod/old-file.js

# Vider le bucket (ATTENTION)
aws s3 rm s3://solaire-empire-prod/ --recursive
```

### Gestion CloudFront

```bash
# Lister les distributions
aws cloudfront list-distributions \
  --query "DistributionList.Items[*].[Id,DomainName,Status]" \
  --output table

# Invalider le cache (après update)
aws cloudfront create-invalidation \
  --distribution-id E1234567890ABC \
  --paths "/*"

# Invalider un fichier spécifique
aws cloudfront create-invalidation \
  --distribution-id E1234567890ABC \
  --paths "/index.html" "/data/catalogue.json"
```

### Monitoring

```bash
# Logs S3 (activer d'abord dans Console)
aws s3 ls s3://solaire-empire-prod-logs/

# Métriques CloudFront
aws cloudwatch get-metric-statistics \
  --namespace AWS/CloudFront \
  --metric-name Requests \
  --dimensions Name=DistributionId,Value=E1234567890ABC \
  --start-time 2025-02-01T00:00:00Z \
  --end-time 2025-02-12T23:59:59Z \
  --period 86400 \
  --statistics Sum
```

## Configuration Domaine Custom

### 1. Acheter domaine (Route53 ou externe)
```bash
# Vérifier disponibilité
aws route53domains check-domain-availability \
  --domain-name solaire-empire.fr

# Acheter (si disponible)
aws route53domains register-domain \
  --domain-name solaire-empire.fr \
  --duration-in-years 1 \
  --auto-renew \
  --admin-contact file://contact.json \
  --registrant-contact file://contact.json \
  --tech-contact file://contact.json
```

### 2. Certificat SSL (ACM)
```bash
# Demander certificat (doit être en us-east-1 pour CloudFront)
aws acm request-certificate \
  --domain-name solaire-empire.fr \
  --subject-alternative-names www.solaire-empire.fr \
  --validation-method DNS \
  --region us-east-1

# Valider via DNS (suivre instructions email)
```

### 3. Configurer CloudFront avec domaine
Console AWS > CloudFront > Edit Distribution:
- **Alternate Domain Names (CNAMEs)**: solaire-empire.fr, www.solaire-empire.fr
- **SSL Certificate**: Custom SSL (sélectionner certificat ACM)

### 4. Créer records Route53
```bash
# Créer hosted zone
aws route53 create-hosted-zone \
  --name solaire-empire.fr \
  --caller-reference $(date +%s)

# Pointer vers CloudFront (Alias record)
# Via Console AWS > Route53 > Create Record
# Type: A - IPv4 address
# Alias: Yes
# Alias Target: CloudFront distribution
```

## CI/CD avec GitHub Actions

### .github/workflows/deploy.yml
```yaml
name: Deploy to AWS

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Configure AWS Credentials
      uses: aws-actions/configure-aws-credentials@v1
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: eu-west-3

    - name: Build
      run: |
        mkdir -p dist
        cp -r src/* dist/
        cp data/catalogue.json dist/data/
        cp agents/results_gemini_web.json dist/agents/

    - name: Deploy to S3
      run: |
        aws s3 sync dist/ s3://solaire-empire-prod/ --delete

    - name: Invalidate CloudFront
      run: |
        aws cloudfront create-invalidation \
          --distribution-id ${{ secrets.CLOUDFRONT_DISTRIBUTION_ID }} \
          --paths "/*"
```

### Secrets GitHub
Settings > Secrets > New repository secret:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `CLOUDFRONT_DISTRIBUTION_ID`

## Coûts Estimés

### Trafic Modéré (10k visiteurs/mois)

| Service | Usage | Coût USD/mois |
|---------|-------|---------------|
| **S3** | 1 GB stockage + 100k requêtes | $0.50 |
| **CloudFront** | 100 GB transfer + 1M requêtes | $10.00 |
| **Route53** | 1 hosted zone + 1M queries | $1.00 |
| **ACM (SSL)** | Certificat SSL | Gratuit |
| **Total** | | **~$12/mois** |

### Trafic Élevé (100k visiteurs/mois)

| Service | Usage | Coût USD/mois |
|---------|-------|---------------|
| **S3** | 1 GB stockage + 1M requêtes | $1.00 |
| **CloudFront** | 1 TB transfer + 10M requêtes | $85.00 |
| **Route53** | 1 hosted zone + 10M queries | $10.00 |
| **Total** | | **~$96/mois** |

## Sécurité

### Headers de sécurité (CloudFront Functions)
```javascript
function handler(event) {
    var response = event.response;
    response.headers = {
        ...response.headers,
        'strict-transport-security': { value: 'max-age=31536000' },
        'x-content-type-options': { value: 'nosniff' },
        'x-frame-options': { value: 'DENY' },
        'x-xss-protection': { value: '1; mode=block' }
    };
    return response;
}
```

### WAF (Web Application Firewall) - Optionnel
```bash
# Créer Web ACL
aws wafv2 create-web-acl \
  --name solaire-empire-waf \
  --scope CLOUDFRONT \
  --default-action Allow={} \
  --region us-east-1

# Associer à CloudFront
aws wafv2 associate-web-acl \
  --web-acl-arn arn:aws:wafv2:us-east-1:ACCOUNT:global/webacl/... \
  --resource-arn arn:aws:cloudfront::ACCOUNT:distribution/E123...
```

Coût WAF: ~$5/mois + $1 par million de requêtes

## Rollback

### Revenir à version précédente
```bash
# Lister les versions (si versioning activé)
aws s3api list-object-versions \
  --bucket solaire-empire-prod \
  --prefix index.html

# Restaurer version spécifique
aws s3api copy-object \
  --bucket solaire-empire-prod \
  --copy-source solaire-empire-prod/index.html?versionId=VERSION_ID \
  --key index.html
```

## Support

### Debug
```bash
# Tester S3 website
curl -I http://solaire-empire-prod.s3-website.eu-west-3.amazonaws.com

# Tester CloudFront
curl -I https://d1234567890abc.cloudfront.net

# Vérifier DNS
dig solaire-empire.fr
nslookup solaire-empire.fr
```

### Logs
- **S3 Access Logs**: Console > S3 > Bucket > Properties > Server access logging
- **CloudFront Logs**: Console > CloudFront > Distribution > Logs

---

**Infrastructure**: AWS (S3 + CloudFront)
**Région**: eu-west-3 (Paris)
**CDN**: CloudFront Global
**Coût**: ~$12/mois (trafic modéré)
**Latence**: <50ms (Europe), <200ms (Global)

🚀 **Prêt pour la production !**
