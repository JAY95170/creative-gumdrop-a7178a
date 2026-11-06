#!/usr/bin/env python3
"""Captures et parcours de test du jeu ACG (mobile + PC). Voir ../SKILL.md."""
import argparse, functools, http.server, json, os, socketserver, sys, threading
from pathlib import Path
from playwright.sync_api import sync_playwright

# Partie de test : 7 cartes (SR/SSR sinon moins) en formation Lance, niveau et pièces élevés, intro coupée.
SETUP = r"""
() => {
 const rows=FORMS.lance.rows,sl=rows.flat(),used=new Set(),ids=[];
 sl.forEach(p=>{const c=CARDS.filter(c=>c.poste===p&&['SR','SSR'].includes(c.r)&&!used.has(c.id)&&!c.ex&&!c.awk&&!c.scn).sort((a,b)=>b.note-a.note)[0];used.add(c.id);ids.push(c.id);S.owned[c.id]=1});
 S.team=ids;S.form='lance';S.xp=2000;S.introOff=true;S.tab='tour';S.psub='st';S.coins=5000;
 if(S.init)S.init.done=true;save();render();return ids;
}
"""
class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a, **k): pass

VIEWPORTS = {'m': (390, 844), 'pc': (1280, 760)}

def serve(root, port):
    handler = functools.partial(Quiet, directory=str(root))
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.TCPServer(('127.0.0.1', port), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.', help="dossier contenant index.html")
    ap.add_argument('--out', default='captures')
    ap.add_argument('--steps', help="fichier JSON d'étapes [{js, wait, shot}]")
    ap.add_argument('--viewports', default='m,pc')
    ap.add_argument('--port', type=int, default=0, help='0 = port libre automatique')
    a = ap.parse_args()
    steps = json.loads(Path(a.steps).read_text(encoding='utf-8')) if a.steps else [{"js": "0", "wait": 800, "shot": "accueil"}]
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    srv = serve(Path(a.root).resolve(), a.port); port = srv.server_address[1]
    bad = 0
    with sync_playwright() as p:
        kw = {'executable_path': os.environ['CHROME_PATH']} if os.environ.get('CHROME_PATH') else {}
        b = p.chromium.launch(args=['--no-sandbox'], **kw)
        for name in a.viewports.split(','):
            w, h = VIEWPORTS[name]
            pg = b.new_context(viewport={'width': w, 'height': h}).new_page(); errs = []
            pg.on('pageerror', lambda e: errs.append('JS: ' + str(e)))
            pg.on('console', lambda m: errs.append('console: ' + m.text) if m.type == 'error' and not m.text.startswith('Failed to load resource') else None)
            pg.on('response', lambda r: errs.append('404: ' + r.url) if r.status == 404 and 'favicon' not in r.url else None)
            pg.goto(f'http://127.0.0.1:{port}/index.html'); pg.wait_for_timeout(1200)
            pg.evaluate(SETUP); pg.wait_for_timeout(500)
            for s in steps:
                if s.get('js'): pg.evaluate(s['js'])
                pg.wait_for_timeout(s.get('wait', 500))
                if s.get('shot'): pg.screenshot(path=str(out / f"{name}-{s['shot']}.png"))
            print(f'[{name} {w}x{h}] erreurs: {len(errs)}'); bad += len(errs)
            for e in errs[:10]: print('  ', e)
        b.close()
    srv.shutdown()
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
