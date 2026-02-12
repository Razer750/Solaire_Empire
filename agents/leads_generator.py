#!/usr/bin/env python3
"""
Agent GPT-4o-mini pour génération de contenu LEADS
Centre nerveux de la prospection Solaire Empire
"""

import json
import requests

OPENROUTER_API_KEY = "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"
OPENROUTER_BASE = "https://openrouter.ai/api/v1/chat/completions"

def call_gpt4o_mini(task, system_prompt="Tu es un expert en vente et marketing solaire."):
    """Appel à GPT-4o-mini via OpenRouter"""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Solaire Empire - Leads Generator"
    }

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": task}
    ]

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": messages,
        "temperature": 0.8,  # Plus créatif pour le marketing
        "max_tokens": 3000
    }

    print("[GPT-4o-mini] Appel en cours...")
    response = requests.post(OPENROUTER_BASE, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        content = result['choices'][0]['message']['content']
        print(f"[GPT-4o-mini] [OK] Reponse recue ({len(content)} caracteres)")
        return content
    else:
        print(f"[GPT-4o-mini] [ERREUR] {response.status_code}: {response.text}")
        return None

def generate_argumentaire_vente():
    """Génère l'argumentaire de vente"""
    task = """
MISSION: Créer un script de vente PERCUTANT pour Solaire Empire

CONTEXTE:
- Technologie CdTe de Longyan (Telluride de Cadmium)
- Certification Classe A de Honstar (sécurité maximale)
- Stock IMMÉDIAT à Ivry-sur-Seine (94)
- Prix: -30% vs silicium traditionnel
- Performance: Meilleur rendement en faible luminosité
- Esthétique: Panneau noir uniforme premium

PUBLIC CIBLE:
- Architectes (BIPV - Building Integrated PhotoVoltaics)
- Promoteurs immobiliers
- Installateurs RGE
- Entreprises (toitures commerciales/industrielles)

STRUCTURE DEMANDÉE:

# 1. ACCROCHE (30 secondes)
[Phrase choc qui capte l'attention]

# 2. PROBLÈME (1 minute)
[Les douleurs du marché actuel: Prix élevés, délais, esthétique]

# 3. SOLUTION CdTe (2 minutes)
[Innovation Longyan, Classe A Honstar, Stock Ivry]

# 4. PREUVE (1 minute)
[Chiffres, certifications, garanties]

# 5. URGENCE (30 secondes)
[Pourquoi acheter MAINTENANT]

# 6. CALL-TO-ACTION (30 secondes)
[Action immédiate demandée]

TON: Professionnel, confiant, disruptif (style "on révolutionne le marché")
LONGUEUR: 5 minutes de pitch complet
FORMAT: Markdown avec sections claires
"""

    result = call_gpt4o_mini(task, "Tu es un sales engineer expert en photovoltaïque avec 15 ans d'expérience.")

    if result:
        with open("leads/argumentaire_vente.md", 'w', encoding='utf-8') as f:
            f.write(result)
        print("[OK] leads/argumentaire_vente.md cree!")
        return True
    return False

def generate_cibles_prioritaires():
    """Génère la liste des cibles prioritaires"""
    task = """
MISSION: Créer une liste STRUCTURÉE des cibles prioritaires pour Solaire Empire

CONTEXTE:
- Produit: Panneaux solaires CdTe (Honstar/Longyan)
- Avantages: -30% prix, meilleur faible lumière, esthétique, stock Ivry
- Marché: France, focus Île-de-France (proximité stock)

CIBLES À INCLURE:

1. ARCHITECTES
   - Cabinets spécialisés BIPV
   - Bureaux d'études énergétiques
   - Architectes HQE/BREEAM

2. PROMOTEURS IMMOBILIERS
   - Logement neuf (RE2020)
   - Rénovation énergétique
   - Immobilier tertiaire

3. INSTALLATEURS RGE
   - Électriciens QualiPV
   - Couvreurs + solaire
   - Entreprises générales bâtiment

4. ENTREPRISES B2B
   - PME/ETI avec toitures
   - Centres commerciaux
   - Entrepôts logistiques
   - Agriculteurs (hangars)

5. COLLECTIVITÉS
   - Mairies (bâtiments publics)
   - Bailleurs sociaux
   - Zones d'activités

POUR CHAQUE CIBLE, FOURNIS:
{
  "categorie": "...",
  "sous_types": [...],
  "pain_points": [...],  // Leurs problèmes
  "notre_solution": "...",  // Comment on les résout
  "arguments_cles": [...],  // Top 3 arguments pour eux
  "decision_makers": "...",  // Qui contacter (titre)
  "budget_moyen": "...",  // Budget projet typique
  "cycle_vente": "...",  // Court/Moyen/Long
  "priorite": 1-5  // 5 = très prioritaire
}

RETOURNE un JSON structuré et complet.
"""

    result = call_gpt4o_mini(task, "Tu es un expert en business development pour le secteur photovoltaïque.")

    if result:
        # Nettoie le JSON (retire les backticks markdown si présents)
        clean_result = result.strip()
        if clean_result.startswith('```json'):
            clean_result = clean_result[7:]
        if clean_result.startswith('```'):
            clean_result = clean_result[3:]
        if clean_result.endswith('```'):
            clean_result = clean_result[:-3]
        clean_result = clean_result.strip()

        try:
            # Valide que c'est du JSON correct
            data = json.loads(clean_result)

            with open("leads/cibles_prioritaires.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print("[OK] leads/cibles_prioritaires.json cree!")
            return True
        except json.JSONDecodeError:
            # Sauvegarde en markdown si le JSON est invalide
            with open("leads/cibles_prioritaires.json", 'w', encoding='utf-8') as f:
                f.write(clean_result)
            print("[WARN] JSON invalide, sauvegarde brute effectuee")
            return True
    return False

def generate_reels_scripts():
    """Génère 3 scripts de Reels TikTok"""
    task = """
MISSION: Créer 3 scripts de REELS/TikTok de 30 secondes pour Solaire Empire

OBJECTIF: Pousser les gens à laisser leurs coordonnées sur le site pour un devis

CONTRAINTES:
- Durée: 30 secondes EXACTEMENT
- Format: Vertical (9:16)
- Hook: 3 premières secondes CRUCIALES
- CTA: Clair et actionnable
- Ton: Disruptif, provocateur, "on casse les codes"

CONTEXTE PRODUIT:
- Panneaux CdTe (Honstar/Longyan)
- -30% moins cher que le silicium
- Noir uniforme (ultra esthétique)
- Stock France (Ivry) = livraison rapide
- Meilleur rendement faible lumière

ANGLES À EXPLOITER:

REEL #1: "Le Secret des Panneaux Noirs"
- Hook: "Pourquoi les riches choisissent TOUJOURS les panneaux noirs ?"
- Body: Comparaison esthétique Silicium (moche) vs CdTe (classe)
- CTA: "Devis gratuit sur Solaire-Empire.fr"

REEL #2: "Stock France VS Chine"
- Hook: "6 mois d'attente pour des panneaux chinois ? On a mieux."
- Body: Stock à Ivry = livraison en 48h
- CTA: "Réserve ton stock maintenant"

REEL #3: "Le Calcul qui Tue"
- Hook: "Ton électricien te vend du silicium 30% trop cher"
- Body: Calcul économies sur 25 ans avec CdTe
- CTA: "Devis comparatif gratuit"

POUR CHAQUE SCRIPT, FOURNIS:

## Reel #[N] : [Titre accrocheur]

**Durée**: 30s

**Visuel suggéré**:
[Description plan par plan: 0-3s, 4-10s, 11-20s, 21-30s]

**Script voix-off**:
[Texte EXACT à dire, chronométré]

**Texte écran** (overlays):
[Textes qui apparaissent à l'écran avec timing]

**Musique**:
[Genre/ambiance suggérée]

**Call-to-Action final**:
[Texte exact + bouton/lien]

**Hashtags**:
[5-8 hashtags pertinents]

TON: Dynamique, énergique, "anti-système"
OBJECTIF: Minimum 50 leads/semaine par reel
FORMAT: Markdown structuré
"""

    result = call_gpt4o_mini(task, "Tu es un créateur de contenu viral TikTok spécialisé en B2C/B2B tech.")

    if result:
        with open("leads/reels_scripts.md", 'w', encoding='utf-8') as f:
            f.write(result)
        print("[OK] leads/reels_scripts.md cree!")
        return True
    return False

def main():
    """Génère tous les documents LEADS"""
    print("\n" + "="*60)
    print(">>> LEADS GENERATOR - GPT-4o-mini <<<")
    print("="*60 + "\n")

    success_count = 0

    # 1. Argumentaire de vente
    print("TACHE 1: Argumentaire de vente")
    print("-" * 60)
    if generate_argumentaire_vente():
        success_count += 1

    # 2. Cibles prioritaires
    print("\nTACHE 2: Cibles prioritaires")
    print("-" * 60)
    if generate_cibles_prioritaires():
        success_count += 1

    # 3. Scripts Reels
    print("\nTACHE 3: Scripts Reels TikTok")
    print("-" * 60)
    if generate_reels_scripts():
        success_count += 1

    print("\n" + "="*60)
    print(f">>> GENERATION TERMINEE: {success_count}/3 documents crees <<<")
    print("="*60)
    print("\nDossier /leads pret pour la prospection!")

if __name__ == "__main__":
    main()
