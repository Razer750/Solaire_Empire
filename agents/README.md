# 🎭 Agents Multi-Modèles - Solaire Empire

## Architecture

```
Claude (Chef d'Orchestre)
   ↓
   ├─→ Gemini 2.0 Flash (via OpenRouter)
   │   └─→ Analyse Web: advsolarpower.com
   │       ├─ URLs vidéos
   │       ├─ Scripts Reels
   │       └─ Messages marketing
   │
   └─→ GPT-4o (via OpenRouter)
       └─→ Vérification PDF: Honstar/Longyan
           ├─ Extraction catalogue produits
           ├─ Specs techniques CdTe
           └─→ OUTPUT: data/catalogue.json
```

## Utilisation

### Lancement automatique
```bash
python agents/orchestrator.py
```

### Résultats attendus
- `agents/results_gemini_web.json` - Analyse du site concurrent
- `agents/results_gpt4o_pdf.json` - Extraction des PDFs
- `data/catalogue.json` - Catalogue structuré prêt pour le site

## Agents

### 🔹 Gemini 2.0 Flash (Gratuit)
- **Spécialité**: Scraping web, analyse de contenu multimédia
- **Modèle**: `google/gemini-2.0-flash-exp:free`
- **Tâche**: Extraire vidéos et scripts de advsolarpower.com

### 🔸 GPT-4o (Payant, haute précision)
- **Spécialité**: Extraction de données techniques, parsing PDF
- **Modèle**: `openai/gpt-4o`
- **Tâche**: Structurer les 5 PDF en catalogue.json

### ⚡ Claude Sonnet 4.5 (Local via CLI)
- **Spécialité**: Orchestration, développement web, intégration
- **Tâche**: Assembler le site Solaire Empire avec les données collectées

## Innovation CdTe

Le site doit mettre en avant:
- ⚡ **Moins cher** que le silicium
- ✨ **Plus esthétique** (panneau noir uniforme)
- 🇫🇷 **Stock en France** (Ivry-sur-Seine)
- 🔬 **Technologie CdTe** (Telluride de Cadmium) nouvelle génération

## Configuration OpenRouter

Clé API déjà configurée dans `.claude/settings.local.json`
- Gemini: Gratuit, illimité
- GPT-4o: ~$5/1M tokens (budget contrôlé)
