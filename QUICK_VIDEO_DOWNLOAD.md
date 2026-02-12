# 🎬 Téléchargement Rapide des Vidéos (5 minutes)

## Option 1 : Vidéos Mixkit (Recommandé - Plus facile)

### Étape 1 : Télécharger les 3 vidéos

**Vidéo 1 - Panneaux Solaires** (obligatoire)
1. Ouvrir: https://mixkit.co/free-stock-video/solar-panels-in-a-field-4323/
2. Cliquer sur **"Free Download"**
3. Choisir **"HD 1920x1080"**
4. Enregistrer dans `C:\Users\razer\Desktop\immo_pulse\src\assets\videos\`
5. Renommer en: **`solar-panels-ground.mp4`**

**Vidéo 2 - Architecture Moderne** (obligatoire)
1. Ouvrir: https://mixkit.co/free-stock-video/modern-building-glass-facade-4320/
2. Cliquer sur **"Free Download"**
3. Choisir **"HD 1920x1080"**
4. Enregistrer dans `C:\Users\razer\Desktop\immo_pulse\src\assets\videos\`
5. Renommer en: **`villa-glass-walls.mp4`**

**Vidéo 3 - Ciel Étoilé** (obligatoire)
1. Ouvrir: https://mixkit.co/free-stock-video/starry-night-sky-time-lapse-4223/
2. Cliquer sur **"Free Download"**
3. Choisir **"HD 1920x1080"**
4. Enregistrer dans `C:\Users\razer\Desktop\immo_pulse\src\assets\videos\`
5. Renommer en: **`modern-roof-stars.mp4`**

---

## Option 2 : Vidéos Pexels (Meilleure qualité)

Si vous préférez des vidéos plus spécifiques aux panneaux solaires :

**Vidéo 1 - Panneaux Solaires**
- https://www.pexels.com/video/solar-panels-in-a-solar-farm-7989411/
- Cliquer "Free Download" → HD → Renommer: `solar-panels-ground.mp4`

**Vidéo 2 - Architecture**
- https://www.pexels.com/video/modern-architecture-3044967/
- Cliquer "Free Download" → HD → Renommer: `villa-glass-walls.mp4`

**Vidéo 3 - Nuit Étoilée**
- https://www.pexels.com/video/milky-way-2387611/
- Cliquer "Free Download" → HD → Renommer: `modern-roof-stars.mp4`

---

## Vérification

Une fois les 3 vidéos téléchargées, vérifier avec :

```bash
ls -lh C:\Users\razer\Desktop\immo_pulse\src\assets\videos\*.mp4
```

Vous devriez voir :
```
villa-glass-walls.mp4
solar-panels-ground.mp4
modern-roof-stars.mp4
```

---

## Étape Suivante

Une fois les 3 vidéos en place, exécuter :

```bash
cd C:\Users\razer\Desktop\immo_pulse
npm run dev
```

Ouvrir http://localhost:5173 pour voir le résultat !

---

## Déploiement sur AWS

Quand tout fonctionne localement :

```bash
git add .
git commit -m "feat: Add local HD videos for VideoHero

- Add 3 HD videos (villa, solar panels, stars)
- Configure VideoHero.jsx for local video playback
- Update results_gemini_web.json with local URLs

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

git push origin main
```

Le workflow GitHub Actions déploiera automatiquement sur AWS !

---

## Temps Estimé

- Téléchargement vidéo 1 : 30 sec
- Téléchargement vidéo 2 : 30 sec
- Téléchargement vidéo 3 : 30 sec
- Renommage : 1 min
- Test local : 1 min

**Total : ~3-4 minutes** ⚡
