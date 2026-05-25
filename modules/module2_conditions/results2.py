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
    res["est_positif"]     = run_tests(s.est_positif,     [((5,),True),((-3,),False),((0,),False)])
    res["est_pair"]        = run_tests(s.est_pair,         [((4,),True),((7,),False),((0,),True)])
    res["dans_intervalle"] = run_tests(s.dans_intervalle,  [((5,1,10),True),((0,1,10),False),((10,1,10),True)])
    res["est_divisible"]   = run_tests(s.est_divisible,    [((9,3),True),((10,3),False)])
    res["maximum"]         = run_tests(s.maximum,          [((3,7),7),((7,3),7),((5,5),5)])
    res["minimum"]         = run_tests(s.minimum,          [((3,7),3),((7,3),3),((5,5),5)])
    res["valeur_absolue"]  = run_tests(s.valeur_absolue,   [((5,),5),((-5,),5),((0,),0)])
    res["signe"]           = run_tests(s.signe,            [((3,),"positif"),((-1,),"negatif"),((0,),"zero")])
    res["max_trois"]       = run_tests(s.max_trois,        [((1,9,4),9),((5,5,5),5),((3,3,9),9)])
    res["mention"]         = run_tests(s.mention,          [((17,),"Très bien"),((14,),"Bien"),((12,),"Assez bien"),((10,),"Passable"),((8,),"Insuffisant")])
    res["est_bissextile"]  = run_tests(s.est_bissextile,   [((2024,),True),((1900,),False),((2000,),True),((2023,),False)])
    res["peut_entrer"]     = run_tests(s.peut_entrer,      [((20,False,False),True),((16,True,False),True),((20,False,True),False),((15,False,False),False)])
    res["triangle_valide"] = run_tests(s.triangle_valide,  [((3,4,5),True),((1,2,10),False),((5,5,5),True)])
    res["fizzbuzz_un"]     = run_tests(s.fizzbuzz_un,      [((9,),"fizz"),((10,),"buzz"),((15,),"fizzbuzz"),((7,),7)])
    return res

COLS = ["est_positif","est_pair","dans_intervalle","est_divisible",
        "maximum","minimum","valeur_absolue",
        "signe","max_trois","mention",
        "est_bissextile","peut_entrer","triangle_valide","fizzbuzz_un"]

def level(pct):
    if pct==100: return "Advanced"
    if pct>=60:  return "Intermediate"
    return "Beginner"

def main():
    files = sorted(f for f in os.listdir() if f.startswith("eval2_") and f.endswith(".py"))
    if not files: print("Aucun fichier eval2_*.py trouvé."); return

    with open("results_eval2.csv","w",encoding="utf-8") as out:
        out.write("Name," + ",".join(f"{c}" for c in COLS) + ",Total,Level\n")
        for f in files:
            name = f.replace("eval2_","").replace(".py","").replace("_"," ").title()
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
    print("\nRésultats exportés dans results_eval2.csv")