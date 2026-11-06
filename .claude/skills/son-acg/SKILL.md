---
name: son-acg
description: Sons et musique du jeu ACG (clics, boutons, combats, coups, ouverture de booster, ambiance, réglages de volume). À utiliser quand Harlem parle de son, bruitage, musique de fond, volume, mute, ou de petits détails d'interface sonores et animés.
---

# Son d'ACG

## Ce qui existe déjà dans `index.html` (Grep `/* ---------- son`)
- Sons **synthétisés** (aucun fichier, 0 Ko, aucun droit d'auteur) : `ac()` (contexte audio, respecte `S.mute`), `tone(freq, début, durée, type, volume, freqFin)`, `noise(début, durée, volume, f1, f2)`.
- Banque `SFX` : `tap`, `rip`, `flip`, `coin`, `charge(rareté)`, `reveal(rareté)`, `reward`. Appelés avec `SFX.tap()` etc. (Grep `SFX\.` pour voir où).
- Sons **fichiers** (clips d'ouverture UR/LR, scènes) : `sndPlay(url, {loop, vol, fade})` / `sndStop(handle, fade)`, dossier `sounds/`, jamais lourds.
- Bouton de coupure : `drawMute()`, réglage `S.mute`.

## Principes
- **Synthétiser d'abord** (`tone`/`noise`) : léger, sans droits. Un fichier `.mp3` seulement pour une voix, un clip ou une musique ; le dire à Harlem avant (poids + droits).
- Un son = une intention : chaque rareté, chaque coup (léger, critique, bloqué, KO), chaque écran a une signature reconnaissable. Pas de bip générique répété partout.
- Volumes bas par défaut (gain ≤ .15 pour les effets, musique ≤ .08), jamais de pic soudain ; fondu entrée/sortie sur les boucles.
- Sur mobile, le son démarre seulement après un geste : `ac()` gère déjà le `resume()` ; ne jamais lancer de musique au chargement.
- Mute respecté partout. Si on ajoute **musique** et **effets** séparés, ajouter des champs dans `S` avec une valeur par défaut au chargement (ne pas casser les anciennes sauvegardes) et deux interrupteurs dans le Profil.
- Les petits détails d'interface (survol, bouton enfoncé, onglet, équipement, erreur, gain de niveau, notification) passent par la même banque `SFX` : on ajoute une clé, on l'appelle depuis le handler `ACT` concerné ou l'écouteur de clic unique.

## Pistes de la catégorie Son
1. Clic / bouton / onglet / erreur / validation (famille « interface »).
2. Combat : coup léger, coup lourd, critique, blocage, soin, KO, victoire, défaite (brancher sur `hitDmg` / `stFight` / `matchHTML`, à l'affichage du coup, pas dans le calcul).
3. Booster : déchirure, charge, révélation par rareté (déjà là : à raffiner), récompense.
4. Ambiance : musique de fond en boucle, une par grand écran (menu, combat, Histoire/espace), fondu entre deux.
5. Réglages : volume musique / effets dans le Profil.

## Tester
Le navigateur de test est muet : vérifier (a) 0 erreur console avec `test-jeu`, (b) que l'appel part bien (espionner `tone`/`noise` ou `sndPlay` depuis Playwright et compter les appels), (c) l'écoute réelle par Harlem sur téléphone et PC. Ne jamais déclarer « le son est bon » sans son écoute.

## Règles du jeu
Le son ne change aucune règle : pas de mise à jour du PDF. Ligne JOURNAL : `JJ/MM/AAAA · JEU/Son · … · vXXX`.
