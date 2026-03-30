import os
import importlib.util

def load_student(file_name):
    spec = importlib.util.spec_from_file_location(file_name, file_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

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

def grade_student(student):
    def run_tests(tests, label):
        passed = 0
        total = len(tests)
        failures = []

        for func, expected, args in tests:
            try:
                result = func(*args)
                if result == expected:
                    passed += 1
                else:
                    failures.append(
                        f"  ❌ {label}{args} → reçu {repr(result)}, attendu {repr(expected)}"
                    )
            except Exception as e:
                failures.append(
                    f"  💥 {label}{args} → erreur : {e}"
                )

        return passed, total, failures

    results = {}
    all_failures = []

    # --- perimetre_rectangle ---
    results["perimetre_rectangle"] = run_tests([
        (student.perimetre_rectangle, 14, (4, 3)),
        (student.perimetre_rectangle, 20, (6, 4)),
        (student.perimetre_rectangle, 8,  (2, 2)),
        (student.perimetre_rectangle, 22, (10, 1)),
        (student.perimetre_rectangle, 0,  (0, 0)),
    ], "perimetre_rectangle")

    # --- surface_rectangle ---
    results["surface_rectangle"] = run_tests([
        (student.surface_rectangle, 12, (4, 3)),
        (student.surface_rectangle, 24, (6, 4)),
        (student.surface_rectangle, 0,  (5, 0)),
        (student.surface_rectangle, 1,  (1, 1)),
        (student.surface_rectangle,100,(10,10)),
    ], "surface_rectangle")

    # --- perimetre_carre (reuse) ---
    def test_reuse_perimetre_carre(a):
        try:
            expected = student.perimetre_rectangle(a, a)
            result = student.perimetre_carre(a)
            return result == expected, f"perimetre_carre({a})"
        except Exception as e:
            return False, f"💥 perimetre_carre({a}) → erreur : {e}"

    passed = 0
    total = 5
    failures = []
    for a in [1, 3, 5, 7, 10]:
        ok, msg = test_reuse_perimetre_carre(a)
        if ok:
            passed += 1
        else:
            failures.append(msg)

    results["perimetre_carre"] = (passed, total, failures)

    # --- surface_carre ---
    passed = 0
    total = 5
    failures = []
    for a in [1, 3, 5, 7, 10]:
        try:
            expected = student.surface_rectangle(a, a)
            result = student.surface_carre(a)
            if result == expected:
                passed += 1
            else:
                failures.append(
                    f"❌ surface_carre({a}) → reçu {result}, attendu {expected}"
                )
        except Exception as e:
            failures.append(f"💥 surface_carre({a}) → erreur : {e}")

    results["surface_carre"] = (passed, total, failures)

    # --- perimetre_triangle ---
    results["perimetre_triangle"] = run_tests([
        (student.perimetre_triangle, 12, (3,4,5)),
        (student.perimetre_triangle, 9,  (3,3,3)),
        (student.perimetre_triangle,15,  (5,5,5)),
        (student.perimetre_triangle,11,  (2,4,5)),
        (student.perimetre_triangle,0,   (0,0,0)),
    ], "perimetre_triangle")

    # --- equilateral ---
    results["equilateral"] = run_tests([
        (student.equilateral, True,  (3,3,3)),
        (student.equilateral, True,  (7,7,7)),
        (student.equilateral, False, (3,3,4)),
        (student.equilateral, False, (3,4,5)),
        (student.equilateral, False, (1,2,1)),
    ], "equilateral")

    # --- comparer_surfaces ---
    results["comparer_surfaces"] = run_tests([
        (student.comparer_surfaces, "rectangle", (4,3,3)),
        (student.comparer_surfaces, "carré",     (2,3,3)),
        (student.comparer_surfaces, "égaux",      (3,3,3)),
        (student.comparer_surfaces, "rectangle", (10,1,3)),
        (student.comparer_surfaces, "carré",     (1,1,5)),
    ], "comparer_surfaces")

    # --- polynomial ---
    results["polynomial"] = run_tests([
        (student.polynomial, 3,  (0,0,3,99)),
        (student.polynomial, 6,  (1,0,2,2)),
        (student.polynomial, 27, (1,2,3,4)),
        (student.polynomial, 0,  (1,0,0,0)),
        (student.polynomial, 11, (2,1,1,2)),
        (student.polynomial, 5,  (-1,0,6,1)),
    ], "polynomial")

    return results


def main():
    files = [f for f in os.listdir() if f.startswith("eval2_") and f.endswith(".py")]

    if not files:
        print("No student files found.")
        return

    with open("results_eval2.csv", "w") as f:
        f.write("Name,perimetre_rectangle,surface_rectangle,perimetre_carre,surface_carre,perimetre_triangle,equilateral,comparer_surfaces,polynomial,Total,Level\n")

        for file in files:
            student_name = file.replace("eval2_", "").replace(".py", "")
            student_name = student_name.replace("_", " ").title()

            try:
                student = load_student(file)
                results = grade_student(student)

                print(f"\n--- {student_name} ---")

                total_passed = 0
                total_tests = 0

                for exercise, (passed, total, failures) in results.items():
                    print(f"{exercise}: {passed}/{total}")
                    total_passed += passed
                    total_tests += total

                    for fail in failures:
                        print(fail)

                percentage = (total_passed / total_tests) * 100

                if percentage == 100:
                    level = "Advanced"
                elif percentage >= 60:
                    level = "Intermediate"
                else:
                    level = "Beginner"

                print(f"\nTOTAL: {total_passed}/{total_tests} ({level})\n")

                f.write("Name,perimetre_rectangle,surface_rectangle,perimetre_carre,surface_carre,perimetre_triangle,equilateral,comparer_surfaces,polynomial,Total,Level\n")

            except Exception:
                print(f"{student_name}: ERROR")
                f.write(f"{student_name},ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR\n")


if __name__ == "__main__":
    main()