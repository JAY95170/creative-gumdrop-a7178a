---
name: lot-et-push
description: Cycle de travail d'un lot de modifications du jeu ACG, du backup au push. À utiliser au début de toute modification d'index.html, quand on termine un lot, ou quand Harlem dit « go », « push », « pousse », « mets en ligne » ou donne un numéro de version.
---

# Lot et push (ACG)

Un lot = un thème, une version, **un seul push**. Chaque push sur `main` déclenche un déploiement Netlify payant.

## Début de lot
1. Lis les 10 dernières lignes de `JOURNAL.md` (`tail -10`). Absent ? Dis-le et demande la dernière version à Harlem.
2. Vérifie la catégorie annoncée au premier message. Hors catégorie → note « À transmettre → catégorie X », ne le fais pas.
3. Sauvegarde : `mkdir -p sauvegardes && cp index.html sauvegardes/jeu-vXXX.html` (XXX = version actuelle, avant modification).
4. Relis la zone à toucher (Grep), jamais tout le fichier.

## Pendant
- Garde le numéro de version proposé par Harlem. Sans numéro : propose le suivant (actuelle + 1) et dis-le.
- Teste avec le skill `test-jeu` (mobile 390×844 **et** PC 1280×760, zéro erreur console, parcours réel).
- Image remplacée : incrémente `AV` (`const AV='?v=NN'`) sinon les joueurs gardent l'ancienne en cache.

## Fin de lot
1. Ajoute une ligne à `JOURNAL.md` : `JJ/MM/AAAA · catégorie · ce qui a changé · vXXX`. Fichier absent : donne la ligne à Harlem pour qu'il la colle.
2. Règle du jeu modifiée (raretés, économie, combat, boosters, histoire) → signale « mettre à jour le PDF des règles » et dis laquelle.
3. Résume en 3-5 tirets : ce qui change, ce qui reste à valider sur vrais appareils, les « À transmettre ».

## Push (seulement si Harlem le demande)
```bash
git status --short                      # que des fichiers du lot
git add index.html images/…             # jamais docs-prive/, sauvegardes/, JOURNAL.md
git commit -m "vXXX · résumé du lot"
git pull --rebase origin main           # Denis a pu pousser des images entre-temps
git push origin HEAD
```
- Le rebase apporte parfois des conflits sur `index.html` (ligne `ART`, `AV`, CSS) : garde les deux modifications, retest, puis push.
- Denis : branche + Pull Request, un lot par PR, jamais de push direct sur `main`.
- Après le push : dis le commit et rappelle que Netlify redéploie.
