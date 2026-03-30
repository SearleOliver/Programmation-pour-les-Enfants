import importlib.util
import traceback
import os

TOTAL_TESTS = 0
PASSED_TESTS = 0
FAILED_DETAILS = []

def load_student_file():
    files = [f for f in os.listdir() if f.startswith("eval1_") and f.endswith(".py")]

    if len(files) == 0:
        print("❌ Aucun fichier eval1 trouvé.")
        return None

    if len(files) > 1:
        print("❌ Plusieurs fichiers trouvés. Gardez seulement le vôtre.")
        return None

    file = files[0]

    spec = importlib.util.spec_from_file_location("student", file)
    student = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student)

    print(f"✔ Fichier chargé : {file}")
    student_name = file.replace("eval1_", "").replace(".py", "")
    return student, student_name

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
    global TOTAL_TESTS, PASSED_TESTS, FAILED_DETAILS
    TOTAL_TESTS = 0
    PASSED_TESTS = 0
    FAILED_DETAILS = []

    # --- ajouter ---
    test(student.ajouter,  3,   1,   2)
    test(student.ajouter,  0,  -1,   1)
    test(student.ajouter, 15,  10,   5)
    test(student.ajouter,  0,   0,   0)
    test(student.ajouter, -5,  -2,  -3)

    # --- soustraire ---
    test(student.soustraire,  1,   3,  2)
    test(student.soustraire,  6,   3, -3)
    test(student.soustraire, -6,  -3,  3)
    test(student.soustraire,  0,   5,  5)
    test(student.soustraire, 42,  42,  0)

    # --- multiplier ---
    test(student.multiplier, 18,   3,   6)
    test(student.multiplier, 18,  -3,  -6)
    test(student.multiplier,-18,   3,  -6)
    test(student.multiplier,  0,   5,   0)
    test(student.multiplier,  7,   1,   7)

    # --- pair ---
    test(student.pair, True,   2)
    test(student.pair, False,  3)
    test(student.pair, True,   0)
    test(student.pair, False,  1)
    test(student.pair, True,  -4)
    test(student.pair, False, -7)

    # --- carre ---
    test(student.carre,  0,  0)
    test(student.carre,  1,  1)
    test(student.carre,  9,  3)
    test(student.carre, 25,  5)
    test(student.carre,  9, -3)

    # --- comparer ---
    test(student.comparer, "a > b",  5,  3)
    test(student.comparer, "a < b",  2,  7)
    test(student.comparer, "a == b", 4,  4)
    test(student.comparer, "a < b", -1,  0)
    test(student.comparer, "a > b",  0, -1)
    test(student.comparer, "a == b", 0,  0)

    # --- difference_carres ---
    for a, b in [(5, 3), (4, 7), (6, 6), (0, 4), (-3, 2)]:
        try:
            left  = student.difference_carres_gauche(a, b)
            right = student.difference_carres_droite(a, b)
            TOTAL_TESTS += 1
            if left == right:
                PASSED_TESTS += 1
            else:
                FAILED_DETAILS.append(
                    f"  ❌ difference_carres({a}, {b}) → gauche={repr(left)}, droite={repr(right)} — l'identité n'est pas vérifiée !"
                )
        except Exception as e:
            TOTAL_TESTS += 1
            FAILED_DETAILS.append(
                f"  💥 difference_carres({a}, {b}) → erreur : {e}"
            )

def show_results(student_name):
    global TOTAL_TESTS,PASSED_TESTS,FAILED_DETAILS
    print("\n--- RESULTS ---")
    print(f"Score: {PASSED_TESTS}/{TOTAL_TESTS}")

    percentage = (PASSED_TESTS / TOTAL_TESTS) * 100

    if percentage == 100:
        level = "Advanced"
    elif percentage >= 60:
        level = "Intermediate"
    else:
        level = "Beginner"

    print("Level:", level)
    
    print("\nDetails:")
    for fail in FAILED_DETAILS:
        print(fail)
        


if __name__ == "__main__":
    try:
        result = load_student_file()

        if result is None:
            input("\nAppuyez sur Entrée pour quitter...")
        else:
            student, student_name = result

            run_tests(student)
            show_results(student_name)

    except Exception:
        print("Crash du programme.")
        traceback.print_exc()