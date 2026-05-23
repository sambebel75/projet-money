#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
subtitle_generator.py — Générateur de sous-titres automatiques avec Whisper

Ce script génère des fichiers de sous-titres (.srt) à partir de fichiers audio
en utilisant Whisper (OpenAI) en local — 100% gratuit.

Stack : Python 3.10+ | openai-whisper | Aucun coût API

Usage:
    python subtitle_generator.py --audio audio.mp3 --output subtitles.srt
    python subtitle_generator.py --audio audio.mp3 --model small --language fr
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional

try:
    import whisper
except ImportError:
    print("❌ Module 'whisper' non installé.")
    print("   Installation : pip install openai-whisper")
    print("   Ou pour version accélérée : pip install faster-whisper")
    sys.exit(1)

# Configuration des logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('subtitle_generator.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

# Modèles Whisper disponibles
WHISPER_MODELS = {
    'tiny': {'params': '39M', 'speed': '~32x', 'quality': 'Baseline'},
    'base': {'params': '74M', 'speed': '~16x', 'quality': 'Better'},
    'small': {'params': '244M', 'speed': '~6x', 'quality': 'Good (recommandé)'},
    'medium': {'params': '769M', 'speed': '~2x', 'quality': 'Excellent'},
    'large': {'params': '1550M', 'speed': '~1x', 'quality': 'Best (lent)'},
}

DEFAULT_MODEL = 'small'
DEFAULT_LANGUAGE = 'fr'


