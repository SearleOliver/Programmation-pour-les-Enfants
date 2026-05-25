import importlib.util, traceback, os

def load_student():
    files = [f for f in os.listdir() if f.startswith("eval6_") and f.endswith(".py")]
    if not files:    print("❌ Aucun fichier eval6_Prenom.py trouvé."); return None
    if len(files)>1: print("❌ Plusieurs fichiers trouvés."); return None
    spec = importlib.util.spec_from_file_location("student", files[0])
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); print(f"✔ {files[0]}"); return m

def group(fn, cases, label):
    p,t,fails = 0,len(cases),[]
    for args,exp in cases:
        try:
            r = fn(*args)
            if r == exp: p+=1
            else: fails.append(f"  ❌ {label}{args} → {r!r}  attendu {exp!r}")
        except Exception as e:
            fails.append(f"  💥 {label}{args} → erreur : {e}")
    return p,t,fails

def run(s):
    res = {}
    res["compter_elements"]    = group(s.compter_elements,    [(([" a","b","a"],),{"a":2,"b":1}),(([],),{}),(([" a"],),{"a":1})], "compter_elements")
    res["dico_depuis_listes"]  = group(s.dico_depuis_listes,  [(( ["a","b"],[1,2]),{"a":1,"b":2}),(( ["x"],[9]),{"x":9}),(([],[]),{})], "dico_depuis_listes")
    res["inverser_dictionnaire"]= group(s.inverser_dictionnaire,[(( {"a":1,"b":2}),{1:"a",2:"b"}),(( {"x":7}),{7:"x"}),(( {"a":1,"b":9,"c":13}),{1:"a",9:"b",13:"c"})], "inverser_dictionnaire")
    res["somme_valeurs"]       = group(s.somme_valeurs,        [(( {"a":1,"b":2}),3),(( {"a":1,"b":1,"c":1}),3),(( {"a":4,"b":78}),82),(( {}),0)], "somme_valeurs")
    res["max_cle"]             = group(s.max_cle,              [(( {"a":1,"b":2}),"b"),(( {"a":9,"b":7}),"a"),(( {"z":27,"d":2,"y":29}),"y")], "max_cle")
    res["filtrer_par_valeur"]  = group(s.filtrer_par_valeur,   [(( {"a":1,"b":5,"c":3},3),{"b":5,"c":3}),(( {"a":1,"b":2},5),{}),(( {"a":10},1),{"a":10})], "filtrer_par_valeur")
    res["compter_mots"]        = group(s.compter_mots,         [(("hi hi",),{"hi":2}),(("Hello world Hello",),{"Hello":2,"world":1}),(("a",),{"a":1})], "compter_mots")
    res["mot_le_plus_frequent"]= group(s.mot_le_plus_frequent, [(("le chat et le chien",),"le"),(("a a a b b",),"a"),(("bonjour",),"bonjour")], "mot_le_plus_frequent")
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