---
name: test-jeu
description: Tester le jeu ACG dans un vrai navigateur (Playwright, mobile 390×844 et PC 1280×760), faire des captures d'écran, détecter les erreurs console, et simuler les combats pour calibrer les taux de victoire (mode Histoire, Tour). À utiliser après toute modification d'index.html et pour équilibrer un boss ou un acte.
---

# Tester ACG

S'appuie sur `webapp-testing` (Playwright). Prérequis : `pip install playwright` puis `playwright install chromium`. Variable `CHROME_PATH` si tu veux utiliser un autre Chrome.

## Captures et parcours : `scripts/capture.py`
Lance un serveur local, ouvre le jeu en mobile **et** PC, prépare une partie de test (7 cartes SR/SSR, niveau et pièces élevés, intro coupée), exécute des étapes JS, prend des captures, liste les erreurs.
```bash
python .claude/skills/test-jeu/scripts/capture.py --out captures --steps etapes.json
```
`etapes.json` : liste `[{"js":"ACT.psub('st')","wait":1000,"shot":"espace"}, …]`. Exemple mode Histoire :
```json
[{"js":"S.tab='tour';S.psub='st';render()","wait":900,"shot":"espace"},
 {"js":"ACT.spEnter('db')","wait":2600,"shot":"planete"},
 {"js":"ACT.stGo('0,0')","wait":1500,"shot":"combat"}]
```
Sortie : `captures/<m|pc>-<shot>.png` + les erreurs de page et de console. **Regarde les images** (Read) : un test sans coup d'œil ne valide pas un visuel.
`--viewports m` ou `pc` pour un seul format. Appelle les actions réelles (`ACT.xxx(...)`) plutôt que de cliquer au pixel.

## Simuler les combats : `scripts/winrates.py`
Taux de victoire du mode Histoire par palier d'équipe (S = que des N · A = N/R · B = mélange · C = SR · D = SSR · E = UR) pour chaque acte, avec les objectifs (≥ 50 % de PV, sans KO) et la durée moyenne.
```bash
python .claude/skills/test-jeu/scripts/winrates.py --runs 250
```
Cibles du mode Histoire : l'équipe du palier prévu gagne ~70-85 % ; un cran en dessous ~30-50 % ; deux crans en dessous échoue presque toujours. Réglage : fixer `at` (attaque du boss) à une valeur modérée et ajuster `pv` ; ne pas pousser `at` à l'extrême (les persos tombent en un coup, combat sans intérêt). Combats ≈ 7-11 tours au palier visé.
Paramètres des boss : `STORY` dans `index.html` (`pv`, `at`, `df`, `n` = frappe tous les n coups, `rage`, `rw`).

## Pièges
- Ne lis pas la sortie HTML entière : Grep la partie utile.
- Le jeu garde son état dans localStorage : chaque test repart d'un contexte neuf (le script le fait).
- Mode Histoire : `ST_MODE` = `'space'` ou `'planet'` ; un monde verrouillé se débloque en finissant l'acte 3 du précédent (`stState().d.db=[1,1,1]`).
