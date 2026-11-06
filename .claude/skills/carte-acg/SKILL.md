---
name: carte-acg
description: Créer, modifier, chercher ou équilibrer des cartes et des mondes d'ACG (raretés, notes, postes, époques, tags, nouveau monde). À utiliser quand Harlem parle d'ajouter ou changer un personnage, une version, une rareté, une note, un monde, ou de chercher des persos et époques pour un animé.
---

# Cartes ACG

Une carte = **un personnage à un moment précis de l'œuvre**. Règles complètes : `references/raretes-et-epoques.md` (lis-le avant d'ajouter ou de changer une rareté).

## Format (ligne JSON `RAW` dans `index.html`)
`[id, monde, nom, version, classe, poste, rareté, note, [tags], "nom complet"]`
- `id` : `<monde>-<nom>-<version>` en minuscules sans accents, tirets (`op-monkey-arc-wano`). **Ne change jamais l'id d'une carte existante** (sauvegardes des joueurs).
- `monde` : clé de `MONDES` (`op`, `na`, `db`, `bl`, `jjk`, …).
- `classe` : Bagarreur, Épéiste, Mage, Tireur, Healer, Support. `poste` : Tank, DPS, Distance, Soutien.
- Soutien : sa classe fixe son effet (`SUPK` : Healer soigne, Support renforce, Bagarreur brise la défense, Épéiste critique, Mage spécial, Tireur couvre).
- `rareté` : N, R, SR, SSR, UR, LR. `note` : choisie à la main, dans la bande de la rareté. Les 6 stats (PV, ATT, DEF, VIT, TEC, POU) sont calculées par `genStats`, sauf UR/LR fixées à la main dans `URS_FIX`.
- Tags : 3 à 5 (Capitaine, Sensei, Saiyan…) ; trois cartes du même tag donnent un bonus d'équipe.
- Nom de version affiché : table `VL` (« Forme · Époque »).

## Ajouter une carte : checklist
1. Cartes voisines du monde : Grep l'id du monde dans `RAW`, liste la rareté et la note de chacune.
2. Choisis l'époque (règles d'époque), la rareté (rang dans le monde) et la note (entre ses voisines, dans la bande).
3. Ajoute la ligne dans `RAW`, l'entrée `VL`, `URS_FIX` si UR/LR, une ligne `SPM` si SSR/UR (attaque spéciale par défaut : couleurs et nom), `PRO` si utile.
4. Image : skill `images-cartes`. Sans image la carte existe mais l'album la marque comme manquante.
5. Contrôle : roster chargé sans erreur console, aucune rareté ne chevauche la bande d'une autre, quotas du monde respectés. Si `simulations/verif-roster.py` existe en local, lance-le.
6. Signale « PDF des règles à mettre à jour » si une rareté, une bande ou un quota change.

## Chercher des persos pour un animé
1. Lis les cartes existantes du monde (Grep `RAW`), ne propose jamais un doublon (même perso + même époque).
2. Cherche sur le web les arcs et exploits (wikis de l'œuvre) ; propose 5 à 10 candidats : perso, époque (moment réel, jamais « Légendaire »), rareté, note, poste, classe, justification en une ligne.
3. Respecte le profil cible d'un monde : au moins 12 cartes, 1 UR (si le sommet est présent), 2 SSR, 3 SR, 3 R, 3-4 N, au moins 1 Tank et 1 Soutien.
4. Présente sous forme de tableau court. Harlem valide avant tout codage.

## Interdits
- Changer la rareté d'une carte déjà en jeu sans accord de Harlem (elle change pour tous les joueurs).
- Créer une 3e UR dans un monde : une carte plus forte que les 2 UR devient LR (saison ou événement).
- Toucher à l'économie (taux de boosters, garanties) : hors catégorie, voir `JOURNAL.md` et signaler.
