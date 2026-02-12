# ⚠️ Configuration CloudFront - Vérification Compte Requise

## Situation Actuelle

Votre compte AWS nécessite une **vérification** avant de créer des ressources CloudFront.

**Message d'erreur** :
```
Your account must be verified before you can add new CloudFront resources.
```

C'est une **protection standard AWS** pour les nouveaux comptes (prévention fraude/abus).

---

## 🔓 Solution 1: Vérifier le Compte AWS

### Étapes

1. **Contacter AWS Support**
   - URL: https://console.aws.amazon.com/support/home
   - Ouvrir un ticket "Account and Billing Support"

2. **Message à envoyer** :
   ```
   Subject: Request to enable CloudFront for account 112158171430

   Hello AWS Support,

   I would like to enable CloudFront distributions on my AWS account.
   I received the error "Your account must be verified before you can add new CloudFront resources."

   Account ID: 112158171430
   Use Case: Static website hosting (Solaire Empire)
   Region: eu-west-3 (Paris)

   Please verify my account to enable CloudFront.

   Thank you.
   ```

3. **Délai de réponse**
   - Support Basic (gratuit) : 24-48h
   - Support Developer (payant) : 12-24h
   - Support Business (payant) : 1h

### Une fois vérifié

```bash
# Créer la distribution
aws cloudfront create-distribution \
  --distribution-config file://cloudfront-config.json
```

---

## 🚀 Solution 2: Configuration Manuelle (Console AWS)

En attendant la vérification CLI, vous pouvez créer la distribution via Console Web.

### Étapes Détaillées

#### 1. Ouvrir Console CloudFront
https://console.aws.amazon.com/cloudfront/v4/home

#### 2. Create Distribution

**Bouton** : "Create Distribution"

#### 3. Origin Settings

| Paramètre | Valeur |
|-----------|--------|
| **Origin Domain** | `solaire-empire-prod.s3-website.eu-west-3.amazonaws.com` |
| **Protocol** | HTTP only |
| **Name** | `S3-solaire-empire-prod` |

⚠️ **IMPORTANT** : Utilisez l'endpoint **website** (avec `.s3-website.`), PAS l'endpoint REST API.

#### 4. Default Cache Behavior

| Paramètre | Valeur |
|-----------|--------|
| **Viewer Protocol Policy** | Redirect HTTP to HTTPS |
| **Allowed HTTP Methods** | GET, HEAD, OPTIONS |
| **Compress Objects** | Yes |
| **Cache Policy** | CachingOptimized (ou créer custom) |

#### 5. Settings

| Paramètre | Valeur |
|-----------|--------|
| **Price Class** | Use Only North America and Europe |
| **Default Root Object** | `index.html` |
| **Description** | Solaire Empire - Revolution CdTe |

#### 6. Custom Error Responses

Après création, ajouter 2 error responses :

**Error Response 1** :
- HTTP Error Code: **403**
- Customize Error Response: **Yes**
- Response Page Path: `/index.html`
- HTTP Response Code: **200**

**Error Response 2** :
- HTTP Error Code: **404**
- Customize Error Response: **Yes**
- Response Page Path: `/index.html`
- HTTP Response Code: **200**

#### 7. Create Distribution

**Bouton** : "Create Distribution"

**Temps de propagation** : 15-20 minutes

---

## 🌐 Après Création

### Récupérer l'URL CloudFront

```bash
# Lister les distributions
aws cloudfront list-distributions \
  --query "DistributionList.Items[*].[Id,DomainName,Status]" \
  --output table
```

### URL Format
```
https://d1234567890abc.cloudfront.net
```

### Tester
```bash
curl -I https://d1234567890abc.cloudfront.net
```

### Invalider le Cache (après mises à jour)

```bash
# Obtenir l'ID de distribution
DIST_ID=$(aws cloudfront list-distributions \
  --query "DistributionList.Items[?Origins.Items[0].DomainName=='solaire-empire-prod.s3-website.eu-west-3.amazonaws.com'].Id" \
  --output text)

# Invalider tout le cache
aws cloudfront create-invalidation \
  --distribution-id $DIST_ID \
  --paths "/*"
```

---

## 💰 Coûts CloudFront

### Trafic Modéré (10k visiteurs/mois)

| Service | Usage | Coût USD/mois |
|---------|-------|---------------|
| **Data Transfer Out** | 100 GB | $8.50 |
| **HTTP Requests** | 1M requêtes | $1.00 |
| **HTTPS Requests** | Inclus | $0.00 |
| **Invalidations** | 1000/mois gratuit | $0.00 |
| **Total** | | **~$10/mois** |

### Free Tier (12 mois)

| Service | Inclus Gratuit |
|---------|----------------|
| **Data Transfer Out** | 50 GB/mois |
| **HTTP/HTTPS Requests** | 2M requêtes/mois |

→ **Site quasi gratuit 1ère année !**

---

## 🔧 Configuration Avancée (Optionnel)

### Custom Domain

1. **Acheter domaine** : solaire-empire.fr
2. **Créer certificat SSL** (ACM us-east-1)
   ```bash
   aws acm request-certificate \
     --domain-name solaire-empire.fr \
     --subject-alternative-names www.solaire-empire.fr \
     --validation-method DNS \
     --region us-east-1
   ```

3. **Valider certificat** (via DNS records)

4. **Ajouter CNAME à CloudFront**
   - Alternate Domain Names: `solaire-empire.fr`, `www.solaire-empire.fr`
   - SSL Certificate: Custom (sélectionner certificat ACM)

