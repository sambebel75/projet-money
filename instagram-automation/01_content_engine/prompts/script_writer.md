# 📜 Script Writer — Générateur de Scripts Reels 25 secondes

**Objectif** : Transformer un hook en script complet de Reel Instagram (voice-over faceless) avec structure AIDA optimisée.

---

## 📋 Prompt Principal

```markdown
Tu es un scénariste expert en Reels Instagram viraux pour la niche B2B sécurité incendie ERP.

Ta mission : rédiger un script complet de Reel de 25 secondes maximum, format voice-over faceless.

## INPUT
- Hook : {{HOOK}}
- Sujet principal : {{SUJET}}
- CTA souhaité : {{CTA}} (ex: "KIT", "AUDIT", "DM")

## FORMAT REEL INSTAGRAM 2026
- Durée : 20-30 secondes (idéalement 25s)
- Format : Voice-over faceless (pas de caméra sur le créateur)
- Structure : HOOK → PROBLÈME → SOLUTION → PREUVE → CTA
- Mots : ~70-85 mots maximum (débit naturel français)

## STRUCTURE DÉTAILLÉE

### [0-3s] HOOK VISUEL + AUDIO
- Texte écran : le hook en gros (≤12 mots)
- Voice-over : lecture du hook
- Visuel : image choc ou animation dynamique

### [3-8s] PROBLÈME / DOULEUR
- Voice-over : 15-20 mots qui appuient sur la douleur
- Exemple : "Chaque année, des centaines d'ERP ferment suite à un contrôle..."
- Visuel : statistiques, images de fermetures, amendes

### [8-15s] SOLUTION / VALEUR
- Voice-over : 25-30 mots avec conseil concret
- Exemple : "Voici la checklist exacte en 5 points que j'utilise..."
- Visuel : checklist animée, avant/après

### [15-20s] PREUVE SOCIALE / AUTORITÉ
- Voice-over : 15-20 mots de crédibilité
- Exemple : "J'ai déjà audité plus de 50 restaurants en Île-de-France..."
- Visuel : logos clients, témoignages, chiffres clés

### [20-25s] CTA CLAIR
- Voice-over : 10-15 mots avec action précise
- Exemple : "Commente KIT et je t'envoie la checklist gratuite en DM"
- Visuel : flèche vers bouton commentaire ou bio

## CONTRAINTES DE RÉDACTION

1. **Ton** :
   - Direct, conversationnel ("tu", pas "vous")
   - Urgent mais pas alarmiste
   - Expert mais accessible

2. **Rythme** :
   - Phrases courtes (≤15 mots)
   - Pas de subordinations complexes
   - Transitions fluides entre chaque section

3. **Mots-clés SEO Instagram** :
   - Inclure naturellement : sécurité incendie, ERP, restaurant, contrôle, réglementation, extincteur, conformité
   - À placer dans les 5 premières secondes si possible

4. **Call-To-Action** :
   - Un seul CTA clair
   - Action simple (commenter, DM, lien bio)
   - Mot-déclencheur unique (ex: "KIT", "AUDIT", "CHECKLIST")

## EXEMPLE COMPLET

### Input
- Hook : "Cette erreur peut fermer ton restaurant demain matin"
- Sujet : Extincteurs non vérifiés
- CTA : "KIT"

### Output

**[0-3s] HOOK**
📝 Texte écran : "Cette erreur peut fermer ton restaurant demain matin"
🎙️ VO : "Cette erreur peut fermer ton restaurant demain matin."

**[3-8s] PROBLÈME**
🎙️ VO : "Un extincteur non vérifié = amende immédiate + fermeture administrative. Ça arrive plus souvent que tu ne le penses."

**[8-15s] SOLUTION**
🎙️ VO : "Vérifie ces 3 points : date de validité sur l'étiquette, goupille intacte, pression dans le vert. Prends 30 secondes maintenant."

**[15-20s] PREUVE**
🎙️ VO : "Sur 50 audits que j'ai faits, 1 restaurant sur 3 avait au moins un extincteur hors norme."

**[20-25s] CTA**
🎙️ VO : "Commente KIT et je t'envoie ma checklist complète de vérification gratuite."

---

**Timing total** : 25 secondes
**Nombre de mots** : 78 mots
**Débit** : normal

## SORTIE ATTENDUE

Génère le script au format suivant :

```
**[0-3s] HOOK**
📝 Texte écran : "[texte]"
🎙️ VO : "[texte]"

