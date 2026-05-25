#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
content_generator.py — Script principal de génération de contenu Instagram

Ce script automatise la génération complète de contenu Instagram :
1. Récupère les idées depuis Notion
2. Génère hooks, scripts, captions via IA (Claude/OpenAI)
3. Met à jour Notion avec le contenu généré
4. Prépare les fichiers pour production vidéo

Stack : Python 3.10+ | Notion API | Claude/OpenAI | 100% automatisé

Usage:
    python content_generator.py --notion-db <DATABASE_ID> --batch-size 5
    python content_generator.py --test-notion  # Test de connexion
"""

import argparse
import logging
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict

try:
    from notion_client import Client
except ImportError:
    print("❌ Module 'notion-client' non installé.")
    print("   Installation : pip install notion-client")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("⚠️ Module 'python-dotenv' non installé, utilisation des variables système")

# Configuration des logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('content_generator.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

# Prompts intégrés (version simplifiée, à charger depuis fichiers .md en prod)
PROMPT_HOOKS = """
Tu es un expert en copywriting Instagram spécialisé dans la niche B2B sécurité incendie ERP.

Génère 10 hooks viraux ultra-accrocheurs pour des Reels Instagram de 20-30 secondes.

Cible : Propriétaires de restaurants, hôtels, petits ERP
Douleurs : Amendes, fermetures administratives, méconnaissance des normes

Contraintes :
- ≤ 12 mots par hook
- Crée émotion forte (curiosité, peur, urgence)
- Utilise des chiffres concrets
- Parle directement au propriétaire ("tu", "ton")

Format de sortie : Liste numérotée de 10 hooks
"""

PROMPT_SCRIPT = """
Tu es un scénariste expert en Reels Instagram viraux pour la niche sécurité incendie.

Rédige un script complet de Reel de 25 secondes maximum, format voice-over faceless.

Hook : {hook}
Sujet : {topic}
CTA : {cta}

Structure :
[0-3s] HOOK
[3-8s] PROBLÈME / DOULEUR
[8-15s] SOLUTION / VALEUR
[15-20s] PREUVE SOCIALE / AUTORITÉ
[20-25s] CTA CLAIR

Contraintes :
- ~70-85 mots maximum
- Phrases courtes (≤15 mots)
- Ton direct, conversationnel ("tu")
- Un seul CTA clair

Format de sortie :
**[0-3s] HOOK**
📝 Texte écran : "..."
🎙️ VO : "..."

**[3-8s] PROBLÈME**
🎙️ VO : "..."

...etc
"""

PROMPT_CAPTION = """
Tu es un expert en copywriting Instagram et SEO.

Rédige une caption Instagram complète et optimisée pour un Reel.

Script du Reel :
{script}

Hook principal : {hook}
Mot-clé principal : {keyword}
CTA : {cta}

Structure AIDA obligatoire :
- 1ère ligne : Accroche (≤80 caractères)
- Paragraphe 1 : Intérêt (problème)
- Paragraphe 2 : Désir (solution)
- Paragraphe 3 : Preuve (autorité)
- CTA : Action claire
- Hashtags : 8-12 hashtags (après 3 sauts de ligne)

Contraintes :
- 800-2200 caractères total
- Ton conversationnel ("tu")
- Emojis modérés (1 tous les 2-3 paragraphes)
- Mot-clé principal dans les 125 premiers caractères

