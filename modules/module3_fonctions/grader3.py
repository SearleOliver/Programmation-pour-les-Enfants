import importlib.util, traceback, os

def load_student():
    files = [f for f in os.listdir() if f.startswith("eval3_") and f.endswith(".py")]
    if not files:    print("❌ Aucun fichier eval3_Prenom.py trouvé."); return None
    if len(files)>1: print("❌ Plusieurs fichiers trouvés."); return None
    spec = importlib.util.spec_from_file_location("student", files[0])
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); print(f"✔ {files[0]}"); return m

def approx(a, b, tol=1e-6):
    try: return abs(float(a)-float(b)) < tol
    except: return a == b

def group(fn, cases, label, tol=False):
    p,t,fails = 0,len(cases),[]
    for args, exp in cases:
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
    res["carre"]               = group(s.carre,               [((5,),25),((0,),0),((-3,),9)], "carre")
    res["cube"]                = group(s.cube,                 [((3,),27),((2,),8),((0,),0)],  "cube")
    res["est_pair"]            = group(s.est_pair,             [((4,),True),((7,),False),((0,),True)], "est_pair")
    res["comparer"]            = group(s.comparer,             [((3,7),"a < b"),((7,3),"a > b"),((5,5),"a == b")], "comparer")
    res["perimetre_rectangle"] = group(s.perimetre_rectangle,  [((4,3),14),((5,5),20),((10,2),24)], "perimetre_rectangle")
    res["surface_rectangle"]   = group(s.surface_rectangle,    [((4,3),12),((5,5),25),((7,2),14)],  "surface_rectangle")
    res["perimetre_carre"]     = group(s.perimetre_carre,      [((5,),20),((3,),12),((1,),4)],       "perimetre_carre")
    res["surface_carre"]       = group(s.surface_carre,        [((5,),25),((4,),16),((1,),1)],       "surface_carre")
    res["perimetre_triangle"]  = group(s.perimetre_triangle,   [((3,4,5),12),((1,1,1),3)],           "perimetre_triangle")
    res["equilateral"]         = group(s.equilateral,          [((3,3,3),True),((3,4,5),False)],     "equilateral")
    res["comparer_surfaces"]   = group(s.comparer_surfaces,    [((4,3,3),"rectangle"),((2,2,4),"carré"),((2,2,2),"égaux")], "comparer_surfaces")
    res["imc"]                 = group(s.imc,                  [((70,1.75),70/1.75**2)],             "imc", tol=True)
    res["polynome"]            = group(s.polynome,             [((1,2,3,4),27),((0,0,5,99),5),((1,0,0,5),25)], "polynome")
    res["verifier_identite"]   = group(s.verifier_identite,    [((5,3),True),((7,2),True),((10,1),True)], "verifier_identite")
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