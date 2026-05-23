# 📋 Checklist de lancement — Instagram UGC AI Machine

**Objectif** : Guide pas-à-pas pour lancer ton infrastructure Instagram automatisée en 7 jours.

---

## 🎯 Prérequis (avant J1)

### Matériel
- [ ] Ordinateur (Mac/PC/Linux) avec Python 3.10+ installé
- [ ] Connexion Internet stable
- [ ] Espace disque : 5GB minimum (pour modèles Whisper locaux)

### Comptes à créer (gratuits)
- [ ] **Notion** → https://notion.so (CRM & Content Database)
- [ ] **Buffer** → https://buffer.com (publication auto, 3 comptes gratuits)
- [ ] **ManyChat** → https://manychat.com (automation DM, 1000 contacts gratuits)
- [ ] **Systeme.io** → https://systeme.io (affiliation + tunnel de vente)
- [ ] **Leonardo.ai** → https://leonardo.ai (génération images, 150/jour gratuits)
- [ ] **CapCut** → https://capcut.com (montage vidéo gratuit)

### API Keys à récupérer
- [ ] **Anthropic API** (Claude) → https://console.anthropic.com (~$5 offerts)
- [ ] OU **OpenAI API** → https://platform.openai.com ($5 offerts)
- [ ] **Notion Integration** → https://www.notion.so/my-integrations

---

## 📅 Semaine 1 — J1 à J7

### J1 : Installation environnement

```bash
# 1. Cloner le repository
cd ~/Documents
git clone <repo-url> instagram-automation
cd instagram-automation

# 2. Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer .env
cp .env.example .env
# Éditer .env avec vos clés API
```

**Checklist J1 :**
- [ ] Repository cloné
- [ ] Environnement virtuel activé
- [ ] Dépendances installées (`pip list` pour vérifier)
- [ ] Fichier `.env` configuré avec clés API

---

### J2 : Configuration Notion Database

**Étapes :**
1. Se connecter sur Notion
2. Créer une nouvelle page "Content Engine"
3. Ajouter une base de données type "Table"
4. Copier les propriétés depuis `01_content_engine/templates/notion_database_schema.json`
5. Créer les 4 vues personnalisées (Pipeline, Idées, Calendrier, Performances)
6. Partager la base avec l'intégration API créée
7. Noter le Database ID dans `.env`

**Checklist J2 :**
- [ ] Page Notion créée
- [ ] Base de données configurée avec toutes les propriétés
- [ ] 4 vues personnalisées créées
- [ ] Intégration API connectée
- [ ] Database ID noté dans `.env`

**Test :**
```bash
python 08_scripts/content_generator.py --test-notion
```

---

### J3 : Test génération voix Edge-TTS

**Commande de test :**
```bash
python 03_video_production/tts_generator.py \
  --text "Cette erreur peut fermer ton restaurant demain matin" \
  --output test_audio.mp3 \
  --voice fr-FR-DeniseNeural \
  --rate +5%
```

**Vérifications :**
- [ ] Fichier `test_audio.mp3` généré
- [ ] Durée : ~3-4 secondes
- [ ] Qualité audio : claire, naturelle
- [ ] Taille fichier : <100 KB

**Astuce :** Pour Instagram Reel, utilisez :
- Voice : `fr-FR-DeniseNeural`
- Rate : `+5%` à `+10%` (plus dynamique)
- Pitch : `+0Hz` (normal)

---

### J4 : Test Whisper sous-titres

**Commande de test :**
```bash
python 03_video_production/subtitle_generator.py \
  --audio test_audio.mp3 \
  --output test_subtitles.srt \
  --model small \
  --language fr
```

**Vérifications :**
- [ ] Fichier `test_subtitles.srt` généré
- [ ] Sous-titres synchronisés avec l'audio
- [ ] Maximum 2 lignes par sous-titre
- [ ] Longueur max 42 caractères par ligne

