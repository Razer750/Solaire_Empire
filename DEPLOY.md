# 🚀 GUIDE DE DÉPLOIEMENT - SOLAIRE EMPIRE

## Vue d'ensemble

Ce document vous guide pour déployer Solaire Empire sur AWS avec l'infrastructure complète.

---

## 📋 Checklist Pré-Déploiement

### Fichiers Requis
- [x] `src/index.html` - Page principale
- [x] `src/styles.css` - Styles
- [x] `src/app.js` - Logique frontend
- [x] `src/components/VideoHero.js` - Composant vidéo
- [x] `src/components/VideoHero.css` - Styles vidéo
- [x] `data/catalogue.json` - Catalogue produits (GPT-4o)
- [x] `agents/results_gemini_web.json` - Données vidéos (Gemini)

### Configuration AWS
- [ ] AWS CLI installé
- [ ] Credentials configurées (`aws configure`)
- [ ] Permissions IAM (S3, CloudFront)
- [ ] Région: eu-west-3 (Paris)

---

## 🎯 Méthodes de Déploiement

### Option 1: Script Automatique (Recommandé)

```bash
# 1. Rendre le script exécutable
chmod +x aws/deploy.sh

# 2. Déployer
./aws/deploy.sh production
```

**Durée**: ~2 minutes
**Résultat**: Site déployé sur S3 + CloudFront (si configuré)

---

### Option 2: GitHub Actions (CI/CD)

#### Configuration Secrets

1. Aller sur GitHub > Settings > Secrets > New repository secret
2. Ajouter:
   - `AWS_ACCESS_KEY_ID`: Votre access key AWS
   - `AWS_SECRET_ACCESS_KEY`: Votre secret key AWS
   - `CLOUDFRONT_DISTRIBUTION_ID`: ID distribution CloudFront (optionnel)

#### Déclenchement

```bash
# Push sur main déclenche automatiquement le déploiement
git add .
git commit -m "Deploy: Solaire Empire v1.0"
git push origin main
```

**Durée**: ~3 minutes
**Résultat**: Déploiement automatique à chaque push

---

### Option 3: Manuelle (Console AWS)

#### Étape 1: Créer Bucket S3

1. Console AWS > S3 > Create Bucket
2. Nom: `solaire-empire-prod`
3. Région: `eu-west-3` (Paris)
4. Décocher "Block all public access"
5. Create Bucket

#### Étape 2: Configurer Website Hosting

1. Bucket > Properties > Static website hosting
2. Enable
3. Index document: `index.html`
4. Error document: `index.html`
5. Save

#### Étape 3: Politique Publique

Bucket > Permissions > Bucket Policy:

```json
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
```

#### Étape 4: Upload Fichiers

```bash
# Build
mkdir -p dist/data dist/agents dist/components
cp -r src/* dist/
cp data/catalogue.json dist/data/
cp agents/results_gemini_web.json dist/agents/

# Upload via Console
# Bucket > Upload > Add files > Upload
# Ou via CLI:
aws s3 sync dist/ s3://solaire-empire-prod/ --delete
```

#### Étape 5: CloudFront (Optionnel mais Recommandé)

1. Console AWS > CloudFront > Create Distribution
2. **Origin**:
   - Origin Domain: `solaire-empire-prod.s3-website.eu-west-3.amazonaws.com`
   - Protocol: HTTP only
3. **Default Cache Behavior**:
   - Viewer Protocol: Redirect HTTP to HTTPS
   - Allowed Methods: GET, HEAD, OPTIONS
   - Compress: Yes
4. **Settings**:
   - Price Class: Use Only North America and Europe
   - Default Root Object: `index.html`
5. **Custom Error Responses**:
   - Add: 403 → /index.html (200)
   - Add: 404 → /index.html (200)
6. Create Distribution

**Durée**: ~15 minutes (propagation CloudFront)

---

## 🧪 Test Local Avant Déploiement

```bash
# Test complet
./aws/test-local.sh

# Ou serveur simple
cd src && python -m http.server 8000
```

Ouvrir: http://localhost:8000

**Vérifications**:
- [ ] Page principale s'affiche
- [ ] Vidéos chargent (VideoHero)
- [ ] Catalogue produits affiché
- [ ] Formulaire contact fonctionne
- [ ] Styles appliqués correctement
- [ ] Console sans erreurs (F12)

---

## 📊 URLs Post-Déploiement

### S3 Website (HTTP)
```
http://solaire-empire-prod.s3-website.eu-west-3.amazonaws.com
```

### CloudFront (HTTPS)
```
https://d1234567890abc.cloudfront.net
```
*(ID unique généré par CloudFront)*

### Custom Domain (après config Route53)
```
https://solaire-empire.fr
https://www.solaire-empire.fr
```

