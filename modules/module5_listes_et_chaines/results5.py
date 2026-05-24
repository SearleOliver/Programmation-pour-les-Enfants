
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

    results["somme_liste"] = run_tests([
        (student.somme_liste,  0, ([],)),
        (student.somme_liste,  1, ([1],)),
        (student.somme_liste, 10, ([1, 2, 3, 4],)),
        (student.somme_liste, 15, ([1, 2, 3, 4, 5]),),
        (student.somme_liste,  0, ([-3, 0, 3]),),
    ], "somme_liste")
    
    results["nombre_occurences"] = run_tests([
        (student.nombre_occurrences, 0, ([],1)),
        (student.nombre_occurrences, 1, ([1],       1)),
        (student.nombre_occurrences, 2, ([1,2,2,3], 2)),
        (student.nombre_occurrences, 0, ([1,2,3],   9)),
        (student.nombre_occurrences, 3, ([5,5,5],   5)),
    ], "nombre_occurences")

    results["max_liste"] = run_tests([
        (student.max_liste,  1, ([1],)),
        (student.max_liste,  9, ([3, 1, 4, 1, 5, 9],)),
        (student.max_liste,  0, ([-3, -1, 0],)),
        (student.max_liste, 42, ([10, 42, 7],)),
        (student.max_liste,  5, ([5, 5, 5],)),
    ], "max_liste")

    results["fusion_listes"] = run_tests([
        (student.fusion_listes, [1,2,3,4], ([1,2],[3,4])),
        (student.fusion_listes, [], ([],[])),
    ], "fusion_listes")

    results["filtrer_pairs"] = run_tests([
        (student.filtrer_pairs, [2,4], ([1,2,3,4],)),
        (student.filtrer_pairs, [], ([1,3,5],)),
    ], "filtrer_pairs")

    return results


def main():
    files = [f for f in os.listdir() if f.startswith("eval5_") and f.endswith(".py")]

    if not files:
        print("No student files found.")
        return

    with open("results_eval5.csv", "w") as f:
        f.write("Name,fusion,nombre_occ,max,fusion,filtrer,Total,Level\n")

        for file in files:
            student_name = file.replace("eval5_", "").replace(".py", "")
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
                        f"{results['somme_liste'][0]}/{results['somme_liste'][1]},"
                        f"{results['nombre_occurences'][0]}/{results['nombre_occurences'][1]},"
                        f"{results['max_liste'][0]}/{results['max_liste'][1]},"
                        f"{results['fusion_listes'][0]}/{results['fusion_listes'][1]},"
                        f"{results['filtrer_pairs'][0]}/{results['filtrer_pairs'][1]},"
                        f"{total_passed}/{total_tests},{level}\n"
                    )

            except Exception:
                print(f"{student_name}: ERROR")
                f.write(f"{student_name},ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR\n")


if __name__ == "__main__":
    main()