**Import dans CapCut :**
1. Ouvrir CapCut Desktop
2. Importer audio + vidéo
3. Click droit sur timeline → "Auto Captions" → "Import SRT"
4. Sélectionner `test_subtitles.srt`
5. Ajuster style (police, couleur, ombre)

---

### J5 : Création des 10 premiers scripts

**Processus :**
1. Ouvrir `01_content_engine/prompts/hooks_generator.md`
2. Copier-coller le prompt dans Claude/ChatGPT
3. Générer 30 hooks
4. Sélectionner les 10 meilleurs
5. Pour chaque hook, utiliser `script_writer.md` pour générer le script complet

**Exemple de structure :**
| N° | Hook | Sujet | CTA | Statut |
|----|------|-------|-----|--------|
| 1 | "Cette erreur peut fermer ton restaurant..." | Extincteurs | KIT | ✅ Script |
| 2 | "Pourquoi 80% des ERP sont hors-norme..." | Réglementation | AUDIT | ✅ Script |
| 3 | "3 documents à avoir avant le contrôle" | Checklist | CHECKLIST | ✅ Script |
| ... | ... | ... | ... | ... |

**Checklist J5 :**
- [ ] 30 hooks générés
- [ ] 10 hooks sélectionnés
- [ ] 10 scripts complets rédigés
- [ ] 10 captions optimisées générées
- [ ] 10 listes de hashtags préparées

---

### J6 : Montage des 3 premiers Reels

**Workflow CapCut :**
1. **Importer** : Audio MP3 (généré par Edge-TTS)
2. **Importer** : B-rolls (Pexels gratuit ou Leonardo.ai)
3. **Auto-captions** : Importer fichier SRT (généré par Whisper)
4. **Style** : Police bold (Impact/Arial), blanc avec outline noir
5. **Musique** : Ajouter musique trending (-25dB volume)
6. **Export** : 1080x1920, 30fps, 15Mbps bitrate

**Durée cible :** 20-30 secondes maximum

**Checklist J6 :**
- [ ] Reel #1 monté et exporté
- [ ] Reel #2 monté et exporté
- [ ] Reel #3 monté et exporté
- [ ] Vérification qualité (audio, sous-titres, transitions)
- [ ] Fichiers nommés correctement (reel_01_extincteurs.mp4, etc.)

---

### J7 : Programmation publication semaine 2

**Via Buffer (gratuit) :**
1. Se connecter sur https://buffer.com
2. Connecter compte Instagram Business
3. Upload des 3 Reels
4. Ajouter captions + hashtags
5. Programmer :
   - Reel #1 : Mardi 8h30
   - Reel #2 : Jeudi 12h30
   - Reel #3 : Samedi 10h00

**Via Meta Business Suite (alternative) :**
1. https://business.facebook.com
2. Section "Contenu" → "Créer un Reel"
3. Upload + programmation native Instagram

**Checklist J7 :**
- [ ] Buffer connecté à Instagram
- [ ] 3 Reels programmés
- [ ] Captions ajoutées avec hashtags
- [ ] Lien bio mis à jour (Linktree gratuit ou Systeme.io)
- [ ] ManyChat configuré avec séquence DM (mot-clé: KIT)

---

## 📅 Semaine 2 — J8 à J14 (Premier contenu live)

### Objectifs Semaine 2
- [ ] J8 : Publication Reel #1 ✅
- [ ] J9 : Monitoring commentaires + DMs
- [ ] J10 : Publication Reel #2 ✅
- [ ] J11 : Analyse premières performances
- [ ] J12 : Publication Reel #3 ✅
- [ ] J13 : Optimisation selon retours
- [ ] J14 : Premier outreach DM manuel (10 prospects)

### KPIs à suivre
- Vues totales (objectif : 5 000+)
- Taux de complétion (objectif : >40%)
- Commentaires (objectif : 20+)
- DMs automatiques (objectif : 10+)

---

## 📅 Semaine 3 — J15 à J21 (Scale contenu)

### Objectifs Semaine 3
- [ ] Publication quotidienne (1 reel/jour)
- [ ] Outreach DM : 20 prospects/jour
- [ ] Ajustement stratégie hashtags
- [ ] Test 2 nouveaux formats (carrousel, text reel)