def format_timestamp(seconds: float) -> str:
    """
    Convertit des secondes en format timestamp SRT (HH:MM:SS,mmm).
    
    Args:
        seconds: Temps en secondes
    
    Returns:
        Timestamp formaté pour fichier .srt
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millisecs = int((seconds % 1) * 1000)
    
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millisecs:03d}"


def generate_subtitles(
    audio_file: str,
    output_file: str,
    model_name: str = DEFAULT_MODEL,
    language: str = DEFAULT_LANGUAGE,
    max_line_length: int = 42,
    max_lines: int = 2
) -> bool:
    """
    Génère un fichier de sous-titres SRT à partir d'un fichier audio.
    
    Args:
        audio_file: Chemin du fichier audio (MP3, WAV, M4A, etc.)
        output_file: Chemin du fichier de sortie (.srt)
        model_name: Modèle Whisper à utiliser (tiny/base/small/medium/large)
        language: Code langue (fr/en/es/de/etc.)
        max_line_length: Longueur maximale par ligne (caractères)
        max_lines: Nombre maximum de lignes par sous-titre
    
    Returns:
        True si succès, False sinon
    """
    try:
        # Vérification du fichier audio
        audio_path = Path(audio_file)
        if not audio_path.exists():
            logger.error(f"❌ Fichier audio introuvable: {audio_file}")
            return False
        
        logger.info(f"🎵 Fichier audio chargé: {audio_file}")
        logger.info(f"   Taille: {audio_path.stat().st_size / 1024 / 1024:.2f} MB")
        
        # Chargement du modèle
        logger.info(f"🤖 Chargement du modèle Whisper: {model_name}")
        logger.info(f"   Language cible: {language}")
        
        model = whisper.load_model(model_name)
        
        # Transcription
        logger.info("🎙️ Démarrage de la transcription...")
        
        result = model.transcribe(
            audio_file,
            language=language,
            task='transcribe',
            verbose=False
        )
        
        segments = result['segments']
        
        if not segments:
            logger.warning("⚠️ Aucun segment de transcription généré")
            return False
        
        logger.info(f"✅ Transcription terminée: {len(segments)} segments")
        
        # Génération du fichier SRT
        srt_content = []
        
        for i, segment in enumerate(segments, start=1):
            start_time = format_timestamp(segment['start'])
            end_time = format_timestamp(segment['end'])
            
            # Nettoyage du texte
            text = segment['text'].strip()
            
            # Formatage pour Instagram Reels (max 2 lignes, 42 chars max)
            text_formatted = format_for_instagram(
                text,
                max_line_length=max_line_length,
                max_lines=max_lines
            )
            
            # Création de l'entrée SRT
            srt_entry = f"{i}\n{start_time} --> {end_time}\n{text_formatted}\n"
            srt_content.append(srt_entry)
        
        # Écriture du fichier
        output_path = Path(output_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(srt_content))
        
        logger.info(f"✅ Fichier SRT généré: {output_file}")
        logger.info(f"   Nombre de sous-titres: {len(srt_content)}")
        
        # Statistiques
        total_words = sum(len(s.split()) for s in srt_content)
        logger.info(f"   Mots totaux: {total_words}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Erreur lors de la génération des sous-titres: {str(e)}")
        return False


def format_for_instagram(text: str, max_line_length: int = 42, max_lines: int = 2) -> str:
    """
    Formate un texte pour les sous-titres Instagram Reels.
    
    - Maximum 2 lignes
    - Maximum 42 caractères par ligne
    - Coupure aux mots (pas au milieu d'un mot)
    
    Args:
        text: Texte original
        max_line_length: Longueur maximale par ligne
        max_lines: Nombre maximum de lignes
    
    Returns:
        Texte formaté pour Instagram
    """
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:
            current_line += (" " if current_line else "") + word
        else:
            if current_line:
                lines.append(current_line)
            if len(lines) >= max_lines:
                # On a atteint le max de lignes, on tronque
                break
            current_line = word
    
    if current_line and len(lines) < max_lines:
        lines.append(current_line)
    
    return '\n'.join(lines)


def split_long_segments(
    segments: list,
    max_duration: float = 3.0
) -> list:
    """
    Divise les segments trop longs en plusieurs segments plus courts.
    
    Utile pour les sous-titres Instagram qui doivent être rapides à lire.
    
    Args:
        segments: Liste de segments Whisper
        max_duration: Durée maximale par segment (secondes)
    
    Returns:
        Liste de segments divisés
    """
    new_segments = []
    
    for segment in segments:
        duration = segment['end'] - segment['start']
        
        if duration <= max_duration:
            new_segments.append(segment)
        else:
            # Diviser le segment
            words = segment['text'].split()
            n_words = len(words)
            n_splits = int(duration / max_duration) + 1
            words_per_split = max(1, n_words // n_splits)
            
            for i in range(0, n_words, words_per_split):
                split_words = words[i:i + words_per_split]
                split_duration = duration / n_splits
                
                new_segment = {
                    'start': segment['start'] + (i / n_words) * duration,
                    'end': segment['start'] + ((i + words_per_split) / n_words) * duration,
                    'text': ' '.join(split_words)
                }
                new_segments.append(new_segment)
    
    return new_segments


def convert_srt_to_capcut(srt_file: str, output_file: str) -> bool:
    """
    Convertit un fichier SRT vers un format compatible avec CapCut.
    
    CapCut accepte les fichiers SRT standards, mais cette fonction
    peut ajouter des styles spécifiques si nécessaire.
    
    Args:
        srt_file: Chemin du fichier SRT source
        output_file: Chemin du fichier de sortie
    
    Returns:
        True si succès, False sinon
    """
    try:
        # Pour l'instant, on copie simplement le fichier SRT
        # CapCut lit nativement le format SRT standard
        srt_path = Path(srt_file)
        output_path = Path(output_file)
        
        if not srt_path.exists():
            logger.error(f"❌ Fichier SRT introuvable: {srt_file}")
            return False
        
        with open(srt_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"✅ Fichier CapCut généré: {output_file}")
        return True
        
    except Exception as e:
        logger.error(f"❌ Erreur lors de la conversion CapCut: {str(e)}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='📝 Générateur de sous-titres automatiques avec Whisper'
    )
    
    parser.add_argument(
        '--audio', '-a',
        type=str,
        required=True,
        help='Fichier audio à transcrire (MP3, WAV, M4A)'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        required=True,
        help='Fichier de sortie SRT'
    )
    
    parser.add_argument(
        '--model', '-m',
        type=str,
        default=DEFAULT_MODEL,
        choices=list(WHISPER_MODELS.keys()),
        help=f'Modèle Whisper (défaut: {DEFAULT_MODEL})'
    )
    
    parser.add_argument(
        '--language', '-l',
        type=str,
        default=DEFAULT_LANGUAGE,
        help='Langue de transcription (défaut: fr)'
    )
    
    parser.add_argument(
        '--max-line-length',
        type=int,
        default=42,
        help='Longueur maximale par ligne (défaut: 42)'
    )
    
    parser.add_argument(
        '--max-lines',
        type=int,
        default=2,
        help='Nombre maximum de lignes par sous-titre (défaut: 2)'
    )
    
    parser.add_argument(
        '--capcut',
        action='store_true',
        help='Générer également un fichier compatible CapCut'
    )
    
    parser.add_argument(
        '--list-models',
        action='store_true',
        help='Lister les modèles disponibles et quitter'
    )
    
    args = parser.parse_args()
    
    # Lister les modèles
    if args.list_models:
        print("\n🤖 Modèles Whisper disponibles:\n")
        print(f"{'Modèle':<10} {'Params':<10} {'Vitesse':<10} {'Qualité'}")
        print("-" * 50)
        for name, info in WHISPER_MODELS.items():
            print(f"{name:<10} {info['params']:<10} {info['speed']:<10} {info['quality']}")
        print("\n💡 Recommandation: Utilisez 'small' pour un bon équilibre qualité/vitesse.\n")
        sys.exit(0)
    
    # Génération des sous-titres
    success = generate_subtitles(
        audio_file=args.audio,
        output_file=args.output,
        model_name=args.model,
        language=args.language,
        max_line_length=args.max_line_length,
        max_lines=args.max_lines
    )
    
    # Conversion CapCut optionnelle
    if success and args.capcut:
        capcut_file = args.output.replace('.srt', '_capcut.srt')
        convert_srt_to_capcut(args.output, capcut_file)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
