import importlib.util, traceback, os

def load_student():
    files = [f for f in os.listdir() if f.startswith("eval2_") and f.endswith(".py")]
    if not files:    print("❌ Aucun fichier eval2_Prenom.py trouvé."); return None
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
    res["est_positif"]     = group(s.est_positif,    [((5,),True),  ((-3,),False), ((0,),False)], "est_positif")
    res["est_pair"]        = group(s.est_pair,        [((4,),True),  ((7,),False),  ((0,),True)],  "est_pair")
    res["dans_intervalle"] = group(s.dans_intervalle, [((5,1,10),True),((0,1,10),False),((10,1,10),True)], "dans_intervalle")
    res["est_divisible"]   = group(s.est_divisible,   [((9,3),True), ((10,3),False)], "est_divisible")
    res["maximum"]         = group(s.maximum,         [((3,7),7),    ((7,3),7),    ((5,5),5)],    "maximum")
    res["minimum"]         = group(s.minimum,         [((3,7),3),    ((7,3),3),    ((5,5),5)],    "minimum")
    res["valeur_absolue"]  = group(s.valeur_absolue,  [((5,),5),     ((-5,),5),    ((0,),0)],     "valeur_absolue")
    res["signe"]           = group(s.signe,           [((3,),"positif"),((-1,),"negatif"),((0,),"zero")], "signe")
    res["max_trois"]       = group(s.max_trois,       [((1,9,4),9),  ((5,5,5),5),  ((3,3,9),9)],  "max_trois")
    res["mention"]         = group(s.mention,         [((17,),"Très bien"),((14,),"Bien"),((12,),"Assez bien"),((10,),"Passable"),((8,),"Insuffisant")], "mention")
    res["est_bissextile"]  = group(s.est_bissextile,  [((2024,),True),((1900,),False),((2000,),True),((2023,),False)], "est_bissextile")
    res["peut_entrer"]     = group(s.peut_entrer,     [((20,False,False),True),((16,True,False),True),((20,False,True),False),((15,False,False),False)], "peut_entrer")
    res["triangle_valide"] = group(s.triangle_valide, [((3,4,5),True),((1,2,10),False),((5,5,5),True)], "triangle_valide")
    res["fizzbuzz_un"]     = group(s.fizzbuzz_un,     [((9,),"fizz"),((10,),"buzz"),((15,),"fizzbuzz"),((7,),7)], "fizzbuzz_un")
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