# Backlog ACG — état au 29/10/2026 soir (jeu = v97, en ligne)

## Déploiement
- GitHub JAY95170/creative-gumdrop-a7178a (PUBLIC, main) → Netlify auto-deploy. Ancien dépôt privé acg-jeu : sauvegarde, plus utilisé.
- Commits : Netlify gratuit bloque un 2e contributeur sur dépôt PRIVÉ ; en public, pas de limite.
- Avant lancement public : repasser en privé (Netlify Pro ou contributeurs liés), jamais de clé secrète dans le dépôt.
- 2 développeurs (Harlem + son ami, chacun avec son Claude) : un seul à la fois sur index.html, voir dev/PASSATION.md.

## Fait le 29/10
- v93 PC 2 colonnes · v94 Draft verrouillé, Ouki Tank, « Tout retirer », Équipe PC, taux d'obtention SR+ · v95 barre du haut PC, Album PC · v96 Tour Céleste redessinée, combat PC compact · v97 Saison 1 (boosters village, bannière LR, SBC « Éveil du Kaio » note 82, LR 0,02 % Or, vitrine PC)
- Roster +200 préparé (dev/roster-200.md) + 183 images dans images/ — PAS encore dans le jeu.

## À faire (ordre)
- v98 Roster +200 : notes, stats, tags, nouveaux mondes (voir BRIEF-v98.md). 17 images à fournir par Harlem.
- v99 Bugs/ergonomie : sous-onglet mémorisé · pastilles de récompenses · fond du booster qui dépasse · moins de scrolls (Draft, Bilans) · filtres collection PC comme sur mobile + filtre rareté · tags plus gros · quitter un match (récompenses à la fin ; défaite ou annulation à trancher) · PC pleine largeur (écrans à préciser)
- v100 Équipe/Draft PC : formations homogènes (Rempart en valeur) · formations + stats sur le même écran · lien visuel entre persos du même tag · indicateur couleur dans « tous les mondes » · Draft PC refondu, terrain horizontal
- v101 Boutique : carrousel 3D de boosters (d'après une ancienne version, bannière Goku verticale à droite) · taux de drop par perso · ouverture ×10 en miniatures (meilleures raretés qui tremblent et se rejoignent au centre, passer ou non) · acheter ×10 sans ouvrir + « tout ouvrir » dans le stock · effet 3D + obtention SSR plus forte · 3 cartes de l'accueil agrandies
- v102 Tuto : parcours forcé profil → « comprendre le jeu » (bonus) · mini-quiz + question fun · récompense pièces ou grade affiché sur le profil
- v103 Combat : effets/sons modernisés · rôle des Soutiens visible
- v104 Redesign cadres SBC / Tournoi Draft / Tour Céleste (récompenses d'étage plus grosses) · Éveil format PC, pierres d'éveil modernisées
- Classement Draft jour/semaine en local (points + récompenses), mondial avec le serveur
- Clips 16:9 de Harlem → version horizontale sur PC
- Plus tard : Archives/album par set (Saison 2), équilibrage Tour Difficile, tuile « Booster gratuit » (icône 銅), badge de rareté, traductions (3 langues), PDF des règles à jour

## Serveur et lancement (plus tard)
- Phase 1 comptes + sauvegarde cloud (Supabase : URL + clé publique « anon » seulement), puis amis, parrainage, classement, notifications
- Avant public : pages légales, droits d'auteur, audit de sécurité, bêta fermée entre amis

## Règles à reporter dans le PDF (il date du 20/10)
3 tours, boss, SBC RAPIDE/FORMATION + saison, profil/badges/vitrine, XP, chemistry non auto, échanges SR/SSR, Tour 3 essais + retry 10 000, Draft illimitée, ×10, skip après 3 matchs, prix de vente, Ouki Tank, saisons, LR de saison (SBC Éveil du Kaio + Sceau, 0,02 % Or), pas de budget d'équipe, taux affiché à l'obtention, roster +200 et 9 nouveaux mondes (quand v98 sera faite)
