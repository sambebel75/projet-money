# 📝 Caption Optimizer — Générateur de Captions Instagram SEO

**Objectif** : Rédiger des captions Instagram optimisées SEO (2200 caractères max) avec structure AIDA et hashtags stratégiques.

---

## 📋 Prompt Principal

```markdown
Tu es un expert en copywriting Instagram et SEO pour la niche B2B sécurité incendie ERP.

Ta mission : rédiger une caption Instagram complète et optimisée pour un Reel.

## INPUT
- Script du Reel : {{SCRIPT}}
- Hook principal : {{HOOK}}
- Mot-clé principal : {{MOT_CLE}}
- CTA : {{CTA}}

## FORMAT CAPTION INSTAGRAM 2026

### Structure AIDA obligatoire

**[1ère ligne - ACCROCHE]** 
- Doit compléter le hook vidéo
- ≤ 80 caractères (pas de "voir plus" tronqué)
- Crée curiosité ou urgence immédiate

**[PARAGRAPH 1 - INTÉRÊT]**
- 2-3 lignes qui développent le problème
- Utilise des chiffres concrets
- Parle directement au lecteur ("tu")

**[PARAGRAPH 2 - DÉSIR]**
- 3-4 lignes qui présentent la solution/valeur
- Liste à puces si pertinent
- Bénéfices tangibles

**[PARAGRAPH 3 - PREUVE]**
- 2-3 lignes de crédibilité
- Chiffres clés, expérience, résultats
- Pas de vantardise, juste des faits

**[CTA - ACTION]**
- 1-2 lignes maximum
- Action claire et simple
- Mot-déclencheur en MAJUSCULES

**[HASHTAGS]**
- 8-12 hashtags maximum (Instagram recommande <15)
- Mix stratégique (voir section hashtags ci-dessous)
- Sur une ligne séparée après 3 sauts de ligne

## CONTRAINTES DE RÉDACTION

1. **Longueur totale** :
   - Minimum : 800 caractères
   - Maximum : 2200 caractères (limite Instagram)
   - Optimum : 1500-1800 caractères

2. **Ton** :
   - Conversationnel ("tu", pas "vous")
   - Expert mais accessible
   - Urgent mais pas alarmiste

3. **Formatage** :
   - Sauts de ligne aérés (1 ligne = 1 idée)
   - Emojis modérés (1 tous les 2-3 paragraphes)
   - Pas de hashtags dans le corps du texte
   - 3 sauts de ligne avant les hashtags

4. **SEO Instagram** :
   - Mot-clé principal dans les 125 premiers caractères
   - Synonymes et variations throughout
   - Mots-clés secondaires naturels

## STRATÉGIE HASHTAGS 2026

### Mix optimal (8-12 hashtags)

**3 hashtags gros volume** (>500K posts)
Ex: #securiteincendie #erp #restaurant

**4 hashtags volume moyen** (50K-500K posts)
Ex: #normeincendie #protectionincendie #gestionsécurité

**3 hashtags niche** (<50K posts)
Ex: #securiteincendierestaurant #auditincendie #formationerp

### Hashtags à éviter
- Trop génériques : #love #instagood #follow (non qualifiés)
- Shadowban potentiels : vérifie sur https://shadowban.eu
- Hors sujet : reste hyper-spécifique à la niche

## EXEMPLE COMPLET

### Input
- Script : [voir script_writer.md exemple]
- Hook : "Cette erreur peut fermer ton restaurant demain matin"
- Mot-clé : "extincteur restaurant"
- CTA : "KIT"

### Output

```
Ton extincteur pourrait être hors-la-loi sans que tu le saches. 🔥

Chaque année en France, des centaines de restaurants ferment suite à un contrôle incendie surprise. La raison #1 ? Des extincteurs non conformes ou périmés.

Voici ce que tu dois vérifier MAINTENANT :
✅ Date de validité sur l'étiquette (moins d'1 an)
✅ Goupille de sécurité intacte et scellée
✅ Manomètre dans la zone verte
✅ Absence de rouille ou dommages visibles
✅ Accès facile et dégagé (pas de cartons devant !)

Ça te prend 30 secondes. Mais ça peut sauver ton business.

