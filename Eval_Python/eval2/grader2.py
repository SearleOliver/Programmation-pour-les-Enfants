import importlib.util
import traceback
import os

def load_student_file():
    files = [f for f in os.listdir() if f.startswith("eval2_") and f.endswith(".py")]

    if len(files) == 0:
        print("❌ Aucun fichier eval2 trouvé.")
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

def test_reuse(result, expected, label):
    """Used for tests where expected is computed from another student function.
    Guards against None == None passing when neither function is implemented."""
    global TOTAL_TESTS, PASSED_TESTS
    TOTAL_TESTS += 1
    if expected is None:
        FAILED_DETAILS.append(
            f"  ⚠️  {label} → fonction de référence non implémentée, impossible de comparer"
        )
    elif result is None:
        FAILED_DETAILS.append(
            f"  ❌ {label} → reçu None, attendu {repr(expected)}"
        )
    elif result == expected:
        PASSED_TESTS += 1
    else:
        FAILED_DETAILS.append(
            f"  ❌ {label} → reçu {repr(result)}, attendu {repr(expected)}"
        )

def run_tests(student):

    # --- perimetre_rectangle : 2 * (l + w) ---
    test(student.perimetre_rectangle, 14,  4,  3)
    test(student.perimetre_rectangle, 20,  6,  4)
    test(student.perimetre_rectangle,  8,  2,  2)
    test(student.perimetre_rectangle, 22, 10,  1)
    test(student.perimetre_rectangle,  0,  0,  0)

    # --- surface_rectangle : l * w ---
    test(student.surface_rectangle, 12,  4,  3)
    test(student.surface_rectangle, 24,  6,  4)
    test(student.surface_rectangle,  0,  5,  0)
    test(student.surface_rectangle,  1,  1,  1)
    test(student.surface_rectangle,100, 10, 10)

    # --- square_perimeter ---
    for a in [1, 3, 5, 7, 10]:
        expected = student.perimetre_rectangle(a, a)
        try:
            result = student.square_perimeter(a)
        except Exception as e:
            global TOTAL_TESTS, PASSED_TESTS
            TOTAL_TESTS += 1
            FAILED_DETAILS.append(f"  💥 perimetre_carre({a}) → erreur : {e}")
            continue
        test_reuse(result, expected, f"perimetre_carre({a})")

    # --- square_area ---
    for a in [1, 3, 5, 7, 10]:
        expected = student.surface_rectangle(a, a)
        try:
            result = student.surface_carre(a)
        except Exception as e:
            TOTAL_TESTS += 1
            FAILED_DETAILS.append(f"  💥 surface_carre({a}) → erreur : {e}")
            continue
        test_reuse(result, expected, f"surface_carre({a})")

    # --- triangle_perimeter : a + b + c ---
    test(student.perimetre_triangle, 12,  3,  4,  5)
    test(student.perimetre_triangle,  9,  3,  3,  3)
    test(student.perimetre_triangle, 15,  5,  5,  5)
    test(student.perimetre_triangle, 11,  2,  4,  5)
    test(student.perimetre_triangle,  0,  0,  0,  0)

    # --- is_equilateral ---
    test(student.equilateral, True,   3,  3,  3)
    test(student.equilateral, True,   7,  7,  7)
    test(student.equilateral, False,  3,  3,  4)
    test(student.equilateral, False,  3,  4,  5)
    test(student.equilateral, False,  1,  2,  1)

    # --- compare_areas ---
    test(student.comparer_surfaces, "rectangle",  4,  3,  3)  # 12 > 9
    test(student.comparer_surfaces, "carre",      2,  3,  3)  # 6  < 9
    test(student.comparer_surfaces, "égaux",       3,  3,  3)  # 9 == 9
    test(student.comparer_surfaces, "rectangle", 10,  1,  3)  # 10 > 9
    test(student.comparer_surfaces, "carre",      1,  1,  5)  # 1  < 25

    # --- polynomial : ax² + bx + c ---
    test(student.polynomial,  3,  0,  0,  3, 99)  # 0+0+3       = 3
    test(student.polynomial,  6,  1,  0,  2,  2)  # 4+0+2       = 6
    test(student.polynomial, 27,  1,  2,  3,  4)  # 16+8+3      = 27
    test(student.polynomial,  0,  1,  0,  0,  0)  # 0+0+0       = 0
    test(student.polynomial, 11,  2,  1,  1,  2)  # 8+2+1       = 11
    test(student.polynomial,  5, -1,  0,  6,  1)  # -1+0+6      = 5

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