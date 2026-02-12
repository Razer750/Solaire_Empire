#!/usr/bin/env python3
"""
Script de téléchargement direct de vidéos HD
Alternative sans API - Utilise des URLs directes depuis Pixabay
"""

import urllib.request
from pathlib import Path
import sys

# ========================================
# VIDÉOS GRATUITES DIRECTES (Pixabay)
# ========================================

# URLs directes de vidéos gratuites HD (licence libre)
VIDEOS = [
    {
        "url": "https://videos.pexels.com/video-files/3044967/3044967-hd_1920_1080_30fps.mp4",
        "filename": "villa-glass-walls.mp4",
        "description": "Villa moderne avec architecture en verre"
    },
    {
        "url": "https://videos.pexels.com/video-files/7989411/7989411-hd_1920_1080_30fps.mp4",
        "filename": "solar-panels-ground.mp4",
        "description": "Panneaux solaires au sol"
    },
    {
        "url": "https://videos.pexels.com/video-files/2387611/2387611-hd_1920_1080_24fps.mp4",
        "filename": "modern-roof-stars.mp4",
        "description": "Ciel étoilé nocturne"
    }
]

OUTPUT_DIR = Path(__file__).parent.parent / "src" / "assets" / "videos"

# ========================================
# FONCTIONS
# ========================================

def download_progress(block_num, block_size, total_size):
    """Affiche la progression du téléchargement"""
    downloaded = block_num * block_size
    if total_size > 0:
        percent = min(100, (downloaded / total_size) * 100)
        print(f"\r  Progression: {percent:.1f}%", end='', flush=True)


def download_video(url, filename, description):
    """Télécharge une vidéo depuis une URL directe"""
    print(f"\n[VIDEO] {description}")
    print(f"   Fichier: {filename}")

    output_path = OUTPUT_DIR / filename

    # Vérifier si le fichier existe déjà
    if output_path.exists():
        file_size_mb = output_path.stat().st_size / (1024 * 1024)
        print(f"  [OK] Deja present ({file_size_mb:.2f} MB) - ignore")
        return True

    try:
        print(f"  Telechargement depuis Pexels...")
        urllib.request.urlretrieve(url, output_path, reporthook=download_progress)
        print()  # Nouvelle ligne après la progression

        file_size_mb = output_path.stat().st_size / (1024 * 1024)
        print(f"  [OK] Telecharge avec succes ({file_size_mb:.2f} MB)")
        return True

    except Exception as e:
        print(f"\n  [ERROR] Erreur: {e}")
        print(f"  [INFO] Telechargez manuellement depuis: https://www.pexels.com/videos/")
        return False


def main():
    """Télécharge toutes les vidéos"""
    print("=" * 70)
    print("  TELECHARGEMENT VIDEOS HD - SOLAIRE EMPIRE")
    print("  Source: Pexels (Licence libre - Gratuit)")
    print("=" * 70)

    # Créer le répertoire de sortie
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\n[FOLDER] Destination: {OUTPUT_DIR}")

    success_count = 0

    # Télécharger chaque vidéo
    for video in VIDEOS:
        if download_video(video["url"], video["filename"], video["description"]):
            success_count += 1

    # Résumé
    print("\n" + "=" * 70)
    print(f"[SUCCESS] Termine: {success_count}/{len(VIDEOS)} videos pretes")
    print("=" * 70)

    # Vérifier que toutes les vidéos sont présentes
    all_present = all((OUTPUT_DIR / v["filename"]).exists() for v in VIDEOS)

    if all_present:
        print("\n[SUCCESS] Toutes les videos sont pretes !")
        print("\n[NEXT] Prochaines etapes:")
        print("  1. Testez localement: npm run dev")
        print("  2. Verifiez les videos a http://localhost:5173")
        print("  3. Deployez: git add . && git commit -m 'feat: Add local HD videos' && git push")
        return 0
    else:
        print("\n[WARNING] Certaines videos manquent encore")
        print("\n[INFO] Telechargement manuel:")
        print("  1. Visitez: https://www.pexels.com/videos/")
        print("  2. Recherchez:")
        for v in VIDEOS:
            if not (OUTPUT_DIR / v["filename"]).exists():
                print(f"     - {v['description']}")
        print(f"  3. Enregistrez dans: {OUTPUT_DIR}")
        print("  4. Renommez selon:")
        for v in VIDEOS:
            if not (OUTPUT_DIR / v["filename"]).exists():
                print(f"     - {v['filename']}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
