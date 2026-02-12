# Vidéos HD pour VideoHero

Ce répertoire contient les 3 vidéos HD utilisées par le composant VideoHero.

## Fichiers requis

1. **villa-glass-walls.mp4** - Villa avec verrières transparentes
2. **solar-panels-ground.mp4** - Installation de panneaux solaires au sol
3. **modern-roof-stars.mp4** - Toit moderne sous les étoiles

## Téléchargement

Voir les instructions détaillées dans : `../../DOWNLOAD_VIDEOS.md`

### Méthode rapide

```bash
# Avec le script Python (recommandé)
cd ../../../
python scripts/download_videos.py

# OU téléchargement manuel depuis Pexels
# https://www.pexels.com/videos/
```

## Spécifications

- **Format** : MP4 (H.264)
- **Résolution** : 1920x1080 minimum (HD)
- **Taille** : 5-15 MB par vidéo (optimisé pour le web)
- **Durée** : 20-60 secondes
- **Orientation** : Paysage (landscape)

## Optimisation

Si vos vidéos sont trop lourdes (> 20MB), utilisez ffmpeg :

```bash
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k -movflags +faststart output.mp4
```

## Vérification

Une fois les 3 vidéos en place :

```bash
ls -lh *.mp4
# Devrait afficher les 3 fichiers avec des tailles entre 5-15 MB
```

## Utilisation dans le code

Les vidéos sont référencées dans `agents/results_gemini_web.json` :

```json
{
  "url": "/src/assets/videos/villa-glass-walls.mp4",
  "titre": "Villa Moderne - Panneaux CdTe Intégrés",
  "isLocal": true
}
```

Le composant `VideoHero.js` détecte automatiquement les vidéos locales et utilise `<video>` HTML5 au lieu de YouTube embed.
