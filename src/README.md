# Solaire Empire - Site Web

## 🚀 Lancement

```bash
# Option 1: Serveur Python
cd src
python -m http.server 8000

# Option 2: Serveur Node (si disponible)
npx http-server src -p 8000

# Puis ouvrir: http://localhost:8000
```

## 📁 Structure

```
src/
├── index.html      # Page principale
├── styles.css      # Design Révolution CdTe
├── app.js          # Logique dynamique (charge data/)
└── README.md       # Ce fichier

data/
└── catalogue.json  # Généré par GPT-4o (agents/)

agents/
├── orchestrator.py         # Chef d'orchestre multi-agents
├── results_gemini_web.json # Vidéos analysées par Gemini
└── results_gpt4o_pdf.json  # PDFs traités par GPT-4o
```

## 🎨 Design

### Palette de couleurs
- **Or Solaire** (#FFD700): CTA, highlights, prix
- **Bleu Tech** (#00D4FF): Accents, technologie
- **Noir Profond** (#0f0f1e): Background principal
- **Violet Obscur** (#2a1a3e): Dégradés, cartes

### Typographie
- Headers: Bold, uppercase, glitch effect
- Body: Segoe UI (Windows), SF Pro (macOS fallback)

### Animations
- Hero parallax au scroll
- Cartes produits hover avec lift
- Glitch effect sur titre principal

## 🧠 Logique Multi-Agents

### 1. Gemini (Analyse Web)
```python
# agents/gemini_web_scraper.py
analyse_advsolarpower() → results_gemini_web.json
```
**Output**: URLs vidéos, scripts Reels, branding

### 2. GPT-4o (Extraction PDF)
```python
# agents/orchestrator.py
delegate_pdf_verification() → results_gpt4o_pdf.json → catalogue.json
```
**Output**: Catalogue produits Honstar/Longyan structuré

### 3. Claude (Orchestration + Dev)
- Coordonne Gemini + GPT-4o
- Construit le site web
- Assemble les données dynamiquement

## 📊 Données

### catalogue.json (Source: GPT-4o)
```json
{
  "produits": [
    {
      "ref": "HS-1234",
      "marque": "Honstar",
      "puissance_w": 150,
      "technologie": "CdTe",
      "prix_ht": 100,
      "stock_france": true,
      "specs": {...},
      "arguments": [...]
    }
  ],
  "revolution_cdte": {
    "avantages": [...],
    "comparatif_silicium": {...}
  }
}
```

### results_gemini_web.json (Source: Gemini)
```json
{
  "videos": [
    {"url": "...", "titre": "...", "type": "reel/demo/tutoriel"}
  ],
  "scripts": [...],
  "branding": {...}
}
```

## 🎯 Messages Clés

### Arguments CdTe vs Silicium
1. **Prix**: -30% moins cher
2. **Performance**: Meilleur en faible lumière (climat FR)
3. **Esthétique**: Noir uniforme premium
4. **Garantie**: 25-30 ans (vs 20-25 pour silicium)
5. **Éco**: Impact environnemental réduit
6. **Stock**: Disponible à Ivry-sur-Seine (93)

### Cibles
- **Particuliers**: Maisons, rénovation énergétique
- **Professionnels**: PME, commerces, entrepôts
- **Installateurs**: Réseau partenaires
- **Investisseurs**: Projets photovoltaïques

## 🔧 Maintenance

### Mettre à jour le catalogue
```bash
# 1. Modifier/ajouter PDFs dans data/
# 2. Relancer l'agent GPT-4o
python agents/orchestrator.py

# 3. Parser les résultats
python agents/parse_results.py

# 4. Recharger le site (F5)
```

### Ajouter des vidéos
1. Éditer `agents/results_gemini_web.json`
2. Ajouter dans `results[0].videos`
3. Format: `{"url": "...", "titre": "...", "type": "..."}`

## 🚀 Déploiement

### Netlify / Vercel (Statique)
```bash
# Build: Aucun (site statique)
# Publish directory: src/
# Base directory: /
```

### GitHub Pages
```bash
git init
git add .
git commit -m "Revolution CdTe"
git branch -M main
git remote add origin <repo>
git push -u origin main

# Activer Pages dans Settings → Pages → Source: main/root
```

## 📱 Responsive
- Desktop: Grid 3 colonnes (produits)
- Tablet: Grid 2 colonnes
- Mobile: Grid 1 colonne
- Navigation mobile: Vertical stack

## 🎭 Easter Eggs
- Message console stylisé (F12 pour voir)
- Glitch animation sur titre H1
- Parallax hero au scroll
- Hover effects 3D sur cartes

---

**Généré par**: Architecture Multi-Agents (Claude + Gemini + GPT-4o)
**Stack**: HTML5 + CSS3 + Vanilla JS (zero dependencies)
**Innovation**: Révolution CdTe • Stock France • -30% prix