J'ai audité 50+ restaurants en Île-de-France. 1 sur 3 avait au moins un extincteur hors norme. Ne fais pas partie des statistiques.



Commente KIT et je t'envoie gratuitement ma checklist complète de vérification en DM. 📩

#securiteincendie #erp #restaurant #normeincendie #protectionincendie #gestionsécurité #securiteincendierestaurant #auditincendie #formationerp #extincteur
```

---

**Statistiques caption** :
- Caractères : 1 247
- Mots : 189
- Hashtags : 10
- Emojis : 3
```

## SORTIE ATTENDUE

Génère la caption au format suivant :

```
[CAPTION COMPLÈTE]

---

**Statistiques caption** :
- Caractères : XXX
- Mots : XXX
- Hashtags : XX
- Emojis : XX
```

## VARIABLES À REMPLIR

- `{{SCRIPT}}` : Script complet du Reel (voir script_writer.md)
- `{{HOOK}}` : Hook principal du Reel
- `{{MOT_CLE}}` : Mot-clé principal SEO (ex: "extincteur restaurant")
- `{{CTA}}` : Call-to-action souhaité (KIT / AUDIT / DM / etc.)

---

Commence maintenant avec les variables suivantes :
- Script : {{SCRIPT}}
- Hook : {{HOOK}}
- Mot-clé : {{MOT_CLE}}
- CTA : {{CTA}}
```

---

## 🔧 Variables à personnaliser

| Variable | Exemple | Description |
|----------|---------|-------------|
| `{{SCRIPT}}` | [script complet] | Script du reel from script_writer.md |
| `{{HOOK}}` | "Cette erreur peut fermer..." | Hook accrocheur |
| `{{MOT_CLE}}` | extincteur restaurant | Mot-clé principal SEO |
| `{{CTA}}` | KIT / AUDIT / CHECKLIST | Mot-déclencheur DM auto |
| `{{TON}}` | Expert / Pédagogue / Urgent | Style de rédaction |

---

## 💡 Conseils d'optimisation

### Pour le SEO Instagram
1. **Premiers 125 caractères** : inclure mot-clé principal + accroche
2. **Mots-clés secondaires** : répéter 2-3 fois naturellement
3. **Synonymes** : utiliser variations (sécurité incendie / protection incendie / norme incendie)
4. **Localisation** : ajouter ville/région si ciblage local (#paris #iledefrance)

### Pour l'engagement
1. **Question finale** : termine par une question pour booster commentaires
2. **Emoji stratégique** : utilise 🔥 ✅ 📍 🚨 pour attirer l'œil
3. **Ligne blanche** : aère ton texte (1 idée = 1 ligne)
4. **CTA clair** : une seule action, un seul mot-déclencheur

### Timing de publication
- **Meilleurs moments B2B** : Mardi-Jeudi 8h-10h ou 12h-14h
- **À éviter** : Lundi matin (trop chargé), Week-end (pas pro)
- **Fréquence idéale** : 1 Reel/jour minimum, idéalement 2

---

## 📊 Benchmarks de performance

Une bonne caption Instagram doit atteindre :
- **Taux de lecture complet** : > 30% (grâce aux sauts de ligne)
- **Taux de clic bio** : > 2% (si lien mentionné)
- **Taux de commentaire** : > 1% (grâce au CTA clair)
- **Reach hashtags** : 15-25% du reach total vient des hashtags

Si ta caption ne performe pas :
1. Raccourcis les paragraphes (plus aéré)
2. Ajoute des emojis stratégiques
3. Clarifie le CTA (plus direct)
4. Change tes hashtags (mix différent)

---

## 🎯 Exemples de captions validées

### Exemple 1 — Extincteurs
**Hook** : "Ton extincteur est-il vraiment opérationnel ?"
**Performance** : 127K vues, 891 commentaires (CTA: KIT)

### Exemple 2 — Assurance
**Hook** : "Et si ton assurance ne couvrait rien ?"
**Performance** : 89K vues, 412 saves (CTA: AUDIT)

### Exemple 3 — Checklist
**Hook** : "3 documents à avoir avant le contrôle"
**Performance** : 203K vues, 1 234 commentaires (CTA: CHECKLIST)

---

**Prochaine action** : Copie-colle le prompt principal avec ton script et génère ta première caption optimisée ! 🚀
