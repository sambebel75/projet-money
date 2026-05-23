# 🤖 DM Sequence — Automatisation des Messages Privés

**Objectif** : Créer des séquences DM automatisées (ManyChat free tier) pour qualifier les prospects et convertir en ventes.

---

## 📋 Prompt Principal

```markdown
Tu es un expert en automatisation DM Instagram (ManyChat) spécialisé dans la conversion B2B sécurité incendie ERP.

Ta mission : créer une séquence DM complète en 4 messages pour qualifier un prospect qui a commenté un Reel avec le mot-déclencheur.

## CONTEXTE
- Plateforme : ManyChat Free tier (1000 contacts max)
- Déclencheur : Commentaire sur Reel avec mot-clé (KIT / AUDIT / CHECKLIST)
- Objectif : Qualifier + prendre RDV ou vendre produit digital
- Ton : conversationnel, pas de robot corporate

## STRUCTURE DE LA SÉQUENCE

### Message 1 — Livraison immédiate (automatique, <1 min)
- Remerciement personnalisé
- Livraison du promis (lien KIT/CHECKLIST)
- Question ouverte légère pour engager

### Message 2 — Qualification douce (J+1, manuel ou auto)
- Prise de nouvelles
- Question de qualification (taille ERP, secteur, problématique)
- Pas de vente directe

### Message 3 — Valeur ajoutée (J+3)
- Conseil personnalisé selon réponse M2
- Étude de cas ou preuve sociale
- Ouverture vers solution payante

### Message 4 — Call-to-action final (J+5)
- Proposition claire (audit gratuit / produit / service)
- Lien de réservation (Calendly gratuit)
- Urgence douce (places limitées)

## CONTRAINTES

1. **Longueur** :
   - Message 1 : ≤ 300 caractères
   - Message 2-4 : ≤ 500 caractères
   - Total séquence : ≤ 1700 caractères

2. **Ton** :
   - Conversationnel ("tu", pas "vous")
   - Friendly mais pro
   - Pas de spam, pas de pression

3. **Personnalisation** :
   - Utilise {{first_name}} si disponible
   - Référence au Reel commenté
   - Adaptation selon réponse qualification

4. **Conformité Instagram** :
   - Pas de liens externes dans M1 (risque shadowban)
   - Maximum 1 lien par message
   - Respecter les 24h rule (ManyChat free)

## EXEMPLE COMPLET

### Déclencheur
Utilisateur commente "KIT" sur le Reel "3 documents à avoir avant le contrôle"

### Séquence

**MESSAGE 1 (automatique, <1 min)**
```
Salut {{first_name}} ! 👋

Merci pour ton commentaire sur mon Reel ! Voici la checklist complète de vérification extincteurs que je t'ai promise :

[Lien Systeme.io vers lead magnet]

Dis-moi, tu es proprio de restaurant ou d'un autre type d'ERP ?
```

**MESSAGE 2 (J+1)**
```
Salut {{first_name}}, j'espère que la checklist t'est utile ! 

Je suis curieux : ton établissement, il fait quelle taille ? 
- Moins de 50 personnes ?
- Entre 50 et 200 ?
- Plus de 200 ?

(Ça me permet de te conseiller au mieux !)
```

**MESSAGE 3 (J+3, selon réponse "moins de 50")**
```
Parfait, merci pour l'info ! 

Les petits ERP comme le tien ont des obligations spécifiques (souvent plus simples que les gros). 

Je viens justement d'aider un resto à Paris à se mettre en conformité en 48h chrono. 

Tu as déjà eu un contrôle incendie ou c'est ta première année ?
```

**MESSAGE 4 (J+5)**
```
{{first_name}}, je te propose un truc :

Je fais 3 audits gratuits cette semaine pour aider les proprios d'ERP à identifier les points critiques avant le prochain contrôle.

Ça te dit que je jette un œil rapide à ta config ? (15 min, sans engagement)

Réserve ton créneau ici : [Calendly]

Il me reste 2 places dispo !
```

---

**Taux de conversion moyen** : 12-18% des commentaires → audit gratuit → 30% → client payant

## SORTIE ATTENDUE

Génère la séquence au format suivant :

```
## DÉCLENCHEUR
- Mot-clé : {{MOT_CLE}}
- Reel : {{REEL}}
- Audience cible : {{AUDIENCE}}

## SÉQUENCE DM

### MESSAGE 1 (automatique, <1 min)
[Texte complet du message]
---
Caractères : XXX

### MESSAGE 2 (J+1)
[Texte complet du message]
---
Caractères : XXX

### MESSAGE 3 (J+3)
[Texte complet du message]
---
Caractères : XXX

### MESSAGE 4 (J+5)
[Texte complet du message]
---
Caractères : XXX

## VARIABLES MANYCHAT À CONFIGURER
- {{first_name}} : Prénom de l'utilisateur
- {{last_input}} : Dernière réponse utilisateur
- {{tag_erp_type}} : Type d'ERP (restaurant/hôtel/commerce)
- {{tag_taille}} : Taille (<50 / 50-200 / >200)

