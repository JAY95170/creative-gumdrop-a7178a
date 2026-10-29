# BRIEF — prochaine mise à jour (à partir de v97)

Ordre conseillé, une version par bloc, tests mobile + PC à chaque fois.

## v98 — Roster +200 (priorité de Harlem)
Source : `roster-200.md` + `roster200.json` (id, monde, nom, nom complet, version, classe, poste, rareté, justification, image oui/non).
1. Nouveaux mondes à déclarer (code → nom, couleur) : ss Saint Seiya · ft Fairy Tail · aot L'Attaque des Titans · fma Fullmetal Alchemist · jo JoJo's Bizarre Adventure · csm Chainsaw Man · sl Solo Leveling · opm One Punch Man · fr Frieren. Vérifier filtres, compteurs, SBC « monde du jour », boosters de monde.
2. Pour chaque carte : fixer la note dans la tranche de sa rareté (N 40–55, R 50–64, SR 61–72, SSR 72–89, UR 87–95) en respectant l'ordre strict du monde et les cartes déjà en jeu (repères cités dans la justification). Profil de stats tiré de l'anime ; UR : stats fixées à la main (`URS_FIX`).
3. Tags : 3 à 5 par carte, réutiliser les tags existants quand c'est juste (Capitaine, Épée…) ; nouveaux tags de groupe (ex. [Chevalier d'or], [Espada], [Lune supérieure], [Bataillon d'exploration], [Homonculus], [Classe S]…). Tag de jeu = porté par ≥ 4 cartes.
4. Ajouter dans `RAW`, ajouter les ids illustrés au Set `ART` (183 images déjà dans `images/`). Les 17 cartes ✗ restent « visuel à venir ».
5. Garder l'économie : vérifier la taille de l'album (186 → 386 cartes) contre les paliers d'album (25/50/100/complet) et la récompense « monde complet » ; le rythme « album complet ≈ 3 mois » va s'allonger → le signaler à Harlem avec une simulation, ne rien changer sans son accord.
6. Multivers : Trigun/Hellsing/Black Lagoon dépassent 6 cartes → hors Multivers.

## v99 — Bugs et ergonomie (retours de Harlem du 29/10)
- Mémoriser le sous-onglet actif (ex. Vendre) quand on change d'onglet et qu'on revient.
- Pastille sur les onglets quand une récompense est à récupérer.
- Boutique : le fond/bord de l'image du booster dépasse → l'image doit couvrir tout le sachet.
- Moins de scrolls/slides (Draft, Bilans) sans réduire la lisibilité des cartes.
- Filtres de collection PC « mal faits » : reprendre le fonctionnement mobile (mondes dans les filtres déroulants) + filtre par rareté.
- Tags un peu plus gros.
- Quitter un match en cours : récompenses/défis validés seulement à la fin (défaite ou annulation : à trancher avec Harlem).
- PC pleine largeur (écrans « à moitié vides » : demander lesquels).

## Ensuite (backlog, dans l'ordre)
v100 Équipe/Draft PC · v101 Boutique (carrousel 3D, taux par perso, ouverture ×10, achat sans ouvrir, effets SSR) · v102 Tuto + quiz (récompense pièces ou grade sur le profil) · v103 Combat (effets, sons, rôle des Soutiens) · v104 Redesign cadres SBC/Draft/Tour + Éveil PC · Classement Draft local. Détails dans `backlog.md`.
Clips 16:9 : Harlem les envoie, à brancher en version horizontale sur PC.
