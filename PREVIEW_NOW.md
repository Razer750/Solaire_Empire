# 🚀 PRÉVISUALISER LE SITE IMMÉDIATEMENT

## ⚡ Méthode Express (Recommandée)

### Windows
Double-cliquez sur :
```
preview.bat
```

### Mac / Linux
```bash
./preview.sh
```

**Durée** : 3 secondes
**Résultat** : Navigateur s'ouvre automatiquement sur http://localhost:8000

---

## 📱 Méthode Manuelle

### Option 1: Python (Recommandé)
```bash
cd C:\Users\razer\Desktop\immo_pulse\src
python -m http.server 8000
```

Puis ouvrir : http://localhost:8000

### Option 2: Node.js
```bash
cd C:\Users\razer\Desktop\immo_pulse\src
npx http-server -p 8000
```

### Option 3: PHP
```bash
cd C:\Users\razer\Desktop\immo_pulse\src
php -S localhost:8000
```

---

## ✅ Checklist Visuelle

Une fois le site ouvert, vérifiez :

### Header Hero
- [ ] Titre glitch "LA RÉVOLUTION CdTe" animé
- [ ] Sous-titre : **"300 Couleurs • Classe A Honstar • Stock France"**
- [ ] 4 stats :
  - [ ] **-30%** Prix vs Silicium
  - [ ] **300** Couleurs disponibles
  - [ ] **Classe A** Certification Honstar
  - [ ] **30 ans** Garantie
- [ ] 2 boutons CTA :
  - [ ] **📞 Demander un Devis Gratuit** (pulse animé)
  - [ ] **📦 Voir le Catalogue**
- [ ] Badges confiance :
  - [ ] ✓ Stock permanent Ivry (94)
  - [ ] ✓ Livraison 48h
  - [ ] ✓ Support 7j/7

### Section Révolution CdTe
- [ ] 4 cartes arguments (Économique, Performant, Esthétique, Écologique)
- [ ] Tableau comparatif CdTe vs Silicium
- [ ] Messages clés visibles

### Section Projets Références
- [ ] **3 projets affichés** :
  - [ ] **Pékin Olympic Stadium** (50 MWc)
  - [ ] **Xiongan Smart City** (200 MWc)
  - [ ] **Shanghai Industrial Park** (80 MWc)
- [ ] Chaque projet montre :
  - [ ] Nom + Puissance
  - [ ] Localisation avec 📍
  - [ ] Technologie CdTe
  - [ ] Highlights avec ✓
  - [ ] Année

### Section Catalogue Produits
- [ ] **2 produits** affichés (Honstar + Longyan)
- [ ] Chaque produit montre :
  - [ ] **Badge "Classe A"** (Honstar uniquement) 🛡️
  - [ ] **Badge "300 Couleurs"** 🎨
  - [ ] Badge "Stock France 🇫🇷"
  - [ ] Technologie **CdTe**
  - [ ] Specs : Puissance, Rendement, Dimensions, Garantie
  - [ ] Mention : **"300 couleurs disponibles"**
  - [ ] Prix HT
  - [ ] Arguments (badges)
  - [ ] Bouton **"📞 Demander un devis"**

### Section Vidéos Projets
- [ ] 5 vidéos affichées
- [ ] Thumbnails YouTube ou placeholders
- [ ] Hover effect (play overlay)
- [ ] Types : reel, projet, demo, tutoriel

### Section Contact
- [ ] Formulaire complet (Nom, Email, Téléphone, Type projet, Message)
- [ ] Bouton **"Demander un devis"**
- [ ] Texte : "Stock permanent Ivry-sur-Seine (94) • Livraison 48h"

---

## 🎨 Éléments Visuels à Vérifier

