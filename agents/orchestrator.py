#!/usr/bin/env python3
"""
Orchestrateur Multi-Agents pour Solaire Empire
Délègue les tâches à Gemini et GPT-4o via OpenRouter
"""

import os
import json
import requests
from typing import Dict, List, Any

OPENROUTER_API_KEY = "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"
OPENROUTER_BASE = "https://openrouter.ai/api/v1/chat/completions"

class Agent:
    def __init__(self, model: str, name: str):
        self.model = model
        self.name = name
        self.results = []

    def call(self, task: str, context: Dict = None) -> Dict:
        """Appel à OpenRouter avec le modèle spécifié"""
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": f"Solaire Empire - {self.name}"
        }

        messages = [
            {"role": "system", "content": f"Tu es {self.name}, spécialisé dans cette tâche. Réponds en JSON structuré."},
            {"role": "user", "content": task}
        ]

        if context:
            messages.insert(1, {"role": "system", "content": f"Contexte: {json.dumps(context, ensure_ascii=False)}"})

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 4000
        }

        print(f"[{self.name}] Appel à {self.model}...")
        response = requests.post(OPENROUTER_BASE, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            print(f"[{self.name}] [OK] Reponse recue ({len(content)} caracteres)")
            self.results.append(content)
            return {"success": True, "data": content}
        else:
            error = f"Erreur {response.status_code}: {response.text}"
            print(f"[{self.name}] [ERREUR] {error}")
            return {"success": False, "error": error}

    def save_results(self, filepath: str):
        """Sauvegarde les résultats de l'agent"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({
                "agent": self.name,
                "model": self.model,
                "results": self.results
            }, f, indent=2, ensure_ascii=False)
        print(f"[{self.name}] Résultats sauvegardés: {filepath}")


class Orchestrator:
    def __init__(self):
        self.agents = {
            "gemini": Agent("google/gemini-pro", "Gemini Analyste Web"),
            "gpt4o": Agent("openai/gpt-4o", "GPT-4o Vérificateur PDF")
        }

    def delegate_web_analysis(self, url: str):
        """Délègue l'analyse web à Gemini"""
        task = f"""
Analyse le site web: {url}

MISSION:
1. Extrais toutes les URLs de vidéos (YouTube, Vimeo, vidéos hébergées)
2. Identifie les Reels/Stories de présentation
3. Récupère les scripts/textes de présentation associés
4. Note les messages clés marketing

RETOURNE un JSON avec:
{{
    "videos": [
        {{"url": "...", "titre": "...", "type": "reel/demo/tutoriel"}}
    ],
    "scripts": [
        {{"video_id": "...", "texte": "...", "message_cle": "..."}}
    ],
    "branding": {{
        "slogans": [...],
        "arguments_vente": [...]
    }}
}}
"""
        return self.agents["gemini"].call(task)

    def delegate_pdf_verification(self, pdf_info: List[str]):
        """Délègue la vérification PDF à GPT-4o"""
        task = f"""
MISSION: Vérification croisée de 5 PDFs techniques (Honstar/Longyan)

PDFs à analyser: {json.dumps(pdf_info, ensure_ascii=False)}

EXTRAIS et STRUCTURE:
1. Références produits (modèles, puissances, dimensions)
2. Spécifications techniques (CdTe, rendement, garanties)
3. Prix et disponibilité
4. Certifications (CE, TÜV, etc.)
5. Avantages technologie CdTe vs Silicium

RETOURNE un JSON pour data/catalogue.json:
{{
    "produits": [
        {{
            "ref": "...",
            "marque": "Honstar/Longyan",
            "puissance_w": 000,
            "technologie": "CdTe",
            "prix_ht": 000,
            "stock_france": true/false,
            "specs": {{...}},
            "arguments": ["Moins cher", "Plus esthétique", "Made in China mais stock Ivry"]
        }}
    ],
    "revolution_cdte": {{
        "avantages": [...],
        "comparatif_silicium": {{...}}
    }}
}}
"""
        return self.agents["gpt4o"].call(task)

    def execute_mission(self):
        """Lance l'orchestration complète"""
        print("\n" + "="*60)
        print(">>> SOLAIRE EMPIRE - ORCHESTRATION MULTI-AGENTS <<<")
        print("="*60 + "\n")

        # TÂCHE 1: Gemini analyse advsolarpower.com
        print("TACHE 1: Analyse Web (Gemini)")
        print("-" * 60)
        web_result = self.delegate_web_analysis("https://www.advsolarpower.com")

        if web_result["success"]:
            self.agents["gemini"].save_results("agents/results_gemini_web.json")

        # TÂCHE 2: GPT-4o vérifie les PDFs
        print("\nTACHE 2: Verification PDFs (GPT-4o)")
        print("-" * 60)

        # Liste des PDFs (à adapter selon ce qui est disponible)
        pdfs = [
            "Honstar_CdTe_Catalogue.pdf",
            "Longyan_Technical_Specs.pdf",
            "Honstar_Price_List_2025.pdf",
            "Longyan_Certification.pdf",
            "CdTe_Technology_Comparison.pdf"
        ]

        pdf_result = self.delegate_pdf_verification(pdfs)

        if pdf_result["success"]:
            self.agents["gpt4o"].save_results("agents/results_gpt4o_pdf.json")

            # Tente de parser et sauver directement dans catalogue.json
            try:
                catalogue_data = json.loads(pdf_result["data"])
                with open("data/catalogue.json", 'w', encoding='utf-8') as f:
                    json.dump(catalogue_data, f, indent=2, ensure_ascii=False)
                print("\n[OK] data/catalogue.json cree avec succes!")
            except:
                print("\n[WARN] Resultats bruts sauvegardes, necessite parsing manuel")

        print("\n" + "="*60)
        print(">>> ORCHESTRATION TERMINEE <<<")
        print("="*60)
        print("\nResultats disponibles:")
        print("- agents/results_gemini_web.json")
        print("- agents/results_gpt4o_pdf.json")
        print("- data/catalogue.json (si parsing reussi)")
        print("\n>>> Claude peut maintenant assembler le site Solaire Empire!")


if __name__ == "__main__":
    orchestrator = Orchestrator()
    orchestrator.execute_mission()
