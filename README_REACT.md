# Solaire Empire - Application React avec VideoHero

> Plateforme e-commerce photovoltaïque CdTe avec composant vidéo HD immersif

## 🚀 Démarrage Rapide

```bash
# 1. Installer les dépendances
npm install

# 2. Télécharger les vidéos HD (voir DOWNLOAD_VIDEOS.md)
python scripts/download_videos.py
# OU téléchargement manuel depuis Pexels

# 3. Lancer le serveur de développement
npm run dev
# → http://localhost:5173

# 4. Build pour production
npm run build

# 5. Preview du build
npm run preview
# → http://localhost:4173
```

---

## 📋 Stack Technique

- **Framework** : React 19.2.4
- **Build Tool** : Vite 7.3.1
- **Styling** : CSS3 (vanilla)
- **Vidéos** : HTML5 `<video>` + YouTube embeds
- **Déploiement** : AWS S3 + CloudFront
- **CI/CD** : GitHub Actions

---

## 📦 Structure du Projet

```
immo_pulse/
├── index.html                 # Point d'entrée HTML
├── package.json               # Dépendances et scripts
├── vite.config.js             # Configuration Vite
│
├── src/
│   ├── main.jsx               # Point d'entrée React
│   ├── App.jsx                # Composant racine
│   ├── styles.css             # Styles globaux
│   │
│   ├── components/
│   │   ├── VideoHero.jsx      # Composant vidéo principal ⭐
│   │   └── VideoHero.css      # Styles VideoHero
│   │
│   └── assets/
│       └── videos/            # Vidéos HD locales
│           ├── villa-glass-walls.mp4
│           ├── solar-panels-ground.mp4
│           └── modern-roof-stars.mp4
│
├── agents/
│   └── results_gemini_web.json  # Données vidéos + branding
│
├── data/
│   └── catalogue.json           # Catalogue produits CdTe
│
├── scripts/
│   └── download_videos.py       # Script téléchargement Pexels
│
└── .github/workflows/
    └── deploy-aws.yml           # Déploiement automatique
```

---

## 🎬 Composant VideoHero

### Fonctionnalités

- ✅ **Dual Mode** : Vidéos locales HTML5 + YouTube embeds
- ✅ **Détection automatique** : Analyse l'URL pour choisir le bon lecteur
- ✅ **Contrôles Play/Pause** : Bouton interactif pour vidéos locales
- ✅ **Autoplay conforme** : `muted`, `loop`, `playsInline` (iOS)
- ✅ **Playlist interactive** : Changement de vidéo au clic
- ✅ **Responsive** : Adapté mobile et desktop
- ✅ **SEO optimisé** : Métadonnées structurées

### Usage

```jsx
import VideoHero from './components/VideoHero.jsx'

function App() {
  return <VideoHero />
}
```

### Données Vidéos

Le composant charge automatiquement les données depuis `agents/results_gemini_web.json` :

```json
{
  "videos": [
    {
      "url": "/src/assets/videos/villa-glass-walls.mp4",
      "titre": "Villa Moderne - Panneaux CdTe Intégrés",
      "type": "projet",
      "duree": "30s",
      "isLocal": true
    }
  ],
  "branding": {
    "slogans": ["La Révolution CdTe commence ici"],
    "arguments_vente": ["Prix : -30% vs silicium"]
  }
}
```

---

## 🎥 Vidéos HD

### Spécifications

- **Format** : MP4 (H.264)
- **Résolution** : 1920x1080 minimum
- **Taille** : 5-15 MB par vidéo
- **Durée** : 20-60 secondes
- **Total** : ~30-45 MB (3 vidéos)

### Téléchargement

Voir **`DOWNLOAD_VIDEOS.md`** pour les instructions complètes.

**Option 1 : Script Python**
```bash
pip install requests
python scripts/download_videos.py
```

**Option 2 : Manuel**
- Rechercher sur https://www.pexels.com/videos/
- Télécharger 3 vidéos HD (paysage)
- Placer dans `src/assets/videos/`

---

## 🔧 Scripts Disponibles

```bash
# Développement
npm run dev              # Serveur Vite (http://localhost:5173)

# Production
npm run build            # Build dans dist/
npm run preview          # Preview build (http://localhost:4173)

# Vidéos
python scripts/download_videos.py   # Télécharge vidéos Pexels
```

---

## 🌐 Déploiement AWS

### Configuration

Le déploiement est automatique via GitHub Actions :

1. **Push vers `main`** → Déclenche le workflow
2. **Build Vite** → Génère `dist/`
3. **Upload S3** → Sync avec bucket
4. **CloudFront** → Invalidation cache