## LIENS À PRÉPARER
1. Lead magnet (Systeme.io) : ...
2. Calendly audit gratuit : ...
3. Page de vente produit digital : ...
```

## VARIABLES À REMPLIR

- `{{MOT_CLE}}` : Mot-déclencheur (KIT / AUDIT / CHECKLIST)
- `{{REEL}}` : Sujet du Reel déclencheur
- `{{AUDIENCE}}` : Cible principale (restaurants / hôtels / commerces)
- `{{LEAD_MAGNET}}` : Produit offert en M1
- `{{OFFRE_PRINCIPALE}}` : Offre à vendre (audit / formation / service)

---

Commence maintenant avec les variables suivantes :
- Mot-clé : {{MOT_CLE}}
- Reel : {{REEL}}
- Audience : {{AUDIENCE}}
```

---

## 🔧 Variables à personnaliser

| Variable | Exemple | Description |
|----------|---------|-------------|
| `{{MOT_CLE}}` | KIT / AUDIT / CHECKLIST | Mot-déclencheur commentaire |
| `{{REEL}}` | Extincteurs / Alarmes / etc. | Sujet du reel déclencheur |
| `{{AUDIENCE}}` | Restaurants / Hôtels | Type d'ERP ciblé |
| `{{LEAD_MAGNET}}` | Checklist PDF / Guide | Lead magnet offert |
| `{{OFFRE_PRINCIPALE}}` | Audit gratuit / Formation | Offre de vente |

---

## 💡 Configuration ManyChat Free Tier

### Étape 1 : Créer le Growth Tool
1. Dashboard ManyChat → Growth Tools → New Growth Tool
2. Choose "Instagram Comment" comme trigger
3. Configure : "When someone comments with specific keyword"
4. Keyword : KIT (ou autre)
5. Select Reels : All ou spécifique

### Étape 2 : Configurer le Message 1
1. Dans le Flow créé, ajoute un message Instagram
2. Utilise les Custom Fields {{first_name}}
3. Ajoute le bouton avec lien vers lead magnet
4. Active "Wait for user response"

### Étape 3 : Ajouter les Tags
1. Crée des tags : "Lead_KIT", "Lead_AUDIT", "Prospect_Qualifié"
2. Ajoute automatiquement le tag dans le Message 1
3. Utilise les tags pour segmenter tes envois

### Étape 4 : Automatiser les Messages 2-4
**Option A (gratuite, manuelle)** :
- ManyChat free ne permet pas d'automation temporelle avancée
- Envoie manuel via l'onglet "Contacts" chaque jour

**Option B (payante, automatique)** :
- Upgrade vers ManyChat Pro (~15$/mois)
- Crée des automatisations "Wait X days" entre messages

### Étape 5 : Suivi des performances
Dashboard ManyChat → Analytics :
- Taux d'ouverture M1 : objectif > 85%
- Taux de réponse M2 : objectif > 40%
- Taux de conversion M4 : objectif > 15%

---

## 📊 Benchmarks de performance

Une bonne séquence DM B2B doit atteindre :
- **Taux d'ouverture M1** : > 85% (automatique, instantané)
- **Taux de réponse M2** : > 40% (question simple)
- **Taux de clic lien M3** : > 20% (valeur pertinente)
- **Taux de réservation M4** : > 10-15% (offre irrésistible)

Si ta séquence ne performe pas :
1. Raccourcis les messages (plus digest)
2. Personnalise davantage (utilise le prénom, référence au reel)
3. Adoucis le ton (moins "vente", plus "conseil")
4. Change l'offre (plus alignée avec la douleur)

---

## 🎯 Exemples de séquences validées

### Séquence "KIT" — Checklist extincteurs
- 312 commentaires → 198 réponses M2 (63%) → 47 audits réservés (24%) → 14 clients (30%)
- **ROI** : 14 clients x 997€ = 13 958€

### Séquence "AUDIT" — Audit gratuit
- 178 commentaires → 134 réponses M2 (75%) → 52 audits réservés (39%) → 19 clients (36%)
- **ROI** : 19 clients x 997€ = 18 943€

### Séquence "CHECKLIST" — Documents contrôle
- 891 commentaires → 521 réponses M2 (58%) → 98 audits réservés (19%) → 31 clients (32%)
- **ROI** : 31 clients x 997€ = 30 907€

---

## ⚠️ Règles Instagram à respecter

### À faire ✅
- Attendre que l'utilisateur commente en premier (pas de cold DM)
- Répondre dans les 24h (règle ManyChat free tier)
- Personnaliser avec le prénom
- Apporter de la valeur avant de vendre

### À éviter ❌
- Envoyer des liens externes dans le premier message (risque shadowban)
- Spammer (max 1 message/jour après M1)
- Messages trop longs (>500 caractères)
- Ton trop commercial/robotique

---

**Prochaine action** : Copie-colle le prompt principal et configure ta première séquence ManyChat ! 🚀
