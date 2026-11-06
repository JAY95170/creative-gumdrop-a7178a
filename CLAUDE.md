# ACG — jeu de cartes anime / manga (jeu vidéo de collection, façon FUT)

Un seul fichier de jeu : `index.html` (≈ 670 Ko, JS vanilla, aucun build). État du joueur = objet global `S`, sauvegardé en localStorage (`save()`), écrans redessinés par `render()`. Les clics passent par un écouteur unique : `ACT[data-act](data-v, el, e)`.
Hébergement : ce dépôt GitHub (public) → Netlify déploie `main` à chaque push (chaque push coûte des crédits).

## Qui fait quoi
- **Harlem** : développeur principal, seul maître du jeu. Il valide, donne les numéros de version (vXXX), tient le JOURNAL, fusionne et pousse sur `main`.
- **Denis** : co-développeur, images de cartes et effets (ouverture, vidéos). Il travaille sur sa branche et ouvre une Pull Request = un lot. Il ne touche ni aux règles, ni à l'économie, ni au roster sans accord de Harlem.

## Façon de travailler (obligatoire)
1. Le **premier message** d'une conversation donne sa **catégorie** (IMAGES, JEU/Interface, JEU/Effets, JEU/Histoire, JEU/Marché…). Reste dedans. Ce qui déborde : le noter en « **À transmettre → catégorie X** ».
2. **Ne lis pas tout `index.html`** : cherche la partie utile avec Grep (noms de fonctions ci-dessous), lis seulement ces lignes.
3. **Avant de modifier** : lis les 10 dernières lignes de `JOURNAL.md`, copie `index.html` en `sauvegardes/jeu-vXXX.html` (version actuelle), relis la zone à toucher.
4. **Après chaque modification** : une ligne dans `JOURNAL.md` → `JJ/MM/AAAA · catégorie · ce qui a changé · vXXX`.
5. Si le changement touche une **règle du jeu** (raretés, économie, combat, boosters…) : le signaler pour mettre à jour le PDF des règles.
6. **Un seul push par lot, uniquement quand Harlem le demande.** Avant de pousser : `git pull --rebase origin main` (Denis pousse aussi). Détail dans le skill `lot-et-push`.
7. **Esprit critique** : revérifier les données avant d'affirmer un diagnostic ; ne pas conclure sur une analyse partielle.
8. **Réponses courtes et concrètes**, sans perdre en profondeur (en dire moins, pas analyser moins). Si Harlem dit « court » ou « rapide » : tirets simples, pas de prose.
9. **Assistant de projet** : signale quand Harlem s'attarde sur un détail sans importance ou qui peut attendre, et recentre sur les étapes.
10. Ordre de priorité en cas de contradiction : **code d'`index.html` > JOURNAL > PDF des règles > autres docs**.

## Design
Les cartes et les écrans doivent avoir de l'**aura** et une **qualité irréprochable** : identité forte, finitions soignées, rien de générique ni de brouillon. Charte et tokens : skill `design-acg`. Inspiration générale : skill `frontend-design`.

## Où chercher dans `index.html` (Grep sur ces noms)
- Cartes : `RAW` (une ligne JSON), `MONDES`, `CARDS`/`CARD`, `genStats`, `URS_FIX`, `VL`, `PRO`, `SPM`, `ART`, `AV` (version du cache des images), `UFX` (entrées UR/LR).
- Combat : `ENG`, `hitDmg`, `fighters`, `evalTeam`, `teamFx`, `FORMS`, `SUPK` ; mode Tour : `vTower`, `matchHTML` ; mode Histoire : `STORY`, `stSim`, `stFight`, `vStory`, `vSpace`.
- Écrans : `vPlay`, `vTeam`, `vAlbum`…, CSS en tête de fichier (`:root` = tokens).
- Son : `SFX`, `tone`, `noise`, `ac()` (sons synthétisés), `sndPlay`/`sndStop` (fichiers `sounds/`), `S.mute`, `drawMute`.
- Boosters / boutique : `PACKS`, `PITY_UR`, `poolFor`, `pickW`.

## Skills du projet (`.claude/skills/`)
| Skill | Quand |
|---|---|
| `lot-et-push` | début / fin de chaque lot : sauvegarde, journal, tests, push |
| `carte-acg` | créer, modifier, chercher ou équilibrer une carte ou un monde |
| `images-cartes` | images de cartes : choix, cadrage sous le bandeau, format, intégration |
| `design-acg` | tout écran ou visuel : charte du jeu |
| `test-jeu` | tester le jeu (Playwright mobile + PC), simuler les combats |
| `son-acg` | sons, musique, bruitages, volume, petits détails d'interface sonores |
| `frontend-design`, `webapp-testing`, `handoff`, `find-skills` | skills publics (voir `.claude/skills/SOURCES.md`) |

N'en ajoute pas à la légère : un skill = un besoin qui revient. Pour en chercher un : `find-skills`.

## Docs de travail
`docs-prive/` (non versionné, dans `.gitignore`) : état du projet, plan, messages de démarrage par catégorie. Si le dossier est présent, lis `docs-prive/ETAT.md` au début d'une conversation. Le dépôt est public : n'y mets jamais de document de travail.
