import importlib.util, traceback, os

def load_student():
    files = [f for f in os.listdir() if f.startswith("eval4_") and f.endswith(".py")]
    if not files:    print("❌ Aucun fichier eval4_Prenom.py trouvé."); return None
    if len(files)>1: print("❌ Plusieurs fichiers trouvés."); return None
    spec = importlib.util.spec_from_file_location("student", files[0])
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); print(f"✔ {files[0]}"); return m

def group(fn, cases, label):
    p,t,fails = 0,len(cases),[]
    for args, exp in cases:
        try:
            r = fn(*args)
            if r == exp: p+=1
            else: fails.append(f"  ❌ {label}{args} → {r!r}  attendu {exp!r}")
        except Exception as e:
            fails.append(f"  💥 {label}{args} → erreur : {e}")
    return p,t,fails

def run(s):
    res = {}
    res["somme_n"]           = group(s.somme_n,          [((5,),15),((10,),55),((1,),1),((0,),0)],           "somme_n")
    res["somme_pairs"]       = group(s.somme_pairs,       [((6,),12),((5,),6),((1,),0),((10,),30)],          "somme_pairs")
    res["compte_a_rebours"]  = group(s.compte_a_rebours,  [((4,),[4,3,2,1,0]),((0,),[0]),((2,),[2,1,0])],    "compte_a_rebours")
    res["somme_chiffres"]    = group(s.somme_chiffres,    [((123,),6),((999,),27),((10,),1),((0,),0)],       "somme_chiffres")
    res["factorielle"]       = group(s.factorielle,       [((0,),1),((1,),1),((5,),120),((7,),5040)],        "factorielle")
    res["puissance_boucle"]  = group(s.puissance_boucle,  [((2,8),256),((3,3),27),((5,0),1),((1,100),1)],   "puissance_boucle")
    res["syracuse"]          = group(s.syracuse,          [((6,),8),((1,),0),((2,),1)],                      "syracuse")
    expected_fb = [1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz","Buzz",11,"Fizz",13,14,"FizzBuzz"]
    res["fizzbuzz"]          = group(s.fizzbuzz,          [((15,),expected_fb)],                              "fizzbuzz")
    res["est_premier"]       = group(s.est_premier,       [((2,),True),((7,),True),((9,),False),((1,),False),((13,),True)], "est_premier")
    res["compter_multiples"] = group(s.compter_multiples, [((10,3),3),((10,2),5),((10,10),1),((10,11),0)],  "compter_multiples")
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