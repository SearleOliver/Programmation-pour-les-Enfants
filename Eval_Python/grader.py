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

    # --- ajouter ---
    test(eval1.ajouter,  3,   1,   2)
    test(eval1.ajouter,  0,  -1,   1)
    test(eval1.ajouter, 15,  10,   5)
    test(eval1.ajouter,  0,   0,   0)
    test(eval1.ajouter, -5,  -2,  -3)

    # --- soustraire ---
    test(eval1.soustraire,  1,   3,  2)
    test(eval1.soustraire,  6,   3, -3)
    test(eval1.soustraire, -6,  -3,  3)
    test(eval1.soustraire,  0,   5,  5)
    test(eval1.soustraire, 42,  42,  0)

    # --- multiplier ---
    test(eval1.multiplier, 18,   3,   6)
    test(eval1.multiplier, 18,  -3,  -6)
    test(eval1.multiplier,-18,   3,  -6)
    test(eval1.multiplier,  0,   5,   0)
    test(eval1.multiplier,  7,   1,   7)

    # --- pair ---
    test(eval1.pair, True,   2)
    test(eval1.pair, False,  3)
    test(eval1.pair, True,   0)
    test(eval1.pair, False,  1)
    test(eval1.pair, True,  -4)
    test(eval1.pair, False, -7)

    # --- carre ---
    test(eval1.carre,  0,  0)
    test(eval1.carre,  1,  1)
    test(eval1.carre,  9,  3)
    test(eval1.carre, 25,  5)
    test(eval1.carre,  9, -3)

    # --- comparer ---
    test(eval1.comparer, "a > b",  5,  3)
    test(eval1.comparer, "a < b",  2,  7)
    test(eval1.comparer, "a == b", 4,  4)
    test(eval1.comparer, "a < b", -1,  0)
    test(eval1.comparer, "a > b",  0, -1)
    test(eval1.comparer, "a == b", 0,  0)

    # --- difference_carres : left == right is the lesson ---
    for a, b in [(5, 3), (4, 7), (6, 6), (0, 4), (-3, 2)]:
        try:
            left  = eval1.difference_carres_gauche(a, b)
            right = eval1.difference_carres_droite(a, b)
            global TOTAL_TESTS, PASSED_TESTS
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

import os

def show_results(student_name):
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

    # Save to file
    file_exists = os.path.isfile("results.csv")

    with open("results.csv", "a") as f:
        if not file_exists:
            f.write("Name,Score,Total,Level\n")

        f.write(f"{student_name},{PASSED_TESTS},{TOTAL_TESTS},{level}\n")

    print("\nResult saved!")

    input("\nPress Enter to exit...")

def run_all_tests():
    try:
        student_name = input("Enter your name: ")
        run_tests()
        show_results(student_name)
    except Exception:
        print("Your program crashed.")
        traceback.print_exc()

if __name__ == "__main__":
    run_all_tests()