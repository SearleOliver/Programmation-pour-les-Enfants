import importlib.util
import traceback
spec = importlib.util.spec_from_file_location("eval1", "eval1.py")
eval1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eval1)


TOTAL_TESTS = 0
PASSED_TESTS = 0


def test(func, expected, *args):
    global TOTAL_TESTS, PASSED_TESTS
    TOTAL_TESTS += 1
    try:
        result = func(*args)
        if result == expected:
            PASSED_TESTS += 1
    except Exception:
        pass


def run_tests():
    test(eval1.add, 3, 1, 2)
    test(eval1.add, 0, -1, 1)
    test(eval1.add, 15, 10, 5)

    test(eval1.is_even, True, 2)
    test(eval1.is_even, False, 3)
    test(eval1.is_even, True, 0)
    
    test(eval1.multiply, 2, 3, 6)
    test(eval1.multiply, 2, -3, -6)
    test(eval1.multiply, -6, -3, 18)
    
    test(eval1.substract, -6, -3, -3)
    test(eval1.substract, -6, 18, -24)
    test(eval1.substract, 3, 2, 1)
    


def show_results():
    print("\n--- RESULTS ---")
    print(f"Score: {PASSED_TESTS}/{TOTAL_TESTS}")

    percentage = (PASSED_TESTS / TOTAL_TESTS) * 100

    if percentage == 100:
        print("Parfait")
    elif percentage >= 80:
        print("Niveau Validé mais vous pouvez faire mieux.")
    else:
        print("Réessayez")


def run_all_tests():
    try:
        run_tests()
        show_results()
    except Exception:
        print("Your program crashed.")
        traceback.print_exc()
        
if __name__ == "__main__":
    run_all_tests()