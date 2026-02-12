#!/usr/bin/env python3
"""
Script de téléchargement de vidéos HD depuis Pexels
Pour Solaire Empire - Projet Immo Pulse
"""

import requests
from pathlib import Path
import sys

# ========================================
# CONFIGURATION
# ========================================

PEXELS_API_KEY = "YOUR_API_KEY_HERE"  # https://www.pexels.com/api/
PEXELS_API_URL = "https://api.pexels.com/videos/search"

VIDEO_QUERIES = [
    {
        "query": "modern villa glass walls luxury architecture",
        "filename": "villa-glass-walls.mp4",
        "description": "Villa avec verrières transparentes"
    },
    {
        "query": "solar panels ground installation field",
        "filename": "solar-panels-ground.mp4",
        "description": "Dalles solaires au sol"
    },
    {
        "query": "modern roof architecture night stars sky",
        "filename": "modern-roof-stars.mp4",
        "description": "Toit moderne sous les étoiles"
    }
]

# Chemin relatif depuis la racine du projet
OUTPUT_DIR = Path(__file__).parent.parent / "src" / "assets" / "videos"

# ========================================
# FONCTIONS
# ========================================

def download_video(url, filename):
    """Télécharge une vidéo depuis une URL"""
    print(f"  Téléchargement de {filename}...")

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        output_path = OUTPUT_DIR / filename
        total_size = int(response.headers.get('content-length', 0))

        with open(output_path, 'wb') as f:
            downloaded = 0
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                downloaded += len(chunk)
                if total_size > 0:
                    progress = (downloaded / total_size) * 100
                    print(f"\r  Progression: {progress:.1f}%", end='', flush=True)

        print()  # Nouvelle ligne après la progression
        file_size_mb = output_path.stat().st_size / (1024 * 1024)
        print(f"  ✓ Téléchargé: {filename} ({file_size_mb:.2f} MB)")

        return output_path

    except Exception as e:
        print(f"  ✗ Erreur lors du téléchargement: {e}")
        return None


def search_and_download_videos():
    """Recherche et télécharge les vidéos depuis Pexels"""

    # Vérification de la clé API
    if PEXELS_API_KEY == "YOUR_API_KEY_HERE":
        print("❌ ERREUR: Vous devez configurer votre clé API Pexels")
        print("\n📝 Instructions:")
        print("1. Créez un compte sur https://www.pexels.com/")
        print("2. Générez une clé API sur https://www.pexels.com/api/")
        print("3. Remplacez 'YOUR_API_KEY_HERE' dans ce script par votre clé")
        print("\n💡 Alternative: Téléchargez manuellement depuis pexels.com/videos")
        print("   Recherches suggérées:")
        for vq in VIDEO_QUERIES:
            print(f"   - {vq['query']}")
        return

    # Création du répertoire de sortie
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"📁 Répertoire de sortie: {OUTPUT_DIR}\n")

    headers = {"Authorization": PEXELS_API_KEY}
    downloaded_count = 0

    for video_spec in VIDEO_QUERIES:
        print(f"🔍 Recherche: {video_spec['description']}")
        print(f"   Query: \"{video_spec['query']}\"")

        # Vérifier si le fichier existe déjà
        output_path = OUTPUT_DIR / video_spec['filename']
        if output_path.exists():
            file_size_mb = output_path.stat().st_size / (1024 * 1024)
            print(f"  ⚠️  Fichier existant: {video_spec['filename']} ({file_size_mb:.2f} MB)")
            print(f"  ℹ️  Supprimez le fichier pour re-télécharger\n")
            continue

        try:
            params = {
                "query": video_spec["query"],
                "per_page": 5,
                "orientation": "landscape"
            }

            response = requests.get(PEXELS_API_URL, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            if not data.get("videos"):
                print(f"  ❌ Aucune vidéo trouvée pour: {video_spec['query']}\n")
                continue

            # Trouve la meilleure vidéo HD (1920x1080 ou supérieur)
            best_video = None
            best_file = None

            for video in data["videos"]:
                for file in video.get("video_files", []):
                    # Cherche une vidéo HD avec largeur >= 1920
                    if file.get("quality") == "hd" and file.get("width", 0) >= 1920:
                        best_video = video
                        best_file = file
                        break
                if best_video:
                    break

            # Fallback sur la première vidéo disponible si pas de HD
            if not best_video:
                best_video = data["videos"][0]
                best_file = data["videos"][0]["video_files"][0]
                print(f"  ⚠️  Pas de vidéo HD trouvée, utilisation de la meilleure disponible")

            print(f"  ✓ Trouvé: {best_file['width']}x{best_file['height']} ({best_file.get('quality', 'N/A')})")

            # Télécharger
            if download_video(best_file["link"], video_spec["filename"]):
                downloaded_count += 1

            print()  # Ligne vide entre les vidéos

        except requests.exceptions.RequestException as e:
            print(f"  ❌ Erreur API Pexels: {e}\n")
            continue

    # Résumé
    print("=" * 60)
    print(f"✅ Téléchargement terminé: {downloaded_count}/{len(VIDEO_QUERIES)} vidéos")
    print(f"📁 Emplacement: {OUTPUT_DIR}")

    if downloaded_count < len(VIDEO_QUERIES):
        print("\n⚠️  Certaines vidéos n'ont pas été téléchargées.")
        print("💡 Vous pouvez les télécharger manuellement depuis pexels.com/videos")


# ========================================
# POINT D'ENTRÉE
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("  TÉLÉCHARGEMENT VIDÉOS HD - SOLAIRE EMPIRE")
    print("=" * 60)
    print()

    search_and_download_videos()

    print("\n🎬 Prochaines étapes:")
    print("1. Vérifiez les vidéos dans: src/assets/videos/")
    print("2. Optimisez si nécessaire avec ffmpeg (si > 20MB)")
    print("3. Lancez: npm run dev")
    print()