Format de sortie : Caption complète prête à copier-coller
"""


class ContentGenerator:
    """Générateur de contenu Instagram automatisé."""
    
    def __init__(self, notion_token: str, notion_db_id: str):
        """
        Initialise le générateur de contenu.
        
        Args:
            notion_token: Token d'intégration Notion
            notion_db_id: ID de la base de données Notion
        """
        self.notion = Client(auth=notion_token)
        self.db_id = notion_db_id
        logger.info("✅ Content Generator initialisé")
    
    def test_connection(self) -> bool:
        """Teste la connexion à l'API Notion."""
        try:
            database = self.notion.databases.retrieve(database_id=self.db_id)
            logger.info(f"✅ Connexion Notion réussie : {database.get('title', [{'text': {'content': 'Inconnu'}}])[0]['text']['content']}")
            return True
        except Exception as e:
            logger.error(f"❌ Erreur de connexion Notion : {str(e)}")
            return False
    
    def get_ideas_from_notion(self, limit: int = 5) -> List[Dict]:
        """
        Récupère les idées de contenu depuis Notion.
        
        Args:
            limit: Nombre d'idées à récupérer
        
        Returns:
            Liste des idées avec leurs propriétés
        """
        try:
            response = self.notion.databases.query(
                database_id=self.db_id,
                filter={
                    "property": "Status",
                    "select": {
                        "equals": "💡 Idée"
                    }
                },
                page_size=limit
            )
            
            ideas = []
            for page in response['results']:
                idea = {
                    'id': page['id'],
                    'title': self._get_property(page, 'Title'),
                    'topic': self._get_property(page, 'Sujet'),
                    'hook': self._get_property(page, 'Hook'),
                }
                ideas.append(idea)
            
            logger.info(f"📥 {len(ideas)} idées récupérées depuis Notion")
            return ideas
            
        except Exception as e:
            logger.error(f"❌ Erreur lors de la récupération des idées : {str(e)}")
            return []
    
    def _get_property(self, page: Dict, prop_name: str) -> str:
        """Extrait une propriété d'une page Notion."""
        try:
            prop = page['properties'].get(prop_name, {})
            
            if prop.get('type') == 'title':
                return prop['title'][0]['plain_text'] if prop['title'] else ''
            elif prop.get('type') == 'rich_text':
                return prop['rich_text'][0]['plain_text'] if prop['rich_text'] else ''
            elif prop.get('type') == 'select':
                return prop['select']['name'] if prop['select'] else ''
            else:
                return ''
        except Exception:
            return ''
    
    def generate_with_ai(self, prompt: str, model: str = 'claude') -> str:
        """
        Génère du contenu avec une IA (Claude ou OpenAI).
        
        Args:
            prompt: Prompt à envoyer à l'IA
            model: 'claude' ou 'openai'
        
        Returns:
            Contenu généré
        """
        api_key = os.getenv('ANTHROPIC_API_KEY') or os.getenv('OPENAI_API_KEY')
        
        if not api_key:
            logger.warning("⚠️ Aucune clé API trouvée. Génération simulée.")
            return "[CONTENU SIMULÉ - Ajoutez votre clé API pour générer du contenu réel]"
        
        try:
            if model == 'claude' and os.getenv('ANTHROPIC_API_KEY'):
                import anthropic
                client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
                
                response = client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=1000,
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.content[0].text
            
            elif model == 'openai' and os.getenv('OPENAI_API_KEY'):
                from openai import OpenAI
                client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
                
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=1000
                )
                return response.choices[0].message.content
            
            else:
                logger.warning("⚠️ Modèle IA non disponible")
                return "[CONTENU SIMULÉ - Clé API manquante]"
                
        except Exception as e:
            logger.error(f"❌ Erreur génération IA : {str(e)}")
            return "[ERREUR GÉNÉRATION IA]"
    
    def generate_hooks(self, topic: str = "") -> List[str]:
        """Génère 10 hooks pour un sujet donné."""
        prompt = f"{PROMPT_HOOKS}\n\nSujet spécifique : {topic}" if topic else PROMPT_HOOKS
        response = self.generate_with_ai(prompt)
        
        # Parse simple list
        hooks = []
        for line in response.split('\n'):
            if line.strip() and any(c.isdigit() for c in line[:3]):
                # Nettoyer : "1. " → ""
                hook = line.split('. ', 1)[-1].strip() if '. ' in line else line.strip()
                if hook and len(hook) > 5:
                    hooks.append(hook)
        
        return hooks[:10]
    
    def generate_script(self, hook: str, topic: str, cta: str = "KIT") -> str:
        """Génère un script complet à partir d'un hook."""
        prompt = PROMPT_SCRIPT.format(hook=hook, topic=topic, cta=cta)
        return self.generate_with_ai(prompt)
    
    def generate_caption(self, script: str, hook: str, keyword: str, cta: str) -> str:
        """Génère une caption optimisée à partir d'un script."""
        prompt = PROMPT_CAPTION.format(
            script=script[:500],  # Tronquer si trop long
            hook=hook,
            keyword=keyword,
            cta=cta
        )
        return self.generate_with_ai(prompt)
    
    def update_notion_page(
        self,
        page_id: str,
        **fields
    ) -> bool:
        """
        Met à jour une page Notion avec les champs générés.
        
        Args:
            page_id: ID de la page à mettre à jour
            **fields: Champs à mettre à jour (hook, script, caption, etc.)
        """
        try:
            properties = {}
            
            if 'hook' in fields:
                properties['Hook'] = {'rich_text': [{'text': {'content': fields['hook']}}]}
            
            if 'script' in fields:
                properties['Script'] = {'rich_text': [{'text': {'content': fields['script']}}]}
            
            if 'caption' in fields:
                properties['Caption'] = {'rich_text': [{'text': {'content': fields['caption']}}]}
            
            if 'status' in fields:
                properties['Status'] = {'select': {'name': fields['status']}}
            
            self.notion.pages.update(
                page_id=page_id,
                properties=properties
            )
            
            logger.info(f"✅ Page Notion mise à jour : {page_id}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Erreur mise à jour Notion : {str(e)}")
            return False
    
    def process_batch(self, batch_size: int = 5, output_dir: str = "output") -> Dict:
        """
        Traite un batch d'idées et génère le contenu complet.
        
        Args:
            batch_size: Nombre d'idées à traiter
            output_dir: Dossier de sortie pour les fichiers
        
        Returns:
            Statistiques de traitement
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Récupérer les idées
        ideas = self.get_ideas_from_notion(limit=batch_size)
        
        if not ideas:
            logger.warning("⚠️ Aucune idée trouvée dans Notion")
            return {'processed': 0, 'success': 0, 'failed': 0}
        
        stats = {'processed': len(ideas), 'success': 0, 'failed': 0}
        
        for i, idea in enumerate(ideas, start=1):
            logger.info(f"\n🎬 Traitement idée {i}/{len(ideas)} : {idea['title']}")
            
            try:
                # Génération hooks
                logger.info("🪝 Génération des hooks...")
                hooks = self.generate_hooks(idea.get('topic', ''))
                selected_hook = hooks[0] if hooks else idea.get('hook', 'Hook par défaut')
                
                # Génération script
                logger.info("📜 Génération du script...")
                script = self.generate_script(
                    hook=selected_hook,
                    topic=idea.get('topic', ''),
                    cta='KIT'
                )
                
                # Génération caption
                logger.info("📝 Génération de la caption...")
                caption = self.generate_caption(
                    script=script,
                    hook=selected_hook,
                    keyword=idea.get('topic', ''),
                    cta='KIT'
                )
                
                # Sauvegarde locale
                output_file = output_path / f"reel_{i:02d}_{idea['title'][:20]}.md"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(f"# {idea['title']}\n\n")
                    f.write(f"## Hook\n{selected_hook}\n\n")
                    f.write(f"## Script\n{script}\n\n")
                    f.write(f"## Caption\n{caption}\n")
                
                # Mise à jour Notion
                self.update_notion_page(
                    idea['id'],
                    hook=selected_hook,
                    script=script,
                    caption=caption,
                    status='📝 Script'
                )
                
                stats['success'] += 1
                logger.info(f"✅ Idée {i} traitée avec succès")
                
            except Exception as e:
                logger.error(f"❌ Erreur traitement idée {i} : {str(e)}")
                stats['failed'] += 1
        
        return stats


def main():
    parser = argparse.ArgumentParser(
        description='🤖 Générateur de contenu Instagram automatisé'
    )
    
    parser.add_argument(
        '--notion-db',
        type=str,
        help='Database ID Notion (ou utiliser NOTION_DATABASE_ID dans .env)'
    )
    
    parser.add_argument(
        '--batch-size',
        type=int,
        default=5,
        help='Nombre d\'idées à traiter (défaut: 5)'
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        default='output',
        help='Dossier de sortie (défaut: output)'
    )
    
    parser.add_argument(
        '--test-notion',
        action='store_true',
        help='Tester la connexion Notion et quitter'
    )
    
    parser.add_argument(
        '--model',
        type=str,
        default='claude',
        choices=['claude', 'openai'],
        help='Modèle IA à utiliser (défaut: claude)'
    )
    
    args = parser.parse_args()
    
    # Récupération configuration
    notion_token = os.getenv('NOTION_TOKEN')
    notion_db_id = args.notion_db or os.getenv('NOTION_DATABASE_ID')
    
    if not notion_token:
        logger.error("❌ NOTION_TOKEN manquant. Ajoutez-le dans .env")
        sys.exit(1)
    
    if not notion_db_id:
        logger.error("❌ NOTION_DATABASE_ID manquant. Utilisez --notion-db ou .env")
        sys.exit(1)
    
    # Initialisation
    generator = ContentGenerator(notion_token, notion_db_id)
    
    # Test de connexion
    if args.test_notion:
        success = generator.test_connection()
        sys.exit(0 if success else 1)
    
    # Traitement batch
    logger.info(f"🚀 Démarrage traitement batch ({args.batch_size} idées)")
    stats = generator.process_batch(
        batch_size=args.batch_size,
        output_dir=args.output_dir
    )
    
    # Résumé
    logger.info(f"\n📊 Statistiques batch:")
    logger.info(f"   Traitées : {stats['processed']}")
    logger.info(f"   Succès : {stats['success']}")
    logger.info(f"   Échecs : {stats['failed']}")
    
    sys.exit(0 if stats['failed'] == 0 else 1)


if __name__ == '__main__':
    main()
