import importlib.util, traceback, os, math

def load_student():
    files = [f for f in os.listdir() if f.startswith("eval1_") and f.endswith(".py")]
    if not files:   print("❌ Aucun fichier eval1_Prenom.py trouvé."); return None
    if len(files)>1:print("❌ Plusieurs fichiers trouvés. Gardez seulement le vôtre."); return None
    spec = importlib.util.spec_from_file_location("student", files[0])
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    print(f"✔ Fichier chargé : {files[0]}")
    return m

def approx(a, b, tol=1e-6):
    try: return abs(float(a)-float(b)) < tol
    except: return a == b

def check(label, student_val, expected, tol=None):
    ok = approx(student_val, expected) if tol else (student_val == expected)
    status = "✅" if ok else "❌"
    if ok:
        return True, f"{status} {label}"
    else:
        return False, f"{status} {label}  →  reçu : {repr(student_val)}   attendu : {repr(expected)}"

def run(s):
    results = []
    p = lambda *a,**k: results.append(check(*a,**k))
    # Partie 1
    p("prixTotal25",     s.prixTotal25,    5.89*25)
    p("prixKilo",        s.prixKilo,       5.89/1.5)
    p("prixPanier",      s.prixPanier,     5.89*3.7 + 3.99*5.8)
    p("prixFinal",       s.prixFinal,      (5.89*3.7+3.99*5.8)*0.85)
    p("nbSacs",          s.nbSacs,         int(20//5.89))
    p("monnaie",         s.monnaie,        20 % 5.89)
    # Partie 2
    p("age_entier type", type(s.age_entier), int)
    p("age_entier val",  s.age_entier,     42)
    p("pi_float type",   type(s.pi_float), float)
    p("pi_float val",    s.pi_float,       3.14)
    p("annee_texte type",type(s.annee_texte), str)
    p("annee_texte val", s.annee_texte,    "2025")
    p("arrondi",         s.arrondi,        9)
    # Partie 3
    p("longueur_prenom", s.longueur_prenom, 5)
    p("prenom_maj",      s.prenom_maj,     "ALICE")
    p("nom_min",         s.nom_min,        "dupont")
    p("nom_complet",     s.nom_complet,    "alice DUPONT")
    p("prenom_x3",       s.prenom_x3,      "alicealicealice")
    p("message",         s.message,        "Bonjour alice, tu as 42 ans.")
    return results

def display(results):
    passed = sum(1 for ok,_ in results if ok)
    total  = len(results)
    print("\n─── RÉSULTATS ─────────────────────")
    for ok, msg in results:
        if not ok: print(msg)
    pct = passed/total*100
    level = "Advanced" if pct==100 else "Intermediate" if pct>=60 else "Beginner"
    print(f"\nTOTAL : {passed}/{total}  ({level})")
    input("\nAppuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    try:
        s = load_student()
        if s: display(run(s))
    except Exception:
        traceback.print_exc()
        input("\nAppuyez sur Entrée pour quitter...")