#!/usr/bin/env python3
"""Taux de victoire du mode Histoire par palier d'équipe. Voir ../SKILL.md."""
import argparse, functools, http.server, os, socketserver, threading
from pathlib import Path
from playwright.sync_api import sync_playwright

PREP = r"""
() => {
 const rows=FORMS.lance.rows,sl=rows.flat();
 const tiers={S:['N'],A:['N','R'],C:['SR'],D:['SSR'],E:['UR','SSR']};
 const pick=(rars)=>{const used=new Set(),ids=[];sl.forEach(p=>{const c=CARDS.filter(c=>c.poste===p&&rars.includes(c.r)&&!used.has(c.id)&&!c.ex&&!c.awk&&!c.scn).sort((a,b)=>b.note-a.note)[0];used.add(c.id);ids.push(c.id)});return ids};
 const T={};for(const k in tiers)T[k]=pick(tiers[k]);
 const sr=pick(['SR']),r=pick(['N','R']);T.B=sl.map((p,i)=>i%2===0?sr[i]:r[i]);
 window.__T=T;const info={};for(const k in T)info[k]=Math.round(evalTeam(FORMS.lance.rows,T[k]).note);return info;
}
"""
RUN = r"""
(N) => STORY.map((w,wi)=>w.acts.map((a,ai)=>{const row={};
  for(const k of Object.keys(window.__T)){let win=0,o2=0,o3=0,rd=0;
    for(let i=0;i<N;i++){const r=stSim(a,window.__T[k],'lance');if(r.win)win++;if(r.obj[1])o2++;if(r.obj[2])o3++;rd+=r.rounds}
    row[k]=[Math.round(win/N*100),Math.round(o2/N*100),Math.round(o3/N*100),+(rd/N).toFixed(1)]}
  return {monde:w.n,acte:ai+1,boss:a.b,row}}))
"""

class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a, **k): pass

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--root', default='.'); ap.add_argument('--runs', type=int, default=250); ap.add_argument('--port', type=int, default=0)
    a = ap.parse_args()
    h = functools.partial(Quiet, directory=str(Path(a.root).resolve()))
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.TCPServer(('127.0.0.1', a.port), h); port = srv.server_address[1]; threading.Thread(target=srv.serve_forever, daemon=True).start()
    with sync_playwright() as p:
        kw = {'executable_path': os.environ['CHROME_PATH']} if os.environ.get('CHROME_PATH') else {}
        b = p.chromium.launch(args=['--no-sandbox'], **kw); pg = b.new_page()
        pg.goto(f'http://127.0.0.1:{port}/index.html'); pg.wait_for_timeout(1500)
        print('Notes des paliers :', pg.evaluate(PREP))
        print('Format : [victoire %, ≥50 % PV %, sans KO %, tours moyens]')
        for monde in pg.evaluate(RUN, a.runs):
            for r in monde: print(f"{r['monde']} acte {r['acte']} ({r['boss']}) :", r['row'])
        b.close()
    srv.shutdown()

if __name__ == '__main__':
    main()