### Production batch
- [ ] Générer 20 nouveaux scripts (J15)
- [ ] Monter 10 reels en batch (J16-J17)
- [ ] Programmer semaine 4 (J18)

---

## 📅 Semaine 4 — J22 à J30 (Monétisation)

### Objectifs Semaine 4
- [ ] J22 : Activation liens affiliés en bio
- [ ] J25 : Lancement produit digital #1 (17€)
- [ ] J28 : Premiers closing calls services DFY
- [ ] J30 : Analyse complète + planification mois 2

### Revenus cibles (fin M1)
- Affiliation : 100-300€
- Produits digitaux : 200-500€
- Services DFY : 0-1000€ (1-2 clients)
- **Total : 300-1800€**

---

## 🛠️ Scripts utilitaires à tester

### Content Generator (automatisation complète)
```bash
python 08_scripts/content_generator.py \
  --notion-db <DATABASE_ID> \
  --batch-size 5 \
  --output-dir content_batch_1
```

### Hashtag Researcher
```bash
python 08_scripts/hashtag_researcher.py \
  --niche "securite incendie" \
  --audience "restaurants" \
  --output hashtags_restaurants.txt
```

### Trend Scraper
```bash
python 08_scripts/trend_scraper.py \
  --sources reddit,rss \
  --keywords "incendie,erp,restaurant" \
  --output trends_week_1.json
```

---

## ⚠️ Problèmes courants et solutions

### Problème : Whisper trop lent
**Solution :** Utiliser `faster-whisper` au lieu de `whisper`
```bash
pip uninstall openai-whisper
pip install faster-whisper
```

### Problème : Erreur API Notion
**Solution :** Vérifier que :
1. L'intégration est bien partagée avec la database
2. Le token commence par `secret_`
3. Le database ID est correct (32 caractères)

### Problème : ManyChat n'envoie pas les DMs
**Solution :** Vérifier :
1. Compte Instagram en mode "Business" ou "Creator"
2. ManyChat connecté correctement
3. Mot-clé configuré dans le Growth Tool
4. Respect de la règle des 24h

### Problème : Reels ne performent pas (<100 vues)
**Solution :**
1. Changer les hooks (plus d'urgence/curiosité)
2. Réduire durée (<25 secondes)
3. Améliorer qualité sous-titres (plus gros, plus contrastés)
4. Changer horaires de publication

---

## 📞 Ressources et support

### Documentation officielle
- Notion API : https://developers.notion.com/docs
- Edge-TTS : https://github.com/rany2/edge-tts
- Whisper : https://github.com/openai/whisper
- Buffer API : https://buffer.com/developers
- ManyChat : https://manychat.github.io/manychat-doc/

### Communautés
- Reddit r/InstagramMarketing
- Facebook Group "Instagram Reels Tips 2026"
- Discord "Creator Economy Hub"

---

## ✅ Checklist finale (fin J30)

### Infrastructure
- [ ] Notion Database opérationnelle
- [ ] Tous les scripts Python testés
- [ ] Workflows Make/n8n configurés
- [ ] ManyChat automation active

### Contenu
- [ ] 30 Reels publiés (1/jour)
- [ ] 100+ hooks testés
- [ ] 50+ captions optimisées
- [ ] Bibliothèque de B-rolls constituée

### Audience
- [ ] 1 000+ followers
- [ ] 50 000+ vues totales
- [ ] 4%+ engagement rate
- [ ] 50+ DMs reçus

### Monétisation
- [ ] 3 programmes d'affiliation actifs
- [ ] 1 produit digital lancé
- [ ] 1 offre de service DFY
- [ ] Premier euro encaissé ✅

---

**🎉 Félicitations ! Tu as maintenant une machine d'acquisition Instagram 100% automatisée.**

**Prochaine étape** : Scale à 2 reels/jour et ajoute de nouveaux canaux (TikTok, LinkedIn, YouTube Shorts).