5. **Configurer Route53**
   ```bash
   # Créer hosted zone
   aws route53 create-hosted-zone \
     --name solaire-empire.fr \
     --caller-reference $(date +%s)
   ```

6. **Créer Alias Record** (A) vers CloudFront

### Cache Policies Custom

Console CloudFront > Policies > Cache Policies > Create

**Settings Optimisés** :
- TTL Min: 0
- TTL Default: 86400 (24h)
- TTL Max: 31536000 (1 an)
- Gzip: Enabled
- Brotli: Enabled

### Response Headers Policy

Ajouter headers de sécurité :
```
Strict-Transport-Security: max-age=31536000
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Referrer-Policy: strict-origin-when-cross-origin
```

---

## 📊 Monitoring CloudFront

### Métriques CloudWatch

```bash
# Requêtes totales (24h)
aws cloudwatch get-metric-statistics \
  --namespace AWS/CloudFront \
  --metric-name Requests \
  --dimensions Name=DistributionId,Value=$DIST_ID \
  --start-time $(date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 3600 \
  --statistics Sum

# Taux d'erreur 4xx
aws cloudwatch get-metric-statistics \
  --namespace AWS/CloudFront \
  --metric-name 4xxErrorRate \
  --dimensions Name=DistributionId,Value=$DIST_ID \
  --start-time $(date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 3600 \
  --statistics Average
```

### Logs Access

1. Console S3 > Create Bucket : `solaire-empire-logs`
2. CloudFront > Distribution > Edit
3. Logging: On
4. S3 Bucket: `solaire-empire-logs`
5. Log Prefix: `cloudfront/`

---

## 🔄 Workflow Déploiement avec CloudFront

### 1. Mise à jour fichiers
```bash
cd /c/Users/razer/Desktop/immo_pulse
cp -r src/* dist/
```

### 2. Upload S3
```bash
aws s3 sync dist/ s3://solaire-empire-prod/ --delete
```

### 3. Invalider cache CloudFront
```bash
aws cloudfront create-invalidation \
  --distribution-id $DIST_ID \
  --paths "/*"
```

**Temps total** : 2-3 minutes

---

## 🚨 Troubleshooting

### Distribution en cours de déploiement
**Status** : "In Progress"
**Solution** : Attendre 15-20 minutes

### Erreur 403 Forbidden
**Cause** : Origin mal configuré
**Solution** : Vérifier endpoint S3 **website** (pas REST API)

### Cache non mis à jour
**Solution** : Invalider cache
```bash
aws cloudfront create-invalidation \
  --distribution-id $DIST_ID \
  --paths "/*"
```

### SSL Certificate Error
**Cause** : Certificat pas en us-east-1
**Solution** : Recréer certificat ACM en us-east-1

---

## 📋 Checklist Configuration

### Création Distribution
- [ ] Compte AWS vérifié (ou via Console)
- [ ] Origin: endpoint S3 **website**
- [ ] Protocol: HTTP only (origin)
- [ ] Viewer Protocol: Redirect to HTTPS
- [ ] Compress: Enabled
- [ ] Default Root Object: index.html
- [ ] Error Responses: 403/404 → /index.html

### Post-Configuration
- [ ] Distribution déployée (Status: Deployed)
- [ ] URL CloudFront testée
- [ ] HTTPS fonctionne
- [ ] Site accessible
- [ ] Cache configuré
- [ ] Invalidation testée

### Optionnel
- [ ] Custom domain configuré
- [ ] Certificat SSL ACM
- [ ] Route53 records
- [ ] Monitoring activé
- [ ] Logs configurés

---

## 🎯 État Actuel

| Étape | Status | Action Requise |
|-------|--------|----------------|
| S3 Bucket | ✅ Déployé | Aucune |
| S3 Website | ✅ En ligne | Aucune |
| CloudFront | ⏸️ En attente | Vérification compte AWS |
| Custom Domain | ⏸️ À venir | Acheter domaine |

---

## 🚀 Solution Temporaire (Sans CloudFront)

En attendant la vérification, votre site est **déjà accessible** via S3 :

```
http://solaire-empire-prod.s3-website.eu-west-3.amazonaws.com
```

**Fonctionnalités disponibles** :
- ✅ Site complet accessible
- ✅ Toutes les pages fonctionnent
- ✅ Formulaire contact OK
- ✅ Vidéos + Projets affichés
- ⚠️ Pas de HTTPS (HTTP uniquement)
- ⚠️ Latence plus élevée (pas de CDN)

**Performance** :
- Europe : <100ms ✅
- USA : ~200ms ⚠️
- Asie : ~300ms ⚠️

---

## 📞 Contact AWS Support

### Créer Ticket Support

1. https://console.aws.amazon.com/support/home
2. Create Case
3. Type: Account and Billing Support
4. Category: Account
5. Subject: "Enable CloudFront for account 112158171430"
6. Description: (voir message ci-dessus)

### Support Options

| Plan | Coût | Réponse | Accès |
|------|------|---------|-------|
| **Basic** | Gratuit | 24-48h | Billing only |
| **Developer** | $29/mois | 12-24h | Tech support |
| **Business** | $100/mois | <1h | 24/7 tech |

**Recommandation** : Basic (gratuit) suffit pour ce cas.

---

## ✅ Résumé

**CloudFront** : ⏸️ En attente vérification compte
**S3 Website** : ✅ Opérationnel
**URL Active** : http://solaire-empire-prod.s3-website.eu-west-3.amazonaws.com
**Action Immédiate** : Contacter AWS Support
**Alternative** : Configuration manuelle via Console (peut fonctionner)

**Temps estimé vérification** : 24-48h

🎯 **Le site est déjà en ligne et fonctionnel sur S3 !**
