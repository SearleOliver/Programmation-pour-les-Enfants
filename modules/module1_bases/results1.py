import os, importlib.util, math

def load(f):
    spec = importlib.util.spec_from_file_location(f, f)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def approx(a, b, tol=1e-6):
    try: return abs(float(a)-float(b)) < tol
    except: return a == b

def check(val, exp):
    return approx(val, exp)

def grade(s):
    def t(val, exp): return 1 if check(val, exp) else 0
    def safe(fn): 
        try: return fn()
        except: return None

    scores = {}
    scores["prixTotal25"]   = safe(lambda: t(s.prixTotal25,    5.89*25))
    scores["prixKilo"]      = safe(lambda: t(s.prixKilo,       5.89/1.5))
    scores["prixPanier"]    = safe(lambda: t(s.prixPanier,     5.89*3.7+3.99*5.8))
    scores["prixFinal"]     = safe(lambda: t(s.prixFinal,      (5.89*3.7+3.99*5.8)*0.85))
    scores["nbSacs"]        = safe(lambda: t(s.nbSacs,         int(20//5.89)))
    scores["monnaie"]       = safe(lambda: t(s.monnaie,        20%5.89))
    scores["age_entier"]    = safe(lambda: t(s.age_entier, 42) and t(type(s.age_entier), int))
    scores["pi_float"]      = safe(lambda: t(s.pi_float, 3.14) and t(type(s.pi_float), float))
    scores["annee_texte"]   = safe(lambda: t(s.annee_texte,"2025") and t(type(s.annee_texte), str))
    scores["arrondi"]       = safe(lambda: t(s.arrondi, 9))
    scores["longueur"]      = safe(lambda: t(s.longueur_prenom, 5))
    scores["prenom_maj"]    = safe(lambda: t(s.prenom_maj, "ALICE"))
    scores["nom_min"]       = safe(lambda: t(s.nom_min, "dupont"))
    scores["nom_complet"]   = safe(lambda: t(s.nom_complet, "alice DUPONT"))
    scores["prenom_x3"]     = safe(lambda: t(s.prenom_x3, "alicealicealice"))
    scores["message"]       = safe(lambda: t(s.message, "Bonjour alice, tu as 42 ans."))
    return scores

COLS = ["prixTotal25","prixKilo","prixPanier","prixFinal","nbSacs","monnaie",
        "age_entier","pi_float","annee_texte","arrondi",
        "longueur","prenom_maj","nom_min","nom_complet","prenom_x3","message"]

def level(pct):
    if pct==100: return "Advanced"
    if pct>=60:  return "Intermediate"
    return "Beginner"

def main():
    files = sorted(f for f in os.listdir() if f.startswith("eval1_") and f.endswith(".py"))
    if not files: print("Aucun fichier eval1_*.py trouvé."); return

    with open("results_eval1.csv","w",encoding="utf-8") as out:
        out.write("Name," + ",".join(COLS) + ",Total,Level\n")
        for f in files:
            name = f.replace("eval1_","").replace(".py","").replace("_"," ").title()
            try:
                s = load(f)
                sc = grade(s)
                total = sum(v for v in sc.values() if v is not None)
                pct   = total/len(COLS)*100
                row   = ",".join(str(sc.get(c,"ERR")) for c in COLS)
                out.write(f"{name},{row},{total}/{len(COLS)},{level(pct)}\n")
                print(f"{name}: {total}/{len(COLS)} ({level(pct)})")
            except Exception as e:
                out.write(f"{name}," + ",".join(["ERROR"]*len(COLS)) + ",ERROR,ERROR\n")
                print(f"{name}: ERROR — {e}")

if __name__ == "__main__":
    main()
    print("\nRésultats exportés dans results_eval1.csv")