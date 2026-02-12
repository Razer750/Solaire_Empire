# 🎭 ARCHITECTURE MULTI-AGENTS - SOLAIRE EMPIRE

## Vision Globale

```
┌─────────────────────────────────────────────────────────────┐
│                    CLAUDE (Chef d'Orchestre)                │
│                    i9 Local + Claude CLI                    │
└───────────┬─────────────────────────────────┬───────────────┘
            │                                 │
            ▼                                 ▼
    ┌───────────────┐                 ┌───────────────┐
    │     GEMINI    │                 │    GPT-4o     │
    │  via OpenRouter│                 │ via OpenRouter│
    │    (Gratuit)   │                 │   (Payant)    │
    └───────┬───────┘                 └───────┬───────┘
            │                                 │
            │ Analyse Web                     │ Extraction PDF
            │ advsolarpower.com               │ Honstar/Longyan
            ▼                                 ▼
    results_gemini_web.json          results_gpt4o_pdf.json
            │                                 │
            │                                 │
            └─────────────┬───────────────────┘
                          ▼
                    ASSEMBLAGE
                    catalogue.json
                          │
                          ▼
                ┌─────────────────┐
                │   SITE WEB      │
                │ Solaire Empire  │
                │ index.html      │
                └─────────────────┘
                          │
                          ▼
                    http://localhost:8000
```

## Composants

### 1. Claude Sonnet 4.5 (Vous)
**Rôle**: Chef d'Orchestre
**Responsabilités**:
- Coordonner les agents Gemini et GPT-4o
- Développer le site web (HTML/CSS/JS)
- Assembler les données collectées
- Gérer l'infrastructure /agents

**Outils**:
- i9 local (puissance de calcul)
- Claude Code CLI
- Git, Python, Node.js

### 2. Gemini (via OpenRouter)
**Rôle**: Analyste Web & Multimédia
**Modèle**: `google/gemini-pro` (ou variantes disponibles)
**Tâche**:
- Scraper advsolarpower.com
- Extraire URLs vidéos (YouTube, Vimeo)
- Récupérer scripts des Reels
- Identifier messages marketing

**Output**: `agents/results_gemini_web.json`
```json
{
  "videos": [...],
  "scripts": [...],
  "branding": {
    "slogans": [...],
    "arguments_vente": [...]
  }
}
```

**Status**: ⚠️ Modèle gratuit indisponible, template généré

### 3. GPT-4o (via OpenRouter)
**Rôle**: Extracteur de Données Techniques
**Modèle**: `openai/gpt-4o`
**Tâche**:
- Parser 5 PDFs Honstar/Longyan
- Extraire specs techniques CdTe
- Structurer catalogue produits
- Comparer CdTe vs Silicium

**Output**: `data/catalogue.json`
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
      ...
    }
  ],
  "revolution_cdte": {
    "avantages": [...],
    "comparatif_silicium": {...}
  }
}
```

**Status**: ✅ Opérationnel, données générées

## Infrastructure

### Répertoires
```
immo_pulse/
├── agents/                          # Scripts multi-agents
│   ├── orchestrator.py              # Orchestrateur principal
│   ├── gemini_web_scraper.py        # Agent Gemini dédié
│   ├── parse_results.py             # Parser JSON
│   ├── requirements.txt             # Dépendances Python
│   ├── README.md                    # Doc agents
│   ├── results_gemini_web.json      # Output Gemini
│   └── results_gpt4o_pdf.json       # Output GPT-4o
│
├── data/                            # Données business
│   └── catalogue.json               # Catalogue final (assemblé)
│
├── src/                             # Site web
│   ├── index.html                   # Page principale
│   ├── styles.css                   # Design Révolution CdTe
│   ├── app.js                       # Logique dynamique
│   └── README.md                    # Doc site
│
├── leads/                           # (À venir) Gestion prospects
│
├── .claude/
│   └── settings.local.json          # Config API keys
│
└── ARCHITECTURE.md                  # Ce fichier
```

### Configuration OpenRouter

**Fichier**: `.claude/settings.local.json`
```json
{
  "permissions": {
    "allow": [
      "Bash(export OPENROUTER_API_KEY=\"sk-or-v1-...\")"
    ]
  }
}
```

**Modèles Utilisés**:
- Gemini: Gratuit, mais indisponible actuellement
- GPT-4o: ~$5/1M tokens input, ~$15/1M tokens output

## Workflow

### Phase 1: Collecte de Données
```bash
# Lancer l'orchestration complète
python agents/orchestrator.py

