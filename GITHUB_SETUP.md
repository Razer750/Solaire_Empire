# 🚀 Configuration GitHub - Solaire Empire

## Méthode Rapide (3 minutes)

### Étape 1: Créer le Repository GitHub

1. **Ouvrir** : https://github.com/new

2. **Remplir le formulaire** :

   | Champ | Valeur |
   |-------|--------|
   | **Repository name** | `solaire-empire` |
   | **Description** | Revolution CdTe - Multi-agent solar panels e-commerce platform |
   | **Visibility** | ✅ **Public** (ou Private si préféré) |
   | **Initialize** | ❌ Ne PAS cocher (on a déjà du code) |

3. **Cliquer** : "Create repository"

---

### Étape 2: Connecter et Pousser

Une fois le repo créé, GitHub affichera des instructions. **Ignorer** et utiliser ceci :

```bash
cd C:\Users\razer\Desktop\immo_pulse

# Ajouter le remote GitHub (remplacer USERNAME par votre username GitHub)
git remote add origin https://github.com/USERNAME/solaire-empire.git

# Renommer la branche en main
git branch -M main

# Pousser le code
git push -u origin main
```

**Remplacer `USERNAME`** par votre nom d'utilisateur GitHub.

**Exemple** :
```bash
git remote add origin https://github.com/john-doe/solaire-empire.git
```

---

### Étape 3: Authentification

Si demandé, GitHub demandera vos identifiants :

**Option A : Personal Access Token (Recommandé)**

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Permissions: `repo` (full control)
4. Copier le token
5. Utiliser comme mot de passe lors du push

**Option B : SSH (Alternative)**

```bash
# Générer clé SSH
ssh-keygen -t ed25519 -C "votre@email.com"

# Copier la clé publique
cat ~/.ssh/id_ed25519.pub

# Ajouter sur GitHub: Settings → SSH Keys → New SSH Key
```

Puis utiliser URL SSH :
```bash
git remote set-url origin git@github.com:USERNAME/solaire-empire.git
```

---

## Vérifications Post-Push

### 1. Vérifier sur GitHub

Ouvrir : `https://github.com/USERNAME/solaire-empire`

**Devrait voir** :
- ✅ 33 fichiers
- ✅ README.md ou description
- ✅ Commit initial (80d44be)
- ✅ Dossiers : src/, agents/, aws/, leads/, .github/

### 2. Vérifier GitHub Actions

Aller sur : `https://github.com/USERNAME/solaire-empire/actions`

**Workflow** : `Deploy to AWS`
**Status** : ⚠️ Échouera car secrets AWS non configurés (normal)

---

## Configuration GitHub Actions (CI/CD)

### Ajouter Secrets AWS

1. **Aller sur** : Repository → Settings → Secrets and variables → Actions

2. **Ajouter 3 secrets** :

   | Name | Value | Note |
   |------|-------|------|
   | `AWS_ACCESS_KEY_ID` | `AKIAIOSFODNN...` | Votre Access Key |
   | `AWS_SECRET_ACCESS_KEY` | `wJalrXUtnFEMI...` | Votre Secret Key |
   | `CLOUDFRONT_DISTRIBUTION_ID` | `E1234567890ABC` | Après création CloudFront |

3. **Save** chaque secret

### Obtenir AWS Keys

```bash
# Voir vos credentials
cat ~/.aws/credentials

# Ou créer nouvelles keys
aws iam create-access-key --user-name votre-user
```

---

## Test CI/CD

### Déclencher un Déploiement

```bash
# Faire une modification
echo "# Solaire Empire" > README.md

# Commit
git add README.md
git commit -m "docs: add README

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# Push (déclenche GitHub Actions)
git push
```

**Résultat** :
- GitHub Actions lance le workflow
- Build le site
- Upload vers S3
- Invalide cache CloudFront
- Site mis à jour automatiquement

**Durée** : ~2 minutes

---

## Structure Repository GitHub

```
solaire-empire/
├── .github/
│   └── workflows/
│       └── deploy-aws.yml        # CI/CD automatique
│
├── agents/                       # Scripts multi-agents
│   ├── orchestrator.py
│   ├── leads_generator.py
│   └── ...
│
├── aws/                          # Infrastructure AWS
│   ├── deploy.sh
│   ├── deploy-config.json
│   └── README.md
│
├── src/                          # Site web
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   └── components/
│
├── data/                         # Données business
│   └── catalogue.json
│
├── leads/                        # Prospection
│   ├── argumentaire_vente.md
│   ├── cibles_prioritaires.json
│   └── reels_scripts.md
│
├── .gitignore
├── ARCHITECTURE.md
├── DEPLOY.md
└── README.md (à créer)
```

---

## Créer README.md

### Contenu Suggéré

