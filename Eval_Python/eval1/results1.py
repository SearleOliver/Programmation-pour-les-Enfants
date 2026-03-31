import os
import importlib.util

def load_student(file_name):
    spec = importlib.util.spec_from_file_location(file_name, file_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def grade_student(student):
    def run_tests(tests):
        passed = 0
        total = len(tests)

        for func, expected, args in tests:
            try:
                if func(*args) == expected:
                    passed += 1
            except:
                pass

        return passed, total

    results = {}

    # --- ajouter ---
    results["ajouter"] = run_tests([
        (student.ajouter, 3, (1, 2)),
        (student.ajouter, 0, (-1, 1)),
        (student.ajouter, 15, (10, 5)),
        (student.ajouter, 0, (0, 0)),
        (student.ajouter, -5, (-2, -3)),
    ])

    # --- soustraire ---
    results["soustraire"] = run_tests([
        (student.soustraire, 1, (3, 2)),
        (student.soustraire, 6, (3, -3)),
        (student.soustraire, -6, (-3, 3)),
        (student.soustraire, 0, (5, 5)),
        (student.soustraire, 42, (42, 0)),
    ])

    # --- multiplier ---
    results["multiplier"] = run_tests([
        (student.multiplier, 18, (3, 6)),
        (student.multiplier, 18, (-3, -6)),
        (student.multiplier, -18, (3, -6)),
        (student.multiplier, 0, (5, 0)),
        (student.multiplier, 7, (1, 7)),
    ])

    # --- pair ---
    results["pair"] = run_tests([
        (student.pair, True, (2,)),
        (student.pair, False, (3,)),
        (student.pair, True, (0,)),
        (student.pair, False, (1,)),
        (student.pair, True, (-4,)),
        (student.pair, False, (-7,)),
    ])

    # --- carre ---
    results["carre"] = run_tests([
        (student.carre, 0, (0,)),
        (student.carre, 1, (1,)),
        (student.carre, 9, (3,)),
        (student.carre, 25, (5,)),
        (student.carre, 9, (-3,)),
    ])

    # --- comparer ---
    results["comparer"] = run_tests([
        (student.comparer, "a > b", (5, 3)),
        (student.comparer, "a < b", (2, 7)),
        (student.comparer, "a == b", (4, 4)),
        (student.comparer, "a < b", (-1, 0)),
        (student.comparer, "a > b", (0, -1)),
        (student.comparer, "a == b", (0, 0)),
    ])
    
    results["difference_carre"] = run_tests([
    (student.difference_carres_gauche, -5, (2, 3)),
    (student.difference_carres_droite, -5, (2, 3)),
    (student.difference_carres_gauche, 12, (-4, 2)),
    (student.difference_carres_droite, 12, (-4, 2)),
    (student.difference_carres_gauche, 5, (-3, -2)),
    (student.difference_carres_droite, 5, (-3, -2)),
    ])

    return results


def main():
    files = [f for f in os.listdir() if f.startswith("eval1_") and f.endswith(".py")]

    if not files:
        print("No student files found.")
        return

    with open("results_eval1.csv", "w") as f:
        f.write("Name,ajouter,soustraire,multiplier,pair,carre,comparer,difference_carre,Total,Level\n")

        for file in files:
            student_name = file.replace("eval1_", "").replace(".py", "")
            student_name = student_name.replace("_", " ").title()

            try:
                student = load_student(file)
                results = grade_student(student)

                print(f"\n--- {student_name} ---")

                total_passed = 0
                total_tests = 0

                for exercise, (passed, total) in results.items():
                    print(f"{exercise}: {passed}/{total}")
                    total_passed += passed
                    total_tests += total

                percentage = (total_passed / total_tests) * 100

                if percentage == 100:
                    level = "Advanced"
                elif percentage >= 60:
                    level = "Intermediate"
                else:
                    level = "Beginner"

                print(f"\nTOTAL: {total_passed}/{total_tests} ({level})")

                f.write(
                        f"{student_name},"
                        f"{results['ajouter'][0]}/{results['ajouter'][1]},"
                        f"{results['soustraire'][0]}/{results['soustraire'][1]},"
                        f"{results['multiplier'][0]}/{results['multiplier'][1]},"
                        f"{results['pair'][0]}/{results['pair'][1]},"
                        f"{results['carre'][0]}/{results['carre'][1]},"
                        f"{results['comparer'][0]}/{results['comparer'][1]},"
                        f"{results['difference_carre'][0]}/{results['difference_carre'][1]},"
                        f"{total_passed}/{total_tests},{level}\n"
                    )
            except Exception as e:
                print(f"{student_name}: ERROR → {e}")
                f.write(f"{student_name},ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR\n")


if __name__ == "__main__":
    main()