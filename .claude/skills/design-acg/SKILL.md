---
name: design-acg
description: Charte visuelle du jeu ACG (couleurs, typographies, cartes, mobile d'abord). À utiliser pour créer ou retoucher un écran, un composant, une animation, un visuel ou une carte du jeu, et pour juger si un rendu a assez d'aura.
---

# Design ACG

Objectif : de l'**aura** et de la **qualité**. Chaque écran a un point de vue, pas un gabarit. Complète `frontend-design` (principes généraux) ; en cas de doute, la charte ci-dessous gagne.

## Tokens (déjà dans `:root` de `index.html` : réutilise-les, n'invente pas de couleur)
- Fond sombre : `--bg #05060A`, `--surface #0D1018`, `--surface-2 #161A26`, `--line` blanc 14 %. Texte `--text`, secondaire `--muted`.
- Accent unique : `--accent #F2C230` (or), texte dessus `--accent-ink`. États : `--good #5CC48A`, `--bad #E5534B`.
- Raretés : `--r-n` gris, `--r-r` bleu, `--r-sr` rose, `--r-ssr` or ; UR/LR ont leurs effets propres (holo, entrées animées). Un monde = une couleur `--m-xx` (+ kanji).
- Polices : titres `--f-display` (Unbounded / Dela Gothic One), texte `--f-body` (Manrope / Zen Kaku Gothic), chiffres et étiquettes `--f-mono` (IBM Plex Mono).

## Règles
1. **Mobile d'abord** : largeur utile 390 px, `.app` max 460 px ; sur PC (≥ 1024 px) on gagne de la place (panneaux, grilles), on ne s'étire pas.
2. Une carte a un **bandeau** en bas (nom, version, stats) : ne jamais placer d'élément clé sous les 73 % de hauteur de l'image (voir `images-cartes`).
3. Cohérence : un composant existant (`.btn`, `.eyebrow`, `.seg`, `cardHTML`, `artOf`) avant d'en créer un nouveau. Cherche-le avec Grep.
4. La couleur dit quelque chose (rareté, monde, état) — jamais décorative seule. Un seul accent doré par écran.
5. Mouvement : il explique (entrée, impact, récompense), il ne décore pas. Prévoir `prefers-reduced-motion`.
6. Lisibilité : contraste fort sur fond sombre, texte ≥ 11 px, zones tactiles ≥ 40 px, état `:focus-visible` conservé.
7. Les skills graphiques de Claude doivent servir cette charte, pas la remplacer.

## Vérifier avant de livrer
Capture mobile 390×844 + PC 1280×760 (skill `test-jeu`), puis regarde : hiérarchie claire en 2 secondes ? un détail mémorable ? rien de coupé, flou ou trop lisse ? Sinon recommence ce point.

## Modes spéciaux déjà posés (à imiter, pas à refaire)
- Mode Histoire (`vSpace`, `vStory`, `stFightHTML`) : scène spatiale 3D en CSS (`perspective` + `translate3d`), planètes sphériques en canvas, transition « paupières » entre l'espace et une planète.
- Tour Céleste : toits à avant-toits relevés, ciel à la lune en trame.