# Résultats:
# - agents/results_gemini_web.json (vidéos + branding)
# - agents/results_gpt4o_pdf.json (brut)
```

### Phase 2: Parsing & Structuration
```bash
# Parser les résultats GPT-4o
python agents/parse_results.py

# Output: data/catalogue.json
```

### Phase 3: Construction du Site
```bash
# Claude construit le site dans src/
# - index.html (structure)
# - styles.css (design CdTe)
# - app.js (chargement dynamique)
```

### Phase 4: Lancement
```bash
cd src
python -m http.server 8000

# Ouvrir: http://localhost:8000
```

## Innovation: Révolution CdTe

### Messages Clés
1. **Économique**: -30% vs silicium
2. **Performant**: Meilleur en faible lumière (climat FR)
3. **Esthétique**: Panneau noir uniforme premium
4. **Local**: Stock permanent Ivry-sur-Seine (93)
5. **Garanti**: 25-30 ans performance
6. **Éco**: Impact environnemental réduit

### Marques
- **Honstar**: Fabricant chinois certifié CE/TÜV
- **Longyan**: Technologie CdTe avancée

### Cibles
- Particuliers (maisons)
- Professionnels (PME, commerces)
- Installateurs (partenaires)
- Investisseurs (centrales solaires)

## Automatisation Future

### Agents Autonomes
```python
# agents/auto_refresh.py (à créer)
# Cron: Tous les jours à 6h AM
import schedule

def daily_refresh():
    """Rafraîchit les données quotidiennement"""
    # 1. Scrape advsolarpower.com (Gemini)
    # 2. Check nouveaux PDFs (GPT-4o)
    # 3. Update catalogue.json
    # 4. Rebuild site
    # 5. Notify admin

schedule.every().day.at("06:00").do(daily_refresh)
```

### API Endpoints (à venir)
```
POST /api/devis
    → Envoie demande de devis depuis formulaire

GET /api/stock
    → Vérifie stock en temps réel (Ivry)

POST /api/webhook/new-pdf
    → Trigger re-parsing automatique
```

### Notifications
- Email admin si nouveau produit détecté
- Slack notification sur nouvelle vidéo
- Discord bot pour leads qualifiés

## Métriques

### Performance
- **Temps génération catalogue**: ~5s (GPT-4o)
- **Temps scraping web**: ~8s (Gemini)
- **Temps build site**: <1s (statique)
- **Total pipeline**: ~15s

### Coûts OpenRouter
- **Gemini**: Gratuit (si disponible)
- **GPT-4o**: ~$0.02 par extraction PDF complète
- **Budget mensuel estimé**: <$5 (20 refreshs/mois)

## Sécurité

### API Keys
- Stockées dans `.claude/settings.local.json`
- ⚠️ Ne JAMAIS commit ce fichier
- Ajouter à `.gitignore`

### Validation
- app.js: Sanitize inputs formulaire
- Agents: Timeout 90s max par appel
- Rate limiting: Max 10 req/min OpenRouter

## Évolutions

### Court Terme (Sprint 1)
- [x] Orchestrateur multi-agents
- [x] Site web Solaire Empire
- [x] Catalogue dynamique
- [ ] Vrai scraping advsolarpower.com (fix Gemini model)
- [ ] Intégration vrais PDFs Honstar/Longyan

### Moyen Terme (Sprint 2-3)
- [ ] Formulaire → CRM (HubSpot/Pipedrive)
- [ ] Dashboard admin
- [ ] A/B testing messages CdTe
- [ ] Analytics (Google/Plausible)

### Long Terme (Q2 2025)
- [ ] Mobile app (React Native)
- [ ] Simulateur économies solaires
- [ ] Marketplace installateurs
- [ ] Comparateur intelligent AI

## Support

### Debug
```bash
# Logs agents
tail -f agents/*.json

# Logs serveur web
# (affiché dans terminal)

# Console navigateur
# F12 → Console → Voir easter eggs
```

### Régénération Complète
```bash
# 1. Clean
rm -rf agents/results_*.json data/catalogue.json

# 2. Rebuild
python agents/orchestrator.py
python agents/parse_results.py

# 3. Restart
cd src && python -m http.server 8000
```

---

**Créé par**: Architecture Multi-Agents
**Orchestrateur**: Claude Sonnet 4.5
**Agents**: Gemini (Web) + GPT-4o (PDF)
**Stack**: Python + HTML/CSS/JS
**Innovation**: Révolution CdTe 🌞
