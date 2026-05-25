# 🚀 Instagram UGC AI Machine — Code Repository

> **Infrastructure 100% automatisée** pour transformer Instagram en machine d'acquisition B2B sans budget initial.
>
> Stack : Python 3.10+ | 100% free tier | Niche : Sécurité incendie ERP

---

## 🎯 Vue d'ensemble

Ce repository contient l'intégralité du code et des templates pour :
- ✅ Générer automatiquement des scripts de Reels viraux
- ✅ Produire des voix off IA gratuites (Edge-TTS)
- ✅ Générer des sous-titres automatiques (Whisper)
- ✅ Publier sur Instagram via Buffer/Meta Business Suite
- ✅ Automatiser les DMs avec ManyChat Free
- ✅ Suivre les performances dans Notion + Google Sheets

---

## 🛠️ Stack technique 100% gratuite

| Fonction | Outil | Lien | Limite free tier |
|----------|-------|------|------------------|
| **IA Texte** | Claude.ai / ChatGPT / Gemini | [claude.ai](https://claude.ai) | Rotation entre les 3 |
| **Workflow** | Make | [make.com](https://make.com) | 1000 ops/mois |
| **Voix IA** | Edge-TTS (Microsoft) | Built-in Python | Illimité |
| **Sous-titres** | Whisper Local | Open Source | Illimité |
| **Montage** | CapCut Desktop | [capcut.com](https://capcut.com) | Illimité |
| **Images IA** | Leonardo.ai / Bing | [leonardo.ai](https://leonardo.ai) | 150 img/jour |
| **Publication** | Buffer / Meta Suite | [buffer.com](https://buffer.com) | 3 comptes, 10 posts |
| **CRM** | Notion | [notion.so](https://notion.so) | Illimité perso |
| **DM Auto** | ManyChat | [manychat.com](https://manychat.com) | 1000 contacts |
| **Affiliation** | Systeme.io | [systeme.io](https://systeme.io) | 60% récurrent |

---

## 🚀 Quick Start en 7 étapes

### Étape 1 : Cloner le repository
```bash
cd ~/Documents
git clone <repo-url> instagram-automation
cd instagram-automation
```

### Étape 2 : Installer Python 3.10+
```bash
python3 --version  # Doit afficher 3.10 ou supérieur
```

### Étape 3 : Créer un environnement virtuel
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### Étape 4 : Installer les dépendances
```bash
pip install -r requirements.txt
```

### Étape 5 : Configurer les variables d'environnement
```bash
cp .env.example .env
# Éditer .env avec vos clés API
```

### Étape 6 : Créer les comptes gratuits
- [ ] [Notion](https://notion.so) → Créer une page + base de données
- [ ] [Buffer](https://buffer.com) → Connecter compte Instagram Business
- [ ] [Make](https://make.com) → Créer un compte gratuit
- [ ] [Systeme.io](https://systeme.io) → S'inscrire au programme affilié
- [ ] [Leonardo.ai](https://leonardo.ai) → Créer un compte gratuit

### Étape 7 : Lancer le générateur de contenu
```bash
python 08_scripts/content_generator.py
```

---

## 📁 Structure du projet

```
instagram-automation/
├── README.md                    # Ce fichier
├── .env.example                 # Template de configuration
├── requirements.txt             # Dépendances Python
│
├── 01_content_engine/           # Moteur de contenu
│   ├── prompts/                 # Prompts IA pour génération
│   │   ├── hooks_generator.md
│   │   ├── script_writer.md
│   │   ├── caption_optimizer.md
│   │   ├── dm_sequence.md
│   │   └── hashtag_strategy.md
│   └── templates/
│       └── notion_database_schema.json
│
├── 02_workflow_automation/      # Workflows Make/n8n
│   └── make_scenario_blueprint.json
│
├── 03_video_production/         # Production vidéo
│   ├── tts_generator.py         # Génération voix Edge-TTS
│   ├── subtitle_generator.py    # Sous-titres Whisper
│   └── batch_processor.py       # Traitement par lots
│
├── 04_publishing_distribution/  # Publication
│   ├── buffer_publisher.py      # Publication via Buffer
│   └── meta_business_api.py     # Alternative Meta directe
│
├── 05_monetization/             # Monétisation
│   ├── affiliate_programs.md    # Programmes d'affiliation
│   ├── digital_products/        # Produits digitaux
│   │   ├── product_1_hooks_pack.md
│   │   ├── product_2_prompts_pack.md
│   │   └── product_3_notion_template.md
│   └── dfy_services/            # Services Done-For-You
│       ├── pack_demarrage_497.md
│       ├── pack_mensuel_997.md
│       └── pack_premium_2997.md
│
├── 06_dm_outreach/              # Outreach DM
│   ├── dm_templates_5_variantes.md
│   ├── prospect_list_template.csv
│   └── follow_up_sequences.md
│
├── 07_analytics/                # Analytics
│   ├── kpi_dashboard.md
│   ├── google_sheets_template.md
│   └── weekly_review_template.md
│
└── 08_scripts/                  # Scripts utilitaires
    ├── content_generator.py     # Script principal
    ├── trend_scraper.py         # Scraping tendances
    ├── engagement_pod_helper.py
    └── hashtag_researcher.py
```

---

## 🔑 Variables d'environnement requises

Copiez `.env.example` vers `.env` et remplissez :

```bash
# API Keys (gratuites avec crédits offerts)
ANTHROPIC_API_KEY=sk-ant-...
# ou
OPENAI_API_KEY=sk-...

# Notion (créez une integration sur https://www.notion.so/my-integrations)
NOTION_TOKEN=secret_...
NOTION_DATABASE_ID=votre_database_id

# Buffer (optionnel, pour publication auto)
BUFFER_ACCESS_TOKEN=...
BUFFER_ID=...

# Instagram Business (via Facebook Developer)
INSTAGRAM_BUSINESS_ID=...
FACEBOOK_PAGE_ID=...
```

---

## 📅 Roadmap 30 jours

### Semaine 1 (J1-J7) : Setup infrastructure
- [ ] J1 : Installation environnement + comptes gratuits
- [ ] J2 : Configuration Notion Database
- [ ] J3 : Test génération voix Edge-TTS
- [ ] J4 : Test Whisper sous-titres
- [ ] J5 : Création 10 premiers scripts
- [ ] J6 : Montage 3 premiers Reels
- [ ] J7 : Programmation publication semaine 2

### Semaine 2 (J8-J14) : Premier contenu live
- [ ] J8 : Publication Reel #1
- [ ] J9 : Publication Reel #2
- [ ] J10 : Publication Reel #3
- [ ] J11 : Analyse premières performances
- [ ] J12 : Optimisation hooks/CTAs
- [ ] J13 : Setup ManyChat réponses auto
- [ ] J14 : Premier outreach DM (10 prospects)

### Semaine 3 (J15-J21) : Scale contenu
- [ ] J15-J21 : Publication quotidienne (1 reel/jour)
- [ ] Outreach DM : 20 prospects/jour
- [ ] Ajustement stratégie hashtags
- [ ] Test 2 nouveaux formats

### Semaine 4 (J22-J30) : Monétisation
- [ ] J22 : Activation liens affiliés en bio
- [ ] J25 : Lancement produit digital #1 (17€)
- [ ] J28 : Premiers closing calls services DFY
- [ ] J30 : Analyse complète + planification mois 2

---

## 🎬 Formats de contenu recommandés

### Format A — "Faceless Voice-Over" (60% du contenu)
- Voix IA Edge-TTS (fr-FR-DeniseNeural)
- B-roll IA généré ou Pexels gratuit
- Sous-titres animés CapCut
- Durée : 20-30 secondes

### Format B — "Carrousel Animé" (30% du contenu)
- 8-10 slides Canva
- Conversion vidéo verticale CapCut
- Transition automatique
- Durée : 15-25 secondes

### Format C — "Text Reel" (10% du contenu)
- Texte dynamique sur fond coloré
- Musique trending Instagram
- Durée : 7-15 secondes

---

## 💰 Modèles de monétisation

### 1. Affiliation outils IA (cashflow immédiat)
- Systeme.io : 60% récurrent
- HeyGen : 25% récurrent
- Notion : 50% premier paiement
- Make : 20% récurrent

### 2. Produits digitaux
- "100 hooks viraux B2B" → 17€
- "Pack 50 prompts ChatGPT" → 27€
- "Template Notion Content Engine" → 37€

### 3. Services Done-For-You
- Pack démarrage (497€) : 12 reels + setup
- Pack mensuel (997€) : 30 reels/mois
- Pack premium (2997€) : infrastructure complète

---

## 📊 KPIs à suivre

| Métrique | Objectif M1 | Objectif M2 | Objectif M3 |
|----------|-------------|-------------|-------------|
| Followers | 1 000 | 5 000 | 10 000 |
| Vues/mois | 50 000 | 200 000 | 500 000 |
| Engagement | 4% | 5% | 6% |
| DMs reçus/jour | 5 | 20 | 50 |
| Revenus/mois | 500€ | 2 000€ | 5 000€ |

---

## ⚠️ Contraintes importantes

1. **Tout en français** sauf noms de fichiers techniques
2. **Zéro dépendance payante** dans les scripts
3. **Code Python 3.10+** propre, commenté, avec gestion d'erreurs
4. **Variables d'environnement** pour toutes les clés API
5. **Logs clairs** dans tous les scripts
6. **Respect des rate limits** free tiers

---

## 🆘 Support & Ressources

- Documentation Notion API : https://developers.notion.com
- Edge-TTS GitHub : https://github.com/rany2/edge-tts
- Whisper Documentation : https://github.com/openai/whisper
- Buffer API : https://buffer.com/developers
- Make Documentation : https://www.make.com/en/help

---

## 📝 Licence

MIT License — Utilisation commerciale autorisée

---

**Prochaine action** : Suivez le Quick Start ci-dessus et commencez par J1 ! 🚀
