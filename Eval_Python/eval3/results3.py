import os
import importlib.util

def load_student(file_name):
    spec = importlib.util.spec_from_file_location(file_name, file_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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

    # --- somme_a ---
    results["somme_a"] = run_tests([
        (student.somme_a, 0, (0,)),
        (student.somme_a, 1, (1,)),
        (student.somme_a,10, (4,)),
        (student.somme_a,15, (5,)),
        (student.somme_a,55, (10,)),
    ], "somme_a")

    # --- somme_paire_a ---
    results["somme_paire_a"] = run_tests([
        (student.somme_paire_a, 0, (1,)),
        (student.somme_paire_a, 2, (2,)),
        (student.somme_paire_a, 6, (5,)),
        (student.somme_paire_a,12, (6,)),
        (student.somme_paire_a,30, (10,)),
    ], "somme_paire_a")

    # --- somme_liste ---
    results["somme_liste"] = run_tests([
        (student.somme_liste, 0, ([],)),
        (student.somme_liste, 1, ([1],)),
        (student.somme_liste,10, ([1,2,3,4],)),
        (student.somme_liste,15, ([1,2,3,4,5],)),
        (student.somme_liste, 0, ([-3,0,3],)),
    ], "somme_liste")

    # --- nombre_occurrences ---
    results["nombre_occurrences"] = run_tests([
        (student.nombre_occurrences,0, ([],1)),
        (student.nombre_occurrences,1, ([1],1)),
        (student.nombre_occurrences,2, ([1,2,2,3],2)),
        (student.nombre_occurrences,0, ([1,2,3],9)),
        (student.nombre_occurrences,3, ([5,5,5],5)),
    ], "nombre_occurrences")

    # --- max_liste ---
    results["max_liste"] = run_tests([
        (student.max_liste,1, ([1],)),
        (student.max_liste,9, ([3,1,4,1,5,9],)),
        (student.max_liste,0, ([-3,-1,0],)),
        (student.max_liste,42,([10,42,7],)),
        (student.max_liste,5, ([5,5,5],)),
    ], "max_liste")

    # --- somme_while ---
    results["somme_while"] = run_tests([
        (student.somme_while,0, (0,)),
        (student.somme_while,1, (1,)),
        (student.somme_while,10,(4,)),
        (student.somme_while,15,(5,)),
        (student.somme_while,55,(10,)),
    ], "somme_while")

    # --- factorielle ---
    results["factorielle"] = run_tests([
        (student.factorielle,1,(0,)),
        (student.factorielle,1,(1,)),
        (student.factorielle,2,(2,)),
        (student.factorielle,6,(3,)),
        (student.factorielle,24,(4,)),
        (student.factorielle,120,(5,)),
    ], "factorielle")

    # --- fizzbuzz ---
    results["fizzbuzz"] = run_tests([
        (student.fizzbuzz,[],(0,)),
        (student.fizzbuzz,[1],(1,)),
        (student.fizzbuzz,[1,2,"Fizz",4,"Buzz"],(5,)),
        (student.fizzbuzz,[1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz","Buzz"],(10,)),
        (student.fizzbuzz,[1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz","Buzz",
                           11,"Fizz",13,14,"FizzBuzz"],(15,)),
    ], "fizzbuzz")

    return results


def main():
    files = [f for f in os.listdir() if f.startswith("eval3_") and f.endswith(".py")]

    if not files:
        print("No student files found.")
        return

    with open("results_eval3.csv", "w") as f:
        f.write("Name,somme_a,somme_paire_a,somme_liste,nombre_occurrences,max_liste,somme_while,factorielle,fizzbuzz,Total,Level\n")

        for file in files:
            student_name = file.replace("eval3_", "").replace(".py", "")
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

                print(f"\nTOTAL: {total_passed}/{total_tests} ({level})")

                f.write(
                    f"{student_name},"
                    f"{results['somme_a'][0]}/{results['somme_a'][1]},"
                    f"{results['somme_paire_a'][0]}/{results['somme_paire_a'][1]},"
                    f"{results['somme_liste'][0]}/{results['somme_liste'][1]},"
                    f"{results['nombre_occurrences'][0]}/{results['nombre_occurrences'][1]},"
                    f"{results['max_liste'][0]}/{results['max_liste'][1]},"
                    f"{results['somme_while'][0]}/{results['somme_while'][1]},"
                    f"{results['factorielle'][0]}/{results['factorielle'][1]},"
                    f"{results['fizzbuzz'][0]}/{results['fizzbuzz'][1]},"
                    f"{total_passed}/{total_tests},{level}\n"
                )

            except Exception:
                print(f"{student_name}: ERROR")
                f.write(f"{student_name},ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR,ERROR\n")


if __name__ == "__main__":
    main()