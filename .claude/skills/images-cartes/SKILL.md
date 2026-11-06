---
name: images-cartes
description: Images de cartes d'ACG : choisir une image badass, la juger (netteté, aura, trop IA, fidélité à l'anime), la cadrer sous le bandeau, produire les fichiers webp et les intégrer. À utiliser pour ajouter, remplacer, auditer ou recadrer une image de carte, ou préparer un lot d'images pour Denis.
---

# Images de cartes

## Fichiers
- `images/<id>.webp` : **600×840** (5:7). Viser 900×1260 si la source est assez nette. Miniature : `images/s/<id>.webp` en **300×420**.
- `<id>` = id de la carte dans `RAW` (ex. `op-monkey-arc-wano`).
- Nouvelle ou remplacée : ajouter l'id au `Set` `ART` dans `index.html` si absent, puis incrémenter `AV` (cache).
- Tuiles d'accueil : `images/home/home-<nom>.webp`.

## Cadrage (règle de Harlem)
Le **bandeau** du bas cache le bas de l'image. Zone visible ≈ **5 % → 73 % de la hauteur** ; note en haut à gauche, rareté en haut à droite.
1. Centrer le sujet dans la **zone visible**, pas au milieu de l'image entière.
2. Garder visage **et** élément clé (main, arme, attaque, crâne). Un petit bout d'arme ou de main est très bien.
3. Écrans sans bandeau (SBC, mini-cartes) : l'image doit rester centrée, rien de coupé. Compromis actuel : centre de la zone clé à ~39 % de la hauteur.
4. Toujours calculer le bandeau avant de cadrer. Générer l'aperçu « comme dans le jeu » (haut 68 %) et contrôler : visage entier, élément clé visible, rien sous la note, la rareté ou le bandeau.
5. Si `integrer_images.py` + `recadrages.csv` (`id,hx,hy,zoom`) existent en local : `hx,hy` = centre de la zone clé (0 à 1) ; le script le place à 39 %.

## Choisir et juger → `references/gout-et-grille.md`
Lis-le avant tout choix ou audit d'image. Résumé : l'image porte l'âme du perso, une couleur dominante, fort contraste, silhouette ou geste mémorable, jamais de fond vide. Grille de 6 lignes (mini 8/12), signaux « trop IA » et « décalé de l'anime » = rejet.

## Qualité
Source nette, aucun agrandissement flou. Priorité aux SSR / UR / LR (vues en grand), mais **toutes les raretés** doivent être belles. Rareté visible dans l'image : N scène simple, R pose travaillée, SR moment marquant, SSR image qui accroche, UR scène iconique, LR impact maximal.
Préférer une source connue (officiel, key visuals, planches, captures nettes). Doute après la grille = rejet.

## Dans `index.html`
`artOf(c, big)` donne l'URL ; `cardHTML(c,{mini,note,back})` dessine la carte. Après intégration, ouvre l'Album sur la carte en PC et mobile (skill `test-jeu`).
