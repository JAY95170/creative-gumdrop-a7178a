# ACG — Passation au 2e développeur (29/10/2026)

À lire en premier. Le jeu : ACG (Anime Card Game), jeu de collection de cartes anime façon FUT/MADFUT, jouable dans le navigateur (mobile ET PC). Porteur du projet : Harlem. Le code est écrit par Claude ; les décisions de jeu sont celles de Harlem.

## Où sont les choses
- Code du jeu : un seul fichier `index.html` (HTML + CSS + JS, sans framework) dans le dépôt GitHub `JAY95170/creative-gumdrop-a7178a` (branche `main`), avec `images/`, `clips/`, `scenes/`, `sounds/`, `images/packs/`.
- Mise en ligne : Netlify est relié au dépôt → chaque push sur `main` met le site à jour en ~1 min (même adresse, la progression des joueurs reste dans leur navigateur : localStorage `collection-anime-proto-v2`).
- Le dépôt est PUBLIC (l'offre gratuite Netlify refuse un dépôt privé avec 2 contributeurs). Ne jamais y mettre de clé secrète.
- Dossier `dev/` du dépôt : documents de travail (ce fichier, journal, règles, choix, backlog, roster). Bloqué en ligne par `_redirects`.
- Version actuelle : **v97**.

## Documents (dans `dev/`)
| Fichier | Rôle |
|---|---|
| `INSTRUCTIONS-PROJET.txt` | À coller dans les instructions de ton Projet Claude |
| `Regles-du-jeu.pdf` | Seule référence des règles (date du 20/10, en retard : voir « Règles à reporter » du backlog) |
| `contexte-et-choix.md` | Le POURQUOI des règles et ce qui a été refusé |
| `JOURNAL.md` | Une ligne par version (date · catégorie · changement · version) |
| `backlog.md` | Ce qui est fait, ce qui reste, dans l'ordre |
| `BRIEF-v98.md` | La prochaine mise à jour, prête à lancer |
| `roster-200.md` / `roster200.json` | Les 200 nouvelles cartes, justifiées carte par carte |

## Installer ton poste (une fois)
1. Harlem t'ajoute comme collaborateur du dépôt GitHub (Settings → Collaborators).
2. Dans ton Claude : crée un Projet « ACG », colle `INSTRUCTIONS-PROJET.txt` dans ses instructions, ajoute les documents de `dev/` comme fichiers du Projet.
3. Dans une session Claude Code (ou Claude avec accès GitHub), attache le dépôt et clone-le.

## Règles de travail à deux (important)
- **Un seul à la fois sur `index.html`.** Prévenir l'autre avant de commencer (« je prends v98 ») et après le push. Le fichier est unique : deux personnes qui le modifient en même temps = conflit.
- Toujours `git pull` avant de commencer, relire les 10 dernières lignes de `dev/JOURNAL.md`.
- Avant chaque modification : sauvegarder l'ancienne version (`dev/sauvegardes/jeu-vXX.html` ou laisser l'historique git faire foi + tag `vXX`).
- Après : une ligne dans `dev/JOURNAL.md`, commit `ACG vXX : …`, push. Le numéro de version suit le journal (pas de doublon : celui qui prend la version la réserve).
- Une règle change → la noter dans `backlog.md` (section « Règles à reporter dans le PDF »).
- Tester mobile (390 px) ET PC (1440 px) avant chaque push ; aucune erreur console.
- Ne pas casser les sauvegardes des joueurs : tout nouveau champ de `S` doit avoir une valeur par défaut.

## Repères techniques
- État `S` (localStorage), `render()` qui appelle les vues `vHome, vShop, vAlbum, vTeam, vSbc, vPlay/vTower, vObj, vProf`, actions par `data-act` → objet `ACT`, fiches par `CTX`.
- Cartes : tableau `RAW` = `[id, monde, nom, version, classe, poste, rareté, note, [tags], nom complet]` ; stats générées par `genStats` sauf UR/LR fixées à la main (`URS_FIX`). Illustrations : `images/<id>.webp` + l'id dans le Set `ART`.
- PC : `@media (min-width:1024px)`, barre de navigation en haut, touches 1–7.
- DA : fond #05060A, or #F2C230, polices Unbounded / Manrope / IBM Plex Mono. Jamais de look « IA ».
- Outils admin dans le jeu : boutons pour tout débloquer / obtenir les contenus rares (demande de Harlem).
