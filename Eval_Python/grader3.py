import importlib.util
import traceback

spec = importlib.util.spec_from_file_location("eval3", "eval3.py")
eval3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eval3)

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

def run_tests():

    # --- sum_to : 1 + 2 + ... + n ---
    test(eval3.sum_to,  0,  0)   # aucun entier à additionner
    test(eval3.sum_to,  1,  1)
    test(eval3.sum_to, 10,  4)   # 1+2+3+4
    test(eval3.sum_to, 15,  5)   # 1+2+3+4+5
    test(eval3.sum_to, 55, 10)   # classique

    # --- count_even_up_to ---
    test(eval3.count_even_up_to, 0,  1)   # 1..1 : aucun pair
    test(eval3.count_even_up_to, 1,  2)   # 1..2 : juste 2
    test(eval3.count_even_up_to, 2,  5)   # 1..5 : 2 et 4
    test(eval3.count_even_up_to, 3,  6)   # 1..6 : 2, 4, 6
    test(eval3.count_even_up_to, 5, 10)   # 1..10 : 2,4,6,8,10

    # --- sum_list ---
    test(eval3.sum_list,  0, [])
    test(eval3.sum_list,  1, [1])
    test(eval3.sum_list, 10, [1, 2, 3, 4])
    test(eval3.sum_list, 15, [1, 2, 3, 4, 5])
    test(eval3.sum_list,  0, [-3, 0, 3])     # négatifs qui s'annulent

    # --- count_occurrences ---
    test(eval3.count_occurrences, 0, [],        1)   # liste vide
    test(eval3.count_occurrences, 1, [1],       1)
    test(eval3.count_occurrences, 2, [1,2,2,3], 2)
    test(eval3.count_occurrences, 0, [1,2,3],   9)   # valeur absente
    test(eval3.count_occurrences, 3, [5,5,5],   5)   # tous identiques

    # --- max_list ---
    test(eval3.max_list,  1, [1])
    test(eval3.max_list,  9, [3, 1, 4, 1, 5, 9])
    test(eval3.max_list,  0, [-3, -1, 0])
    test(eval3.max_list, 42, [10, 42, 7])
    test(eval3.max_list,  5, [5, 5, 5])        # tous égaux

    # --- sum_while : même résultat que sum_to mais avec while ---
    test(eval3.sum_while,  0,  0)
    test(eval3.sum_while,  1,  1)
    test(eval3.sum_while, 10,  4)
    test(eval3.sum_while, 15,  5)
    test(eval3.sum_while, 55, 10)

    # --- factorial ---
    test(eval3.factorial,   1,  0)   # 0! = 1 — erreur fréquente de retourner 0 !
    test(eval3.factorial,   1,  1)
    test(eval3.factorial,   2,  2)
    test(eval3.factorial,   6,  3)
    test(eval3.factorial,  24,  4)
    test(eval3.factorial, 120,  5)

    # --- fizzbuzz ---
    test(eval3.fizzbuzz, [], 0)
    test(eval3.fizzbuzz, [1], 1)
    test(eval3.fizzbuzz,
        [1, 2, "Fizz", 4, "Buzz"],
        5)
    test(eval3.fizzbuzz,
        [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"],
        10)
    test(eval3.fizzbuzz,
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