---

## 🔄 Mises à Jour

### Méthode Rapide
```bash
# Redéployer tout
./aws/deploy.sh production
```

### Mise à jour Partielle
```bash
# Upload un fichier spécifique
aws s3 cp src/index.html s3://solaire-empire-prod/

# Invalider cache CloudFront
aws cloudfront create-invalidation \
  --distribution-id E1234567890ABC \
  --paths "/index.html"
```

### Via Git (si CI/CD actif)
```bash
git add .
git commit -m "Update: amélioration VideoHero"
git push origin main
# → Déploiement automatique
```

---

## 💰 Coûts

### Estimation Mensuelle

**Trafic Faible** (1k visiteurs/mois):
- S3: $0.10
- CloudFront: $1.00
- **Total: ~$1/mois**

**Trafic Modéré** (10k visiteurs/mois):
- S3: $0.50
- CloudFront: $10.00
- Route53: $1.00
- **Total: ~$12/mois**

**Trafic Élevé** (100k visiteurs/mois):
- S3: $1.00
- CloudFront: $85.00
- Route53: $10.00
- **Total: ~$96/mois**

**Note**: Les 12 premiers mois, AWS Free Tier offre:
- 5 GB S3 storage
- 50 GB CloudFront transfer
- = Site quasi gratuit la 1ère année !

---

## 🔐 Sécurité

### Headers HTTP (CloudFront Functions)
```javascript
function handler(event) {
    var response = event.response;
    response.headers = {
        'strict-transport-security': { value: 'max-age=31536000' },
        'x-content-type-options': { value: 'nosniff' },
        'x-frame-options': { value: 'DENY' },
        'x-xss-protection': { value: '1; mode=block' }
    };
    return response;
}
```

### SSL/TLS
- CloudFront: Certificat gratuit (auto-généré)
- Custom Domain: AWS Certificate Manager (ACM) gratuit

---

## 🐛 Troubleshooting

### Erreur 403 Forbidden
**Cause**: Bucket policy non configurée
**Solution**:
```bash
aws s3api put-bucket-policy \
  --bucket solaire-empire-prod \
  --policy file://aws/bucket-policy.json
```

### Fichiers ne s'affichent pas
**Cause**: Cache CloudFront
**Solution**:
```bash
aws cloudfront create-invalidation \
  --distribution-id E1234567890ABC \
  --paths "/*"
```

### Erreur AWS CLI
**Cause**: Credentials non configurées
**Solution**:
```bash
aws configure
# Entrer Access Key ID + Secret Access Key
```

### Vidéos ne chargent pas
**Cause**: CORS non configuré
**Solution**: Console S3 > Bucket > Permissions > CORS:
```json
[{
  "AllowedOrigins": ["*"],
  "AllowedMethods": ["GET", "HEAD"],
  "AllowedHeaders": ["*"],
  "MaxAgeSeconds": 3600
}]
```

---

## 📞 Support

### Documentation AWS
- [S3 Static Website](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)
- [CloudFront](https://docs.aws.amazon.com/cloudfront/)
- [Route53](https://docs.aws.amazon.com/route53/)

### Commandes Debug
```bash
# Test S3 endpoint
curl -I http://solaire-empire-prod.s3-website.eu-west-3.amazonaws.com

# Test CloudFront
curl -I https://d1234567890abc.cloudfront.net

# Vérifier DNS (si custom domain)
nslookup solaire-empire.fr
dig solaire-empire.fr
```

---

## ✅ Checklist Post-Déploiement

- [ ] Site accessible via URL S3
- [ ] HTTPS fonctionne (CloudFront)
- [ ] VideoHero affiche les vidéos
- [ ] Catalogue produits chargé
- [ ] Formulaire contact opérationnel
- [ ] Console navigateur sans erreurs
- [ ] Test sur mobile (responsive)
- [ ] Performance: Lighthouse score >90
- [ ] SEO: Meta tags présents
- [ ] Analytics configuré (Google Analytics)

---

## 🎯 Prochaines Étapes

1. **Domaine Custom**: Acheter solaire-empire.fr sur Route53
2. **SSL Custom**: Certificat ACM (gratuit)
3. **Analytics**: Google Analytics / Plausible
4. **Monitoring**: CloudWatch Alarms
5. **Backup**: Versioning S3 activé
6. **CDN Avancé**: Geo-restriction si besoin
7. **WAF**: Protection DDoS (optionnel, +$5/mois)

---

**Infrastructure**: AWS S3 + CloudFront + Route53
**Région**: eu-west-3 (Paris)
**Coût**: ~$12/mois (trafic modéré)
**Latence**: <50ms Europe, <200ms Global
**Disponibilité**: 99.99% SLA

🚀 **Prêt pour la production !**
