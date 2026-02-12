#!/usr/bin/env python3
"""
Télécharge des vidéos de test gratuites pour valider le système
L'utilisateur pourra ensuite les remplacer par de vraies vidéos HD
"""

import urllib.request
from pathlib import Path
import sys

# Vidéos de test depuis Sample Videos (domaine public)
SAMPLE_VIDEOS = [
    {
        "url": "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4",
        "filename": "villa-glass-walls.mp4",
        "description": "Video de test 1 (a remplacer)"
    },
    {
        "url": "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_2mb.mp4",
        "filename": "solar-panels-ground.mp4",
        "description": "Video de test 2 (a remplacer)"
    },
    {
        "url": "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_5mb.mp4",
        "filename": "modern-roof-stars.mp4",
        "description": "Video de test 3 (a remplacer)"
    }
]

OUTPUT_DIR = Path(__file__).parent.parent / "src" / "assets" / "videos"

def download_progress(block_num, block_size, total_size):
    """Affiche la progression"""
    downloaded = block_num * block_size
    if total_size > 0:
        percent = min(100, (downloaded / total_size) * 100)
        print(f"\r  Progression: {percent:.1f}%", end='', flush=True)

def download_video(url, filename, description):
    """Télécharge une vidéo"""
    print(f"\n[VIDEO] {description}")
    print(f"   Fichier: {filename}")

    output_path = OUTPUT_DIR / filename

    if output_path.exists():
        file_size_mb = output_path.stat().st_size / (1024 * 1024)
        print(f"  [OK] Deja present ({file_size_mb:.2f} MB)")
        return True

    try:
        print(f"  Telechargement...")
        urllib.request.urlretrieve(url, output_path, reporthook=download_progress)
        print()

        file_size_mb = output_path.stat().st_size / (1024 * 1024)
        print(f"  [OK] Telecharge ({file_size_mb:.2f} MB)")
        return True

    except Exception as e:
        print(f"\n  [ERROR] {e}")
        return False

def main():
    """Point d'entrée"""
    print("=" * 70)
    print("  TELECHARGEMENT VIDEOS DE TEST - SOLAIRE EMPIRE")
    print("  Note: Videos temporaires pour tester le systeme")
    print("=" * 70)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\n[FOLDER] Destination: {OUTPUT_DIR}")

    success = 0
    for video in SAMPLE_VIDEOS:
        if download_video(video["url"], video["filename"], video["description"]):
            success += 1

    print("\n" + "=" * 70)
    print(f"[SUCCESS] {success}/{len(SAMPLE_VIDEOS)} videos telechargees")
    print("=" * 70)

    if success == len(SAMPLE_VIDEOS):
        print("\n[INFO] Videos de test installees avec succes!")
        print("\n[NEXT] Prochaines etapes:")
        print("  1. Testez le systeme: npm run dev")
        print("  2. Remplacez par de vraies videos HD depuis:")
        print("     - Mixkit.co (gratuit, sans compte)")
        print("     - Pexels.com (gratuit, meilleure qualite)")
        print("  3. Voir: QUICK_VIDEO_DOWNLOAD.md pour les instructions")
        return 0
    else:
        print("\n[WARNING] Echec du telechargement")
        print("[INFO] Telechargez manuellement (voir QUICK_VIDEO_DOWNLOAD.md)")
        return 1

if __name__ == "__main__":
    sys.exit(main())
