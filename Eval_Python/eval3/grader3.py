import importlib.util
import traceback
import os

def load_student_file():
    files = [f for f in os.listdir() if f.startswith("eval3_") and f.endswith(".py")]

    if len(files) == 0:
        print("❌ Aucun fichier eval3 trouvé.")
        return None

    if len(files) > 1:
        print("❌ Plusieurs fichiers trouvés. Gardez seulement le vôtre.")
        return None

    file = files[0]

    spec = importlib.util.spec_from_file_location("student", file)
    student = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student)

    print(f"✔ Fichier chargé : {file}")
    return student

TOTAL_TESTS  = 0
PASSED_TESTS = 0
FAILED_DETAILS = []

def test(func, expected, *args):
    global TOTAL_TESTS, PASSED_TESTS
    TOTAL_TESTS += 1
    func_name = func.__name__
    try:
        result = func(*args)
        if result == expected:
            PASSED_TESTS += 1
        else:
            FAILED_DETAILS.append(
                f"  ❌ {func_name}{args} → reçu {repr(result)}, attendu {repr(expected)}"
            )
    except Exception as e:
        FAILED_DETAILS.append(
            f"  💥 {func_name}{args} → erreur : {e}"
        )

def run_tests(student):

    # --- somme_a : 1 + 2 + ... + n ---
    test(student.somme_a,  0,  0)   # aucun entier à additionner
    test(student.somme_a,  1,  1)
    test(student.somme_a, 10,  4)   # 1+2+3+4
    test(student.somme_a, 15,  5)   # 1+2+3+4+5
    test(student.somme_a, 55, 10)   # classique

    # --- somme_paire_a ---
    test(student.somme_paire_a, 0,  1)   # 1..1 : aucun pair
    test(student.somme_paire_a, 1,  2)   # 1..2 : juste 2
    test(student.somme_paire_a, 2,  5)   # 1..5 : 2 et 4
    test(student.somme_paire_a, 3,  6)   # 1..6 : 2, 4, 6
    test(student.somme_paire_a, 5, 10)   # 1..10 : 2,4,6,8,10

    # --- somme_liste ---
    test(student.somme_liste,  0, [])
    test(student.somme_liste,  1, [1])
    test(student.somme_liste, 10, [1, 2, 3, 4])
    test(student.somme_liste, 15, [1, 2, 3, 4, 5])
    test(student.somme_liste,  0, [-3, 0, 3])     # négatifs qui s'annulent

    # --- nombre_occurrences ---
    test(student.nombre_occurrences, 0, [],        1)   # liste vide
    test(student.nombre_occurrences, 1, [1],       1)
    test(student.nombre_occurrences, 2, [1,2,2,3], 2)
    test(student.nombre_occurrences, 0, [1,2,3],   9)   # valeur absente
    test(student.nombre_occurrences, 3, [5,5,5],   5)   # tous identiques

    # --- max_list ---
    test(student.max_liste,  1, [1])
    test(student.max_liste,  9, [3, 1, 4, 1, 5, 9])
    test(student.max_liste,  0, [-3, -1, 0])
    test(student.max_liste, 42, [10, 42, 7])
    test(student.max_liste,  5, [5, 5, 5])        # tous égaux

    # --- sum_while : même résultat que sum_to mais avec while ---
    test(student.somme_while,  0,  0)
    test(student.somme_while,  1,  1)
    test(student.somme_while, 10,  4)
    test(student.somme_while, 15,  5)
    test(student.somme_while, 55, 10)

    # --- factorial ---
    test(student.factorielle,   1,  0)   # 0! = 1 — erreur fréquente de retourner 0 !
    test(student.factorielle,   1,  1)
    test(student.factorielle,   2,  2)
    test(student.factorielle,   6,  3)
    test(student.factorielle,  24,  4)
    test(student.factorielle, 120,  5)

    # --- fizzbuzz ---
    test(student.fizzbuzz, [], 0)
    test(student.fizzbuzz, [1], 1)
    test(student.fizzbuzz,
        [1, 2, "Fizz", 4, "Buzz"],
        5)
    test(student.fizzbuzz,
        [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"],
        10)
    test(student.fizzbuzz,
        [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
         11, "Fizz", 13, 14, "FizzBuzz"],
        15)

def show_results():
    print("\n--- RÉSULTATS ---")
    if FAILED_DETAILS:
        print("Tests échoués :")
        for detail in FAILED_DETAILS:
            print(detail)
    print(f"\nScore : {PASSED_TESTS}/{TOTAL_TESTS}")
    percentage = (PASSED_TESTS / TOTAL_TESTS) * 100
    if percentage == 100:
        print("✅ Parfait !")
    elif percentage >= 80:
        print("👍 Niveau validé, mais vous pouvez faire mieux.")
    elif percentage >= 50:
        print("⚠️  À retravailler.")
    else:
        print("❌ Réessayez.")
    input("\nAppuyez sur Entrée pour quitter...")


if __name__ == "__main__":
    try:
        student = load_student_file()
        if student is None:
            input("\nAppuyez sur Entrée pour quitter...")
        else:
            results = run_tests(student)
            show_results()
    except Exception:
        print("Crash du programme.")
        traceback.print_exc()