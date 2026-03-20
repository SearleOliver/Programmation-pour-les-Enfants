import importlib.util
import traceback

spec = importlib.util.spec_from_file_location("eval1", "eval1.py")
eval1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eval1)

TOTAL_TESTS = 0
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

def run_tests():

    # --- add ---
    test(eval1.add,  3,   1,   2)
    test(eval1.add,  0,  -1,   1)
    test(eval1.add, 15,  10,   5)
    test(eval1.add,  0,   0,   0)
    test(eval1.add, -5,  -2,  -3)

    # --- substract ---
    test(eval1.substract,  1,   3,  2)
    test(eval1.substract,  6,   3, -3)
    test(eval1.substract, -6,  -3,  3)
    test(eval1.substract,  0,   5,  5)
    test(eval1.substract, 42,  42,  0)

    # --- multiply ---
    test(eval1.multiply, 18,   3,   6)
    test(eval1.multiply, 18,  -3,  -6)
    test(eval1.multiply,-18,   3,  -6)
    test(eval1.multiply,  0,   5,   0)
    test(eval1.multiply,  7,   1,   7)

    # --- is_even ---
    test(eval1.is_even, True,   2)
    test(eval1.is_even, False,  3)
    test(eval1.is_even, True,   0)
    test(eval1.is_even, False,  1)
    test(eval1.is_even, True,  -4)
    test(eval1.is_even, False, -7)

    # --- square ---
    test(eval1.square,  0,  0)
    test(eval1.square,  1,  1)
    test(eval1.square,  9,  3)
    test(eval1.square, 25,  5)
    test(eval1.square,  9, -3)

    # --- compare ---
    test(eval1.compare, "a > b",  5,  3)
    test(eval1.compare, "a < b",  2,  7)
    test(eval1.compare, "a == b", 4,  4)
    test(eval1.compare, "a < b", -1,  0)
    test(eval1.compare, "a > b",  0, -1)
    test(eval1.compare, "a == b", 0,  0)

    # --- difference_squares : left == right is the lesson ---
    for a, b in [(5, 3), (4, 7), (6, 6), (0, 4), (-3, 2)]:
        try:
            left  = eval1.difference_squares_left(a, b)
            right = eval1.difference_squares_right(a, b)
            global TOTAL_TESTS, PASSED_TESTS
            TOTAL_TESTS += 1
            if left == right:
                PASSED_TESTS += 1
            else:
                FAILED_DETAILS.append(
                    f"  ❌ difference_squares({a}, {b}) → gauche={repr(left)}, droite={repr(right)} — l'identité n'est pas vérifiée !"
                )
        except Exception as e:
            TOTAL_TESTS += 1
            FAILED_DETAILS.append(
                f"  💥 difference_squares({a}, {b}) → erreur : {e}"
            )

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

def run_all_tests():
    try:
        run_tests()
        show_results()
    except Exception:
        print("Votre programme a planté.")
        traceback.print_exc()

if __name__ == "__main__":
    run_all_tests()