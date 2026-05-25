import os, importlib.util

def load(f):
    spec = importlib.util.spec_from_file_location(f, f)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def approx(a, b, tol=1e-9):
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
    res["somme_liste"]        = run_tests(s.somme_liste,        [(([1,2,3,4],),10),(([0],),0),(([5,5],),10)])
    res["min_liste"]          = run_tests(s.min_liste,           [(([3,1,4,1,5],),1),(([9,2,7],),2),(([0],),0)])
    res["max_liste"]          = run_tests(s.max_liste,           [(([3,1,4,1,5,9],),9),(([1],),1),(([0,0,0],),0)])
    res["moyenne_liste"]      = run_tests(s.moyenne_liste,       [(([2,4,6],),4.0),(([1,2,3],),2.0)], tol=True)
    res["nombre_occurrences"] = run_tests(s.nombre_occurrences,  [(([1,2,2,3],2),2),(([1,1,1],1),3),(([],1),0)])
    res["filtrer_pairs"]      = run_tests(s.filtrer_pairs,       [(([1,2,3,4,5,6],),[2,4,6]),(([1,3,5],),[]),(([2,4],),[2,4])])
    res["inverser_liste"]     = run_tests(s.inverser_liste,      [(([1,2,3],),[3,2,1]),(([1],),[1]),(([],),[])])
    res["fusion_listes"]      = run_tests(s.fusion_listes,       [(([1,2],[3,4]),[1,2,3,4]),(([],[1]),[1])])
    res["compter_voyelles"]   = run_tests(s.compter_voyelles,    [(("Bonjour",),3),(("hello",),2),(("bcdf",),0),(("AEIOU",),5)])
    res["est_palindrome"]     = run_tests(s.est_palindrome,      [(("radar",),True),(("Radar",),True),(("hello",),False),(("kayak",),True)])
    res["inverser_mots"]      = run_tests(s.inverser_mots,       [(("a b c",),"c b a"),(("bonjour monde",),"monde bonjour")])
    res["est_numerique"]      = run_tests(s.est_numerique,       [(("1234",),True),(("12a4",),False),(("0",),True)])
    return res

COLS = ["somme_liste","min_liste","max_liste","moyenne_liste","nombre_occurrences",
        "filtrer_pairs","inverser_liste","fusion_listes",
        "compter_voyelles","est_palindrome","inverser_mots","est_numerique"]

def level(pct):
    if pct==100: return "Advanced"
    if pct>=60:  return "Intermediate"
    return "Beginner"

def main():
    files = sorted(f for f in os.listdir() if f.startswith("eval5_") and f.endswith(".py"))
    if not files: print("Aucun fichier eval5_*.py trouvé."); return

    with open("results_eval5.csv","w",encoding="utf-8") as out:
        out.write("Name," + ",".join(COLS) + ",Total,Level\n")
        for f in files:
            name = f.replace("eval5_","").replace(".py","").replace("_"," ").title()
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
    print("\nRésultats exportés dans results_eval5.csv")