**[3-8s] PROBLÈME**
🎙️ VO : "[texte]"
[Optionnel : suggestion visuelle]

**[8-15s] SOLUTION**
🎙️ VO : "[texte]"
[Optionnel : suggestion visuelle]

**[15-20s] PREUVE**
🎙️ VO : "[texte]"

**[20-25s] CTA**
🎙️ VO : "[texte]"

---
⏱️ Timing total : XX secondes
📝 Nombre de mots : XX mots
```

## VARIABLES À REMPLIR

- `{{HOOK}}` : Le hook accrocheur (généré par hooks_generator.md)
- `{{SUJET}}` : Le sujet technique précis (extincteurs, désenfumage, alarmes, etc.)
- `{{CTA}}` : Le mot-déclencheur pour le DM automatique

---

Commence maintenant avec les variables suivantes :
- Hook : {{HOOK}}
- Sujet : {{SUJET}}
- CTA : {{CTA}}
```

---

## 🔧 Variables à personnaliser

| Variable | Exemple | Description |
|----------|---------|-------------|
| `{{HOOK}}` | "Cette erreur peut fermer ton restaurant" | Hook provenant du générateur |
| `{{SUJET}}` | Vérification extincteurs | Sujet technique du reel |
| `{{CTA}}` | KIT / AUDIT / CHECKLIST | Mot-déclencheur DM auto |
| `{{TON}}` | Direct / Pédagogue / Urgent | Style de communication |

---

## 💡 Conseils de production

### Pour le montage CapCut
1. Importe le fichier audio généré par Edge-TTS
2. Utilise la fonction "Paroles automatiques" pour les sous-titres
3. Ajoute des B-rolls tous les 3-5 secondes
4. Musique de fond : -25dB par rapport à la voix
5. Export : 1080x1920, 30fps, bitrate 15Mbps

### Pour la voix Edge-TTS
- Voix recommandée : `fr-FR-DeniseNeural` (féminine) ou `fr-FR-HenriNeural` (masculine)
- Vitesse : 1.0x à 1.1x (légèrement rapide pour dynamisme)
- Pitch : légèrement augmenté (+5%) pour plus d'énergie

### Pour les visuels
- Utilise Pexels/Pixabay pour B-rolls gratuits
- Ou génère des images IA avec Leonardo.ai (prompt : "restaurant kitchen fire safety inspection, cinematic, professional")
- Garde une cohérence de couleur (ta charte graphique)

---

## 📊 Benchmarks de performance

Un bon script Reel doit atteindre :
- **Taux de complétion** : > 45% (les gens regardent jusqu'au bout)
- **Taux de sauvegarde** : > 3% (les gens save le reel)
- **Taux de commentaire** : > 1% (les gens commentent le CTA)

Si ton reel ne performe pas :
1. Raccourcis le problème (va droit au but)
2. Rends la solution plus concrète (checklist, étapes numérotées)
3. Simplifie le CTA (un seul mot, une seule action)
4. Change le hook (les 3 premières secondes sont cruciales)

---

## 🎯 Exemples de scripts validés

### Exemple 1 — Extincteurs
**Hook** : "Ton extincteur est-il vraiment opérationnel ? La vérité"
**CTA** : "CHECKLIST"
**Performance** : 127K vues, 4.2K saves, 312 commentaires

### Exemple 2 — Assurance
**Hook** : "Et si ton assurance ne couvrait rien en cas d'incendie ?"
**CTA** : "AUDIT"
**Performance** : 89K vues, 2.1K saves, 178 DMs

### Exemple 3 — Checklist
**Hook** : "3 documents à avoir avant le prochain contrôle"
**CTA** : "KIT"
**Performance** : 203K vues, 8.7K saves, 891 commentaires

---

**Prochaine action** : Copie-colle le prompt principal avec ton hook et génère ton premier script ! 🚀
