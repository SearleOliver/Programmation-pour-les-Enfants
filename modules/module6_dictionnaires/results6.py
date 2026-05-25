import os, importlib.util

def load(f):
    spec = importlib.util.spec_from_file_location(f, f)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def run_tests(fn, cases):
    p = 0
    for args, exp in cases:
        try:
            if fn(*args) == exp: p += 1
        except: pass
    return p, len(cases)

def grade(s):
    res = {}
    res["compter_elements"]     = run_tests(s.compter_elements,     [(([" a","b","a"],),{"a":2,"b":1}),(([],),{}),(([" a"],),{"a":1})])
    res["dico_depuis_listes"]   = run_tests(s.dico_depuis_listes,   [(( ["a","b"],[1,2]),{"a":1,"b":2}),(( ["x"],[9]),{"x":9}),(([],[]),{})])
    res["inverser_dictionnaire"]= run_tests(s.inverser_dictionnaire,[(( {"a":1,"b":2}),{1:"a",2:"b"}),(( {"x":7}),{7:"x"}),(( {"a":1,"b":9,"c":13}),{1:"a",9:"b",13:"c"})])
    res["somme_valeurs"]        = run_tests(s.somme_valeurs,        [(( {"a":1,"b":2}),3),(( {"a":1,"b":1,"c":1}),3),(( {"a":4,"b":78}),82),(( {}),0)])
    res["max_cle"]              = run_tests(s.max_cle,              [(( {"a":1,"b":2}),"b"),(( {"a":9,"b":7}),"a"),(( {"z":27,"d":2,"y":29}),"y")])
    res["filtrer_par_valeur"]   = run_tests(s.filtrer_par_valeur,   [(( {"a":1,"b":5,"c":3},3),{"b":5,"c":3}),(( {"a":1,"b":2},5),{}),(( {"a":10},1),{"a":10})])
    res["compter_mots"]         = run_tests(s.compter_mots,         [(("hi hi",),{"hi":2}),(("Hello world Hello",),{"Hello":2,"world":1}),(("a",),{"a":1})])
    res["mot_le_plus_frequent"] = run_tests(s.mot_le_plus_frequent, [(("le chat et le chien",),"le"),(("a a a b b",),"a"),(("bonjour",),"bonjour")])
    return res

COLS = ["compter_elements","dico_depuis_listes","inverser_dictionnaire",
        "somme_valeurs","max_cle","filtrer_par_valeur",
        "compter_mots","mot_le_plus_frequent"]

def level(pct):
    if pct==100: return "Advanced"
    if pct>=60:  return "Intermediate"
    return "Beginner"

def main():
    files = sorted(f for f in os.listdir() if f.startswith("eval6_") and f.endswith(".py"))
    if not files: print("Aucun fichier eval6_*.py trouvé."); return

    with open("results_eval6.csv","w",encoding="utf-8") as out:
        out.write("Name," + ",".join(COLS) + ",Total,Level\n")
        for f in files:
            name = f.replace("eval6_","").replace(".py","").replace("_"," ").title()
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
    print("\nRésultats exportés dans results_eval6.csv")