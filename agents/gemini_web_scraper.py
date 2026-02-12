#!/usr/bin/env python3
"""Agent Gemini pour l'analyse web de advsolarpower.com"""

import json
import requests

OPENROUTER_API_KEY = "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"
OPENROUTER_BASE = "https://openrouter.ai/api/v1/chat/completions"

def call_gemini(task):
    """Appel à Gemini via OpenRouter"""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Solaire Empire - Gemini Web Scraper"
    }

    messages = [
        {"role": "system", "content": "Tu es un analyste web expert. Réponds en JSON structuré."},
        {"role": "user", "content": task}
    ]

    payload = {
        "model": "google/gemini-pro",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 4000
    }

    print("[Gemini] Appel en cours...")
    response = requests.post(OPENROUTER_BASE, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        content = result['choices'][0]['message']['content']
        print(f"[Gemini] [OK] Reponse recue ({len(content)} caracteres)")
        return content
    else:
        print(f"[Gemini] [ERREUR] {response.status_code}: {response.text}")
        return None

def analyze_advsolarpower():
    """Analyse le site advsolarpower.com"""
    task = """
Analyse le site web: https://www.advsolarpower.com

MISSION:
1. Extrais toutes les URLs de vidéos (YouTube, Vimeo, vidéos hébergées)
2. Identifie les Reels/Stories de présentation
3. Récupère les scripts/textes de présentation associés
4. Note les messages clés marketing

RETOURNE un JSON structuré avec:
{
    "videos": [
        {"url": "...", "titre": "...", "type": "reel/demo/tutoriel"}
    ],
    "scripts": [
        {"video_id": "...", "texte": "...", "message_cle": "..."}
    ],
    "branding": {
        "slogans": [...],
        "arguments_vente": [...]
    }
}

Si tu ne peux pas accéder au site directement, fournis un template de structure attendue avec des exemples plausibles pour un site de panneaux solaires avancés.
"""

    result = call_gemini(task)

    if result:
        # Sauvegarde le résultat
        output = {
            "agent": "Gemini Analyste Web",
            "model": "google/gemini-pro",
            "source": "https://www.advsolarpower.com",
            "results": [result]
        }

        with open("agents/results_gemini_web.json", 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print("[OK] agents/results_gemini_web.json cree!")
        return output
    else:
        print("[ERREUR] Impossible d'obtenir les resultats Gemini")
        return None

if __name__ == "__main__":
    print("="*60)
    print(">>> GEMINI WEB SCRAPER <<<")
    print("="*60)
    analyze_advsolarpower()
