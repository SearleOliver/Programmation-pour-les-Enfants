import importlib.util
import traceback

spec = importlib.util.spec_from_file_location("eval2", "eval2.py")
eval2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eval2)

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

def run_tests():

    # --- perimetre_rectangle : 2 * (l + w) ---
    test(eval2.perimetre_rectangle, 14,  4,  3)
    test(eval2.perimetre_rectangle, 20,  6,  4)
    test(eval2.perimetre_rectangle,  8,  2,  2)
    test(eval2.perimetre_rectangle, 22, 10,  1)
    test(eval2.perimetre_rectangle,  0,  0,  0)

    # --- surface_rectangle : l * w ---
    test(eval2.surface_rectangle, 12,  4,  3)
    test(eval2.surface_rectangle, 24,  6,  4)
    test(eval2.surface_rectangle,  0,  5,  0)
    test(eval2.surface_rectangle,  1,  1,  1)
    test(eval2.surface_rectangle,100, 10, 10)

    # --- square_perimeter ---
    # Must equal perimetre_rectangle(a, a) — tests reuse.
    # Uses test_reuse so that None == None cannot pass.
    for a in [1, 3, 5, 7, 10]:
        expected = eval2.perimetre_rectangle(a, a)
        try:
            result = eval2.square_perimeter(a)
        except Exception as e:
            global TOTAL_TESTS, PASSED_TESTS
            TOTAL_TESTS += 1
            FAILED_DETAILS.append(f"  💥 perimetre_carre({a}) → erreur : {e}")
            continue
        test_reuse(result, expected, f"perimetre_carre({a})")

    # --- square_area ---
    # Must equal surface_rectangle(a, a) — tests reuse.
    for a in [1, 3, 5, 7, 10]:
        expected = eval2.surface_rectangle(a, a)
        try:
            result = eval2.surface_carre(a)
        except Exception as e:
            TOTAL_TESTS += 1
            FAILED_DETAILS.append(f"  💥 surface_carre({a}) → erreur : {e}")
            continue
        test_reuse(result, expected, f"surface_carre({a})")

    # --- triangle_perimeter : a + b + c ---
    test(eval2.perimetre_triangle, 12,  3,  4,  5)
    test(eval2.perimetre_triangle,  9,  3,  3,  3)
    test(eval2.perimetre_triangle, 15,  5,  5,  5)
    test(eval2.perimetre_triangle, 11,  2,  4,  5)
    test(eval2.perimetre_triangle,  0,  0,  0,  0)

    # --- is_equilateral ---
    test(eval2.equilateral, True,   3,  3,  3)
    test(eval2.equilateral, True,   7,  7,  7)
    test(eval2.equilateral, False,  3,  3,  4)
    test(eval2.equilateral, False,  3,  4,  5)
    test(eval2.equilateral, False,  1,  2,  1)

    # --- compare_areas ---
    test(eval2.comparer_surfaces, "rectangle",  4,  3,  3)  # 12 > 9
    test(eval2.comparer_surfaces, "carre",      2,  3,  3)  # 6  < 9
    test(eval2.comparer_surfaces, "égaux",       3,  3,  3)  # 9 == 9
    test(eval2.comparer_surfaces, "rectangle", 10,  1,  3)  # 10 > 9
    test(eval2.comparer_surfaces, "carre",      1,  1,  5)  # 1  < 25

    # --- polynomial : ax² + bx + c ---
    test(eval2.polynomial,  3,  0,  0,  3, 99)  # 0+0+3       = 3
    test(eval2.polynomial,  6,  1,  0,  2,  2)  # 4+0+2       = 6
    test(eval2.polynomial, 27,  1,  2,  3,  4)  # 16+8+3      = 27
    test(eval2.polynomial,  0,  1,  0,  0,  0)  # 0+0+0       = 0
    test(eval2.polynomial, 11,  2,  1,  1,  2)  # 8+2+1       = 11
    test(eval2.polynomial,  5, -1,  0,  6,  1)  # -1+0+6      = 5

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

def run_all_tests():
    try:
        run_tests()
        show_results()
    except Exception:
        print("Votre programme a planté.")
        traceback.print_exc()
        input("\nAppuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    run_all_tests()