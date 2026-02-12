# Téléchargement des Vidéos HD

## Option 1 : Script Python Automatique (Recommandé)

### 1. Obtenez votre clé API Pexels (gratuit)

1. Créez un compte sur https://www.pexels.com/
2. Accédez à https://www.pexels.com/api/
3. Cliquez sur "Get started for free"
4. Copiez votre clé API

### 2. Configurez le script

Éditez `scripts/download_videos.py` et remplacez :
```python
PEXELS_API_KEY = "YOUR_API_KEY_HERE"
```

Par votre vraie clé API :
```python
PEXELS_API_KEY = "votre-cle-api-ici"
```

### 3. Installez les dépendances Python

```bash
pip install requests
```

### 4. Lancez le script

```bash
cd C:\Users\razer\Desktop\immo_pulse
python scripts/download_videos.py
```

---

## Option 2 : Téléchargement Manuel

Si vous préférez télécharger manuellement depuis Pexels :

### 1. Villa avec verrières (villa-glass-walls.mp4)

**Recherche sur Pexels** : "luxury villa glass walls modern architecture"

**Critères** :
- Orientation : Paysage (landscape)
- Qualité : HD (1920x1080 minimum)
- Format : MP4
- Durée : 20-60 secondes
- Taille cible : 5-15 MB

**Télécharger dans** : `src/assets/videos/villa-glass-walls.mp4`

**Alternatives de recherche** :
- "modern glass house architecture"
- "luxury villa transparent walls"
- "contemporary architecture glass facade"

---

### 2. Panneaux solaires au sol (solar-panels-ground.mp4)

**Recherche sur Pexels** : "solar panels ground field installation"

**Critères** :
- Orientation : Paysage
- Qualité : HD (1920x1080 minimum)
- Format : MP4
- Durée : 20-60 secondes
- Taille cible : 5-15 MB

**Télécharger dans** : `src/assets/videos/solar-panels-ground.mp4`

**Alternatives de recherche** :
- "solar farm field panels"
- "ground mounted solar installation"
- "solar panel array outdoor"

---

### 3. Toit moderne sous les étoiles (modern-roof-stars.mp4)

**Recherche sur Pexels** : "modern roof architecture night stars"

**Critères** :
- Orientation : Paysage
- Qualité : HD (1920x1080 minimum)
- Format : MP4
- Durée : 20-60 secondes
- Taille cible : 5-15 MB

**Télécharger dans** : `src/assets/videos/modern-roof-stars.mp4`

**Alternatives de recherche** :
- "modern building roof night sky"
- "architecture night stars timelapse"
- "rooftop night sky modern"

---

## Option 3 : Utiliser des Vidéos de Stock Alternatives

Si Pexels ne donne pas de bons résultats, essayez :

- **Pixabay** : https://pixabay.com/videos/ (gratuit, sans attribution)
- **Videvo** : https://www.videvo.net/ (gratuit, certains nécessitent attribution)
- **Coverr** : https://coverr.co/ (gratuit, sans attribution)

---

## Optimisation (si fichiers trop lourds > 20MB)

Si vos vidéos sont trop volumineuses, optimisez-les avec ffmpeg :

```bash
# Installer ffmpeg (Windows)
# Téléchargez depuis: https://ffmpeg.org/download.html

# Optimiser une vidéo
ffmpeg -i villa-glass-walls-original.mp4 \
  -c:v libx264 -crf 23 -preset medium \
  -c:a aac -b:a 128k \
  -movflags +faststart \
  villa-glass-walls.mp4
```

**Paramètres** :
- `-crf 23` : Qualité (18-28, plus bas = meilleure qualité)
- `-preset medium` : Vitesse de compression
- `-movflags +faststart` : Optimise pour streaming web

---

## Vérification

Une fois les 3 vidéos téléchargées, vérifiez :

```bash
ls -lh src/assets/videos/
```

Vous devriez voir :
```
villa-glass-walls.mp4    (5-15 MB)
solar-panels-ground.mp4  (5-15 MB)
modern-roof-stars.mp4    (5-15 MB)
```

**Total cible** : 30-45 MB

---

## Prochaines Étapes

Une fois les vidéos en place :

1. ✅ Vidéos téléchargées dans `src/assets/videos/`
2. ⏭️ Continuer avec l'installation de Vite React
3. ⏭️ Tester les vidéos localement avec `npm run dev`
