#!/usr/bin/env python3
"""Parser pour nettoyer les résultats des agents"""

import json
import re

def extract_json_from_markdown(text):
    """Extrait le JSON d'un bloc code markdown"""
    # Cherche les blocs ```json ... ```
    pattern = r'```json\n(.*?)\n```'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1)
    # Si pas de bloc, retourne le texte brut
    return text

def parse_gpt4o_results():
    """Parse les résultats GPT-4o et crée catalogue.json"""
    with open("agents/results_gpt4o_pdf.json", 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extrait le premier résultat
    raw_result = data['results'][0]

    # Nettoie le JSON
    clean_json = extract_json_from_markdown(raw_result)

    # Parse et reformate
    catalogue = json.loads(clean_json)

    # Sauvegarde dans data/catalogue.json
    with open("data/catalogue.json", 'w', encoding='utf-8') as f:
        json.dump(catalogue, f, indent=2, ensure_ascii=False)

    print("[OK] data/catalogue.json cree avec succes!")
    print(f"- {len(catalogue['produits'])} produits")
    print(f"- Revolution CdTe: {len(catalogue['revolution_cdte']['avantages'])} avantages")

if __name__ == "__main__":
    parse_gpt4o_results()
