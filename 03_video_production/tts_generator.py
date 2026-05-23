#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tts_generator.py — Générateur de voix off IA avec Edge-TTS (Microsoft)

Ce script génère des fichiers audio MP3 de qualité professionnelle
en utilisant la technologie Edge-TTS de Microsoft (100% gratuit).

Stack : Python 3.10+ | edge-tts | Aucun coût

Usage:
    python tts_generator.py --text "Votre texte ici" --output audio.mp3
    python tts_generator.py --script script.txt --output audio.mp3 --voice fr-FR-DeniseNeural
"""

import argparse
import asyncio
import logging
import sys
from pathlib import Path
from datetime import datetime

import edge_tts
from pydub import AudioSegment

# Configuration des logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('tts_generator.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

# Voix françaises disponibles (Edge-TTS Microsoft)
FRENCH_VOICES = {
    'denise': 'fr-FR-DeniseNeural',      # Féminine, recommandée pour UGC
    'henri': 'fr-FR-HenriNeural',        # Masculine
    'alain': 'fr-FR-AlainNeural',        # Masculine alternative
    'brigitte': 'fr-FR-BrigitteNeural',  # Féminine alternative
    'celeste': 'fr-FR-CelesteNeural',    # Féminine
    'claude': 'fr-FR-ClaudeNeural',      # Masculine
    'coraline': 'fr-FR-CoralineNeural',  # Féminine
    'jacqueline': 'fr-FR-JacquelineNeural',  # Féminine
}

DEFAULT_VOICE = FRENCH_VOICES['denise']
DEFAULT_RATE = '+0%'      # Vitesse normale
DEFAULT_PITCH = '+0Hz'    # Pitch normal


async def generate_speech(
    text: str,
    output_file: str,
    voice: str = DEFAULT_VOICE,
    rate: str = DEFAULT_RATE,
    pitch: str = DEFAULT_PITCH,
    volume: str = '+0%'
) -> bool:
    """
    Génère un fichier audio à partir du texte avec Edge-TTS.
    
    Args:
        text: Le texte à convertir en speech
        output_file: Chemin du fichier de sortie (.mp3)
        voice: Voice ID (ex: fr-FR-DeniseNeural)
        rate: Vitesse (+50% max, -50% min)
        pitch: Pitch adjustment (+20Hz max, -20Hz min)
        volume: Volume adjustment (+100% max, -100% min)
    
    Returns:
        True si succès, False sinon
    """
    try:
        logger.info(f"Génération audio avec la voix: {voice}")
        logger.info(f"Paramètres: rate={rate}, pitch={pitch}, volume={volume}")
        
        # Initialisation de la communication Edge-TTS
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch, volume=volume)
        
        # Sauvegarde du fichier audio
        await communicate.save(output_file)
        
        # Vérification du fichier généré
        if Path(output_file).exists():
            file_size = Path(output_file).stat().st_size
            duration = len(AudioSegment.from_mp3(output_file)) / 1000.0
            
            logger.info(f"✅ Fichier généré avec succès: {output_file}")
            logger.info(f"   Taille: {file_size / 1024:.2f} KB")
            logger.info(f"   Durée: {duration:.2f} secondes")
            
            return True
        else:
            logger.error(f"❌ Le fichier n'a pas été créé: {output_file}")
            return False
            
    except Exception as e:
        logger.error(f"❌ Erreur lors de la génération audio: {str(e)}")
        return False


async def generate_from_file(
    script_file: str,
    output_file: str,
    voice: str = DEFAULT_VOICE,
    **kwargs
) -> bool:
    """
    Génère un audio à partir d'un fichier script.
    
    Args:
        script_file: Chemin du fichier contenant le script
        output_file: Chemin du fichier de sortie
        voice: Voice ID
    
    Returns:
        True si succès, False sinon
    """
    try:
        script_path = Path(script_file)
        
        if not script_path.exists():
            logger.error(f"❌ Fichier script introuvable: {script_file}")
            return False
        
        # Lecture du script
        with open(script_path, 'r', encoding='utf-8') as f:
            text = f.read().strip()
        
        if not text:
            logger.error("❌ Le fichier script est vide")
            return False
        
        logger.info(f"📄 Script chargé: {len(text)} caractères")
        
        # Nettoyage du texte (suppression marqueurs de formatage)
        text_clean = clean_script_text(text)
        logger.info(f"🧹 Texte nettoyé: {len(text_clean)} caractères")
        
        # Génération audio
        return await generate_speech(
            text=text_clean,
            output_file=output_file,
            voice=voice,
            **kwargs
        )
        
    except Exception as e:
        logger.error(f"❌ Erreur lors de la lecture du script: {str(e)}")
        return False


def clean_script_text(text: str) -> str:
    """
    Nettoie un texte de script en supprimant les marqueurs de formatage.
    
    Utile pour extraire uniquement le texte à prononcer depuis un script
    formaté avec des balises [0-3s], 🎙️ VO:, etc.
    
    Args:
        text: Texte brut du script
    
    Returns:
        Texte nettoyé prêt pour TTS
    """
    import re
    
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Extraire le texte après "🎙️ VO :" ou "VO :"
        vo_match = re.search(r'(?:🎙️\s*)?VO\s*:\s*["\']?(.+?)["\']?\s*$', line, re.IGNORECASE)
        if vo_match:
            cleaned_lines.append(vo_match.group(1).strip())
            continue
        
        # Si pas de marqueur VO, garder la ligne si elle semble être du texte parlé
        if line.strip() and not line.startswith('[') and not line.startswith('#'):
            # Supprimer les emojis
            line_clean = re.sub(r'[^\w\s.,;:!?\'"()-]', '', line.strip())
            if line_clean and len(line_clean) > 3:
                cleaned_lines.append(line_clean)
    
    return ' '.join(cleaned_lines)


def list_voices():
    """Affiche la liste des voix françaises disponibles."""
    print("\n🎙️ Voix françaises disponibles (Edge-TTS Microsoft):\n")
    print(f"{'Nom':<15} {'Voice ID':<25} {'Genre':<12} {'Recommandation'}")
    print("-" * 70)
    
    recommendations = {
        'denise': "⭐ Recommandée pour UGC (naturelle, dynamique)",
        'henri': "Bonne alternative masculine",
        'alain': "Plus grave, autoritaire",
        'brigitte': "Douce, pédagogique",
        'celeste': "Jeune, énergique",
        'claude': "Mature, sérieuse",
        'coraline': "Claire, professionnelle",
        'jacqueline': "Expérimentée, crédible"
    }
    
    for name, voice_id in FRENCH_VOICES.items():
        genre = "Féminine" if name in ['denise', 'brigitte', 'celeste', 'coraline', 'jacqueline'] else "Masculine"
        rec = recommendations.get(name, "")
        print(f"{name:<15} {voice_id:<25} {genre:<12} {rec}")
    
    print("\n💡 Astuce: Pour un Reel Instagram, utilisez Denise avec rate=+5% pour plus de dynamisme.\n")


def optimize_for_instagram(text: str) -> str:
    """
    Optimise un texte pour la lecture Instagram Reel.
    
    - Ajoute des pauses naturelles
    - Adapte la ponctuation pour le rythme
    - Supprime les mots inutiles
    
    Args:
        text: Texte original
    
    Returns:
        Texte optimisé pour Reel
    """
    import re
    
    # Ajouter des pauses après les hooks
    text = re.sub(r'([.!?])\s+', r'\1 <break time="300ms"/> ', text)
    
    # Raccourcir certaines formulations
    replacements = {
        'est-ce que': '',
        'en fait': '',
        'du coup': '',
        'voilà': '',
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text


async def batch_generate(
    scripts_dir: str,
    output_dir: str,
    voice: str = DEFAULT_VOICE,
    **kwargs
) -> dict:
    """
    Génère des audio pour multiple scripts dans un dossier.
    
    Args:
        scripts_dir: Dossier contenant les scripts (.txt)
        output_dir: Dossier de sortie pour les MP3
        voice: Voice ID
    
    Returns:
        Dict avec statistiques de génération
    """
    scripts_path = Path(scripts_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    script_files = list(scripts_path.glob('*.txt'))
    
    if not script_files:
        logger.warning(f"Aucun fichier .txt trouvé dans {scripts_dir}")
        return {'success': 0, 'failed': 0, 'total': 0}
    
    logger.info(f"📦 Batch processing: {len(script_files)} scripts trouvés")
    
    stats = {'success': 0, 'failed': 0, 'total': len(script_files)}
    
    for script_file in script_files:
        output_file = output_path / f"{script_file.stem}.mp3"
        logger.info(f"\n🎬 Traitement: {script_file.name}")
        
        success = await generate_from_file(
            script_file=str(script_file),
            output_file=str(output_file),
            voice=voice,
            **kwargs
        )
        
        if success:
            stats['success'] += 1
        else:
            stats['failed'] += 1
    
    return stats


def main():
    parser = argparse.ArgumentParser(
        description='🎙️ Générateur de voix off IA avec Edge-TTS (Microsoft)'
    )
    
    parser.add_argument(
        '--text', '-t',
        type=str,
        help='Texte à convertir en speech'
    )
    
    parser.add_argument(
        '--script', '-s',
        type=str,
        help='Fichier script contenant le texte (prioritaire sur --text)'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        required=True,
        help='Fichier de sortie MP3'
    )
    
    parser.add_argument(
        '--voice', '-v',
        type=str,
        default=DEFAULT_VOICE,
        choices=list(FRENCH_VOICES.values()),
        help=f'Voice ID (défaut: {DEFAULT_VOICE})'
    )
    
    parser.add_argument(
        '--rate', '-r',
        type=str,
        default=DEFAULT_RATE,
        help='Vitesse de lecture (ex: +5%, -10%, défault: +0%)'
    )
    
    parser.add_argument(
        '--pitch', '-p',
        type=str,
        default=DEFAULT_PITCH,
        help='Pitch adjustment (ex: +5Hz, -10Hz, défaut: +0Hz)'
    )
    
    parser.add_argument(
        '--volume',
        type=str,
        default='+0%',
        help='Volume adjustment (ex: +20%, -10%, défaut: +0%)'
    )
    
    parser.add_argument(
        '--list-voices', '-l',
        action='store_true',
        help='Lister les voix disponibles et quitter'
    )
    
    parser.add_argument(
        '--batch-dir',
        type=str,
        help='Dossier de scripts pour batch processing'
    )
    
    parser.add_argument(
        '--instagram-optim',
        action='store_true',
        help='Optimiser le texte pour Instagram Reel'
    )
    
    args = parser.parse_args()
    
    # Lister les voix
    if args.list_voices:
        list_voices()
        sys.exit(0)
    
    # Batch processing
    if args.batch_dir:
        stats = asyncio.run(batch_generate(
            scripts_dir=args.batch_dir,
            output_dir=args.output,
            voice=args.voice,
            rate=args.rate,
            pitch=args.pitch,
            volume=args.volume
        ))
        logger.info(f"\n📊 Statistiques batch:")
        logger.info(f"   Succès: {stats['success']}")
        logger.info(f"   Échecs: {stats['failed']}")
        logger.info(f"   Total: {stats['total']}")
        sys.exit(0 if stats['failed'] == 0 else 1)
    
    # Validation des inputs
    if not args.text and not args.script:
        parser.error("Vous devez spécifier --text ou --script")
    
    # Génération unique
    if args.script:
        success = asyncio.run(generate_from_file(
            script_file=args.script,
            output_file=args.output,
            voice=args.voice,
            rate=args.rate,
            pitch=args.pitch,
            volume=args.volume
        ))
    else:
        text = optimize_for_instagram(args.text) if args.instagram_optim else args.text
        success = asyncio.run(generate_speech(
            text=text,
            output_file=args.output,
            voice=args.voice,
            rate=args.rate,
            pitch=args.pitch,
            volume=args.volume
        ))
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
