import os, importlib.util

def load(f):
    spec = importlib.util.spec_from_file_location(f, f)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def approx(a, b, tol=1e-6):
    try: return abs(float(a)-float(b)) < tol
    except: return False

def run_tests(fn, cases, tol=False):
    p = 0
    for args, exp in cases:
        try:
            r = fn(*args)
            ok = approx(r, exp) if tol else r == exp
            if ok: p += 1
        except: pass
    return p, len(cases)

def grade(s):
    res = {}
    res["carre"]               = run_tests(s.carre,               [((5,),25),((0,),0),((-3,),9)])
    res["cube"]                = run_tests(s.cube,                 [((3,),27),((2,),8),((0,),0)])
    res["est_pair"]            = run_tests(s.est_pair,             [((4,),True),((7,),False),((0,),True)])
    res["comparer"]            = run_tests(s.comparer,             [((3,7),"a < b"),((7,3),"a > b"),((5,5),"a == b")])
    res["perimetre_rectangle"] = run_tests(s.perimetre_rectangle,  [((4,3),14),((5,5),20),((10,2),24)])
    res["surface_rectangle"]   = run_tests(s.surface_rectangle,    [((4,3),12),((5,5),25),((7,2),14)])
    res["perimetre_carre"]     = run_tests(s.perimetre_carre,      [((5,),20),((3,),12),((1,),4)])
    res["surface_carre"]       = run_tests(s.surface_carre,        [((5,),25),((4,),16),((1,),1)])
    res["perimetre_triangle"]  = run_tests(s.perimetre_triangle,   [((3,4,5),12),((1,1,1),3)])
    res["equilateral"]         = run_tests(s.equilateral,          [((3,3,3),True),((3,4,5),False)])
    res["comparer_surfaces"]   = run_tests(s.comparer_surfaces,    [((4,3,3),"rectangle"),((2,2,4),"carré"),((2,2,2),"égaux")])
    res["imc"]                 = run_tests(s.imc,                  [((70,1.75),70/1.75**2)], tol=True)
    res["polynome"]            = run_tests(s.polynome,             [((1,2,3,4),27),((0,0,5,99),5),((1,0,0,5),25)])
    res["verifier_identite"]   = run_tests(s.verifier_identite,    [((5,3),True),((7,2),True),((10,1),True)])
    return res

COLS = ["carre","cube","est_pair","comparer",
        "perimetre_rectangle","surface_rectangle","perimetre_carre","surface_carre",
        "perimetre_triangle","equilateral","comparer_surfaces",
        "imc","polynome","verifier_identite"]

def level(pct):
    if pct==100: return "Advanced"
    if pct>=60:  return "Intermediate"
    return "Beginner"

def main():
    files = sorted(f for f in os.listdir() if f.startswith("eval3_") and f.endswith(".py"))
    if not files: print("Aucun fichier eval3_*.py trouvé."); return

    with open("results_eval3.csv","w",encoding="utf-8") as out:
        out.write("Name," + ",".join(COLS) + ",Total,Level\n")
        for f in files:
            name = f.replace("eval3_","").replace(".py","").replace("_"," ").title()
            try:
                s = load(f)
                res = grade(s)
                tp = sum(p for p,t in res.values())
                tt = sum(t for p,t in res.values())
                pct = tp/tt*100
                row = ",".join(f"{res[c][0]}/{res[c][1]}" for c in COLS)
                out.write(f"{name},{row},{tp}/{tt},{level(pct)}\n")
                print(f"{name}: {tp}/{tt} ({level(pct)})")
            except Exception as e:
                out.write(f"{name}," + ",".join(["ERROR"]*len(COLS)) + ",ERROR,ERROR\n")
                print(f"{name}: ERROR — {e}")

if __name__ == "__main__":
    main()
    print("\nRésultats exportés dans results_eval3.csv")