### Couleurs
- [ ] Or solaire (#FFD700) pour titres/CTA
- [ ] Bleu tech (#00D4FF) pour accents
- [ ] Fond dark (#0f0f1e, #1a1a2e, #2a1a3e)
- [ ] Dégradés animés

### Animations
- [ ] Titre glitch (effet text-shadow)
- [ ] Bouton CTA pulse (animation)
- [ ] Cartes hover (lift effect)
- [ ] Parallax hero au scroll
- [ ] Fade in au scroll (cartes)

### Responsive
- [ ] Tester en mode mobile (F12 > Toggle Device)
- [ ] Navigation verticale sur mobile
- [ ] Cartes empilées (1 colonne)

---

## 🔧 Dépannage

### Le serveur ne démarre pas
```bash
# Vérifier Python
python --version

# Si pas installé, télécharger:
# https://www.python.org/downloads/
```

### Le navigateur ne s'ouvre pas
Ouvrir manuellement : http://localhost:8000

### Port 8000 déjà utilisé
```bash
# Utiliser un autre port
python -m http.server 8001

# Ou tuer le processus
# Windows: taskkill /F /IM python.exe
# Mac/Linux: pkill python
```

### Erreurs console (F12)
- Vérifier que `data/catalogue.json` existe
- Vérifier que `agents/results_gemini_web.json` existe
- Recharger avec Ctrl+F5 (hard refresh)

### Styles ne s'appliquent pas
```bash
# Hard refresh
Ctrl + F5 (Windows/Linux)
Cmd + Shift + R (Mac)
```

---

## 📊 Test Performance

### Lighthouse (F12 > Lighthouse)
Objectifs :
- [ ] Performance : >90
- [ ] Accessibility : >90
- [ ] Best Practices : >90
- [ ] SEO : >90

### Temps de chargement
- [ ] First Contentful Paint : <1.5s
- [ ] Time to Interactive : <3s

---

## 📱 Test Multi-Navigateurs

- [ ] Chrome / Edge (Chromium)
- [ ] Firefox
- [ ] Safari (Mac)
- [ ] Mobile (Chrome Android / Safari iOS)

---

## 🎯 Interactions à Tester

### Clicks
1. **Cliquer sur "📞 Demander un Devis"**
   - [ ] Scroll vers formulaire
   - [ ] Focus sur formulaire

2. **Cliquer sur "📦 Voir le Catalogue"**
   - [ ] Scroll vers section catalogue
   - [ ] Smooth scroll

3. **Cliquer sur carte vidéo**
   - [ ] Vidéo YouTube s'affiche
   - [ ] Ou placeholder si pas d'URL

4. **Remplir formulaire + Submit**
   - [ ] Bouton change : "⏳ Envoi en cours..."
   - [ ] Puis : "✓ Demande envoyée !"
   - [ ] Formulaire se reset après 2s

### Hover
- [ ] Cartes produits (lift effect)
- [ ] Cartes projets (lift + glow)
- [ ] Vidéos (play overlay apparaît)
- [ ] Boutons CTA (scale + shadow)

### Scroll
- [ ] Hero parallax (contenu remonte)
- [ ] Cartes fade in (apparition progressive)
- [ ] Smooth scroll (ancres)

---

## 📸 Screenshots Recommandés

Pour validation avant prod :
1. Hero complet (desktop)
2. Section projets (Pékin, Xiongan, Shanghai)
3. Catalogue avec badges (Classe A, 300 couleurs)
4. Formulaire contact
5. Version mobile (responsive)

---

## ✅ Validation Finale

### Données Catalogue
- [x] **300 couleurs** : Mentionné dans hero + badge + specs produits
- [x] **Classe A Honstar** : Badge visible sur produit Honstar
- [x] **CdTe** : Technologie affichée partout (hero, projets, catalogue)
- [x] **Stock Ivry (94)** : Mentionné hero + catalogue + formulaire
- [x] **Prix -30%** : Stat hero + arguments

### Projets Références
- [x] **Pékin** : Olympic Stadium 50 MWc
- [x] **Xiongan** : Smart City 200 MWc BIPV
- [x] **Shanghai** : Industrial Park 80 MWc

### CTA Marketing
- [x] Bouton principal hero : "📞 Demander un Devis Gratuit"
- [x] Animation pulse pour attirer attention
- [x] Redirect vers formulaire contact
- [x] Capture leads (Nom, Email, Téléphone, Type, Message)

---

## 🚀 Commande Ultime

```bash
# Tout en 1 ligne (Windows)
cd C:\Users\razer\Desktop\immo_pulse && preview.bat

# Tout en 1 ligne (Mac/Linux)
cd ~/Desktop/immo_pulse && ./preview.sh
```

---

**Temps de preview** : 3 secondes
**URL** : http://localhost:8000
**Arrêter** : Ctrl+C dans le terminal

🎉 **Site prêt à être prévisualisé !**
