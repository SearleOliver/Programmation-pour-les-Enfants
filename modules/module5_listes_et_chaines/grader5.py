import importlib.util, traceback, os

def load_student():
    files = [f for f in os.listdir() if f.startswith("eval5_") and f.endswith(".py")]
    if not files:    print("❌ Aucun fichier eval5_Prenom.py trouvé."); return None
    if len(files)>1: print("❌ Plusieurs fichiers trouvés."); return None
    spec = importlib.util.spec_from_file_location("student", files[0])
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); print(f"✔ {files[0]}"); return m

def approx(a,b,tol=1e-9):
    try: return abs(float(a)-float(b))<tol
    except: return a==b

def group(fn, cases, label, tol=False):
    p,t,fails = 0,len(cases),[]
    for args,exp in cases:
        try:
            r = fn(*args)
            ok = approx(r,exp) if tol else r==exp
            if ok: p+=1
            else: fails.append(f"  ❌ {label}{args} → {r!r}  attendu {exp!r}")
        except Exception as e:
            fails.append(f"  💥 {label}{args} → erreur : {e}")
    return p,t,fails

def run(s):
    res = {}
    res["somme_liste"]        = group(s.somme_liste,        [(([1,2,3,4],),10),(([0],),0),(([5,5],),10)],              "somme_liste")
    res["min_liste"]          = group(s.min_liste,           [(([3,1,4,1,5],),1),(([9,2,7],),2),(([0],),0)],           "min_liste")
    res["max_liste"]          = group(s.max_liste,           [(([3,1,4,1,5,9],),9),(([1],),1),(([0,0,0],),0)],         "max_liste")
    res["moyenne_liste"]      = group(s.moyenne_liste,       [(([2,4,6],),4.0),(([1,2,3],),2.0)],                      "moyenne_liste", tol=True)
    res["nombre_occurrences"] = group(s.nombre_occurrences,  [(([1,2,2,3],2),2),(([1,1,1],1),3),(([],1),0)],           "nombre_occurrences")
    res["filtrer_pairs"]      = group(s.filtrer_pairs,       [(([1,2,3,4,5,6],),[2,4,6]),(([1,3,5],),[]),(([2,4],),[2,4])], "filtrer_pairs")
    res["inverser_liste"]     = group(s.inverser_liste,      [(([1,2,3],),[3,2,1]),(([1],),[1]),(([],),[])],           "inverser_liste")
    res["fusion_listes"]      = group(s.fusion_listes,       [(([1,2],[3,4]),[1,2,3,4]),(([],[1]),  [1])],             "fusion_listes")
    res["compter_voyelles"]   = group(s.compter_voyelles,    [(("Bonjour",),3),(("hello",),2),(("bcdf",),0),(("AEIOU",),5)], "compter_voyelles")
    res["est_palindrome"]     = group(s.est_palindrome,      [(("radar",),True),(("Radar",),True),(("hello",),False),(("kayak",),True)], "est_palindrome")
    res["inverser_mots"]      = group(s.inverser_mots,       [(("a b c",),"c b a"),(("bonjour monde",),"monde bonjour")], "inverser_mots")
    res["est_numerique"]      = group(s.est_numerique,       [(("1234",),True),(("12a4",),False),(("",),True),(("0",),True)], "est_numerique")
    return res

def display(res):
    tp=0; tt=0
    print("\n─── RÉSULTATS ─────────────────────")
    for ex,(p,t,fails) in res.items():
        print(f"{'✅' if p==t else '⚠️ '} {ex}: {p}/{t}")
        for f in fails: print(f)
        tp+=p; tt+=t
    pct=tp/tt*100
    level="Advanced" if pct==100 else "Intermediate" if pct>=60 else "Beginner"
    print(f"\nTOTAL : {tp}/{tt}  ({level})")
    input("\nAppuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    try:
        s = load_student()
        if s: display(run(s))
    except Exception:
        traceback.print_exc(); input("\nAppuyez sur Entrée pour quitter...")