### Secrets GitHub Requis

- `AWS_ACCESS_KEY_ID` : Clé IAM AWS
- `AWS_SECRET_ACCESS_KEY` : Secret IAM AWS
- `CLOUDFRONT_DISTRIBUTION_ID` : ID distribution CloudFront (optionnel)

### Workflow

Voir `.github/workflows/deploy-aws.yml`

---

## 📊 Performance

### Build Times
- **Vite build** : ~400ms
- **GitHub Actions** : ~2-3 minutes (total)

### Bundle Sizes
- **JavaScript** : 200 kB (63 kB gzipped)
- **CSS** : 15 kB (3 kB gzipped)
- **HTML** : 0.6 kB
- **Vidéos** : ~30-45 MB

### Lighthouse Scores (Cibles)
- Performance : > 90
- Accessibility : > 95
- Best Practices : > 95
- SEO : > 95

---

## 🛠️ Développement

### Prérequis

- Node.js >= 18
- npm >= 9
- Python 3.x (pour téléchargement vidéos)
- Git

### Installation

```bash
# Clone le repo
git clone https://github.com/Razer750/Solaire_Empire.git
cd Solaire_Empire

# Installe les dépendances
npm install

# Télécharge les vidéos
python scripts/download_videos.py

# Lance le dev server
npm run dev
```

### Workflow de Développement

1. Modifier les fichiers dans `src/`
2. Vite rechargement à chaud automatique
3. Tester dans le navigateur
4. Build pour vérifier : `npm run build`
5. Commit et push vers GitHub

---

## 🎨 Personnalisation

### Changer les Vidéos

1. Modifier `agents/results_gemini_web.json` :
```json
{
  "url": "/src/assets/videos/ma-video.mp4",
  "titre": "Mon Titre",
  "type": "projet",
  "isLocal": true
}
```

2. Placer `ma-video.mp4` dans `src/assets/videos/`

### Changer les Couleurs

Modifier `src/styles.css` :
```css
:root {
  --primary: #FFD700;    /* Or solaire */
  --secondary: #1a1a2e;  /* Bleu foncé */
  --accent: #00D4FF;     /* Bleu tech */
}
```

### Ajouter des Sections

Modifier `src/App.jsx` :
```jsx
function App() {
  return (
    <div className="App">
      <VideoHero />
      <MaNouvelleSection />  {/* Nouveau */}
      {/* ... */}
    </div>
  )
}
```

---

## 🐛 Résolution de Problèmes

### Vidéos ne se chargent pas

```bash
# Vérifier présence des fichiers
ls -la src/assets/videos/

# Vérifier chemins JSON
cat agents/results_gemini_web.json | grep "url"

# Vérifier console navigateur (F12)
```

### Build échoue

```bash
# Vérifier Node.js
node --version  # >= 18

# Nettoyer et réinstaller
rm -rf node_modules package-lock.json dist
npm install
npm run build
```

### Autoplay ne marche pas

- Vérifier `muted` sur `<video>`
- Vérifier `playsInline` (iOS)
- Tester autre navigateur
- Vérifier paramètres navigateur

---

## 📚 Documentation

- **Plan complet** : Voir le plan fourni par l'utilisateur
- **Statut implémentation** : `IMPLEMENTATION_STATUS.md`
- **Guide vidéos** : `DOWNLOAD_VIDEOS.md`
- **Résumé final** : `INTEGRATION_COMPLETE.md`

---

## 🤝 Contribution

1. Fork le projet
2. Créer une branche (`git checkout -b feature/ma-feature`)
3. Commit (`git commit -m 'feat: Ma nouvelle feature'`)
4. Push (`git push origin feature/ma-feature`)
5. Ouvrir une Pull Request

---

## 📄 Licence

ISC

---

## 📧 Contact

- **Repo** : https://github.com/Razer750/Solaire_Empire
- **Issues** : https://github.com/Razer750/Solaire_Empire/issues

---

## 🎯 Roadmap

- [x] Configuration Vite + React
- [x] Intégration VideoHero.jsx
- [x] Support vidéos locales HTML5
- [x] Déploiement AWS automatisé
- [ ] Téléchargement vidéos HD
- [ ] Tests unitaires (React Testing Library)
- [ ] Lazy loading vidéos
- [ ] Poster images (placeholder)
- [ ] Analytics (Google Analytics/Plausible)
- [ ] PWA (Service Worker)

---

**Dernière mise à jour** : 2025-02-12
**Version** : 1.0.0
**Statut** : ✅ Opérationnel (en attente vidéos)