```markdown
# ⚡ Solaire Empire - Révolution CdTe

> Plateforme e-commerce photovoltaïque avec architecture multi-agents

[![Deploy to AWS](https://github.com/USERNAME/solaire-empire/actions/workflows/deploy-aws.yml/badge.svg)](https://github.com/USERNAME/solaire-empire/actions/workflows/deploy-aws.yml)

## 🌐 Site Live

**URL** : http://solaire-empire-prod.s3-website.eu-west-3.amazonaws.com

## ✨ Features

- 🤖 **Multi-Agent Architecture** (Claude, GPT-4o, Gemini)
- 🎨 **300 Couleurs** Honstar customization
- 🛡️ **Classe A** Certification
- 🏗️ **Reference Projects** : Beijing (50 MWc), Xiongan (200 MWc), Shanghai (80 MWc)
- 📦 **Stock France** (Ivry-sur-Seine)
- 🚀 **CI/CD** avec GitHub Actions
- ☁️ **AWS** S3 + CloudFront

## 🚀 Quick Start

\`\`\`bash
# Clone
git clone https://github.com/USERNAME/solaire-empire.git
cd solaire-empire

# Install dependencies
pip install -r agents/requirements.txt

# Preview locally
./preview.sh  # or preview.bat on Windows

# Deploy to AWS
./aws/deploy.sh production
\`\`\`

## 📊 Architecture

\`\`\`
Claude Sonnet 4.5 (Orchestrator)
    ↓
    ├─→ GPT-4o (PDF extraction)
    ├─→ GPT-4o-mini (Leads generation)
    └─→ Gemini (Web scraping)
         ↓
    Site Web (HTML/CSS/JS)
         ↓
    AWS S3 + CloudFront
\`\`\`

## 🛠️ Tech Stack

- **Frontend** : HTML5, CSS3, Vanilla JavaScript
- **Backend** : Static (AWS S3)
- **Agents** : Python + OpenRouter API
- **Deployment** : AWS CLI + GitHub Actions
- **CI/CD** : Automated via GitHub Actions

## 📝 License

MIT

## 👥 Authors

- Orchestrated by Claude Sonnet 4.5
- Agents: GPT-4o, GPT-4o-mini, Gemini
\`\`\`

---

## Badges GitHub (Optionnel)

Ajouter au README.md :

```markdown
![GitHub last commit](https://img.shields.io/github/last-commit/USERNAME/solaire-empire)
![GitHub repo size](https://img.shields.io/github/repo-size/USERNAME/solaire-empire)
![GitHub language count](https://img.shields.io/github/languages/count/USERNAME/solaire-empire)
![AWS](https://img.shields.io/badge/AWS-S3%20%2B%20CloudFront-orange)
![OpenRouter](https://img.shields.io/badge/OpenRouter-Multi--Agent-blue)
```

---

## Rendre le Repo Privé (Si Nécessaire)

Repository → Settings → Danger Zone → Change visibility → Make private

**Note** : GitHub Actions fonctionne aussi en privé.

---

## Cloner sur Autre Machine

```bash
# Clone
git clone https://github.com/USERNAME/solaire-empire.git
cd solaire-empire

# Install
pip install -r agents/requirements.txt

# Configure AWS (une fois)
aws configure

# Deploy
./aws/deploy.sh production
```

---

## Workflow Git Futur

### Développement Local

```bash
# Créer branche feature
git checkout -b feature/nouvelle-fonctionnalite

# Modifier fichiers
vim src/index.html

# Commit
git add src/
git commit -m "feat: ajout section testimonials"

# Push branche
git push origin feature/nouvelle-fonctionnalite
```

### Pull Request

1. GitHub → Pull Requests → New
2. Comparer feature branch → main
3. Review + Merge

### Déploiement Automatique

Merge sur `main` → GitHub Actions → Deploy AWS automatique

---

## Protections Branch (Recommandé)

Repository → Settings → Branches → Add rule

**Branch name pattern** : `main`

Protections :
- ✅ Require pull request before merging
- ✅ Require status checks to pass (GitHub Actions)
- ✅ Require conversation resolution

---

## Collaborateurs

Repository → Settings → Collaborators → Add people

Inviter par username ou email GitHub.

---

## 📊 Statistiques

Après quelques semaines, voir :

- **Insights** : Commits, contributors, traffic
- **Actions** : Workflow runs, success rate
- **Issues** : Bug tracking
- **Projects** : Kanban board

---

## 🔒 Sécurité

### Secrets à NE JAMAIS Commiter

- ❌ `.claude/settings.local.json` (API keys)
- ❌ `bucket-policy.json` (configs AWS)
- ❌ `.env` files
- ❌ `credentials.json`

**Vérifier** : `.gitignore` les exclut déjà ✅

### Scan Sécurité GitHub

Repository → Security → Enable Dependabot

Scanne automatiquement les vulnérabilités.

---

## 📞 Support

- **Issues** : https://github.com/USERNAME/solaire-empire/issues
- **Discussions** : https://github.com/USERNAME/solaire-empire/discussions
- **Wiki** : https://github.com/USERNAME/solaire-empire/wiki

---

## ✅ Checklist

- [ ] Repository créé sur GitHub
- [ ] Remote ajouté localement
- [ ] Code pushé (git push)
- [ ] README.md créé
- [ ] Secrets AWS configurés (Actions)
- [ ] GitHub Actions testé
- [ ] Repository description ajoutée
- [ ] Topics ajoutés (aws, solar, multi-agent, etc.)
- [ ] License choisie (MIT)
- [ ] .gitignore vérifié

---

**Temps total** : ~5 minutes
**Résultat** : Repository GitHub prêt avec CI/CD automatique
