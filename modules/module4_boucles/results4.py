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
    res["somme_n"]           = run_tests(s.somme_n,          [((5,),15),((10,),55),((1,),1),((0,),0)])
    res["somme_pairs"]       = run_tests(s.somme_pairs,       [((6,),12),((5,),6),((1,),0),((10,),30)])
    res["compte_a_rebours"]  = run_tests(s.compte_a_rebours,  [((4,),[4,3,2,1,0]),((0,),[0]),((2,),[2,1,0])])
    res["somme_chiffres"]    = run_tests(s.somme_chiffres,    [((123,),6),((999,),27),((10,),1),((0,),0)])
    res["factorielle"]       = run_tests(s.factorielle,       [((0,),1),((1,),1),((5,),120),((7,),5040)])
    res["puissance_boucle"]  = run_tests(s.puissance_boucle,  [((2,8),256),((3,3),27),((5,0),1),((1,100),1)])
    res["syracuse"]          = run_tests(s.syracuse,          [((6,),8),((1,),0),((2,),1)])
    fb = [1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz","Buzz",11,"Fizz",13,14,"FizzBuzz"]
    res["fizzbuzz"]          = run_tests(s.fizzbuzz,          [((15,),fb)])
    res["est_premier"]       = run_tests(s.est_premier,       [((2,),True),((7,),True),((9,),False),((1,),False),((13,),True)])
    res["compter_multiples"] = run_tests(s.compter_multiples, [((10,3),3),((10,2),5),((10,10),1),((10,11),0)])
    return res

COLS = ["somme_n","somme_pairs","compte_a_rebours","somme_chiffres",
        "factorielle","puissance_boucle","syracuse",
        "fizzbuzz","est_premier","compter_multiples"]

def level(pct):
    if pct==100: return "Advanced"
    if pct>=60:  return "Intermediate"
    return "Beginner"

def main():
    files = sorted(f for f in os.listdir() if f.startswith("eval4_") and f.endswith(".py"))
    if not files: print("Aucun fichier eval4_*.py trouvé."); return

    with open("results_eval4.csv","w",encoding="utf-8") as out:
        out.write("Name," + ",".join(COLS) + ",Total,Level\n")
        for f in files:
            name = f.replace("eval4_","").replace(".py","").replace("_"," ").title()
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
    print("\nRésultats exportés dans results_eval4.csv")