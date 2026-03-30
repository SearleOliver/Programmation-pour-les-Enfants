
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

    # --- compter_elements ---
    results["compter"] = run_tests([
        (student.compter_elements,{"a":2}, (["a","a"],)),
        (student.compter_elements, {"b":2}, (["b","b"],)),
        (student.compter_elements, {"a":1,"b":1}, (["a","b"],)),
        (student.compter_elements,{"a":2,"b":1,"c":1}, (["a","a","b","c"],)),
    ])

    # --- fusion_listes ---
    results["fusion"] = run_tests([
        (student.fusion_listes,[1,4,2], ([1,4],[2])),
        (student.fusion_listes,[1,2], ([1],[2])),
        (student.fusion_listes,[23,-1,2,7], ([23,-1],[2,7])),
        (student.fusion_listes,[1], ([1],[])),
    ])

    # --- inverser ---
    results["inverser"] = run_tests([
        (student.inverser_dictionnaire, {1:"a"}, ({"a":1},)),
        (student.inverser_dictionnaire, {7:"a"}, ({"a":7},)),
        (student.inverser_dictionnaire, {1:"a",9:"b",13:"x"}, ({"a":1,"b":9,"x":13},)),
        (student.inverser_dictionnaire, {1:"a",4:"b"}, ({"a":1,"b":4},)),
    ])

    # --- somme ---
    results["somme"] = run_tests([
        (student.somme_valeurs, 3, ({"a":1,"b":2},)),
        (student.somme_valeurs, 3, ({"a":1,"b":1,"d":1},)),
        (student.somme_valeurs, 6, ({"a":1,"b":2,"d":3},)),
        (student.somme_valeurs, 82, ({"a":4,"b":78},)),
    ])

    # --- max_cle ---
    results["max_cle"] = run_tests([
        (student.max_cle,"b", ({"a":1,"b":2},)),
        (student.max_cle, "a", ({"a":1,"b":1},)),
        (student.max_cle,"a", ({"a":9,"b":7,"c":9},)),
        (student.max_cle,"y", ({"z":27,"d":2,"y":29},)),
    ])

    # --- filtrer_pairs ---
    results["filtrer"] = run_tests([
        (student.filtrer_pairs, [2,4], ([1,2,3,4],)),
        (student.filtrer_pairs, [9,12,24], ([8,9,12,24,27],)),
        (student.filtrer_pairs, [0,-2,-4], ([0,-1,-2,-3,-4],)),
        (student.filtrer_pairs, [], ([37,39,47],)),
    ])
    
    # --- compter_mots ---
    results["compter_mots"] = run_tests([
        (student.compter_mots,  {"hi":2}, ("hi hi",)),
        (student.compter_mots,  {"Hello":2,"world":1}, ("Hello world Hello",)),
        (student.compter_mots,  {"Oh":1,"my":1,"god":1}, ("Oh my god",)),
        (student.compter_mots,  {"hi":1,"Hi":1,"hI":1}, ("hi Hi hI",)),
    ])

    return results


def main():
    files = [f for f in os.listdir() if f.startswith("eval4_") and f.endswith(".py")]

    if not files:
        print("No student files found.")
        return

    with open("results_eval4.csv", "w") as f:
        f.write("Name,compter,fusion,inverser,somme,max_cle,filtrer,compter_mots,Total,Level\n")

        for file in files:
            student_name = file.replace("eval4_", "").replace(".py", "")
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
                        f"{results['compter'][0]}/{results['compter'][1]},"
                        f"{results['fusion'][0]}/{results['fusion'][1]},"
                        f"{results['inverser'][0]}/{results['inverser'][1]},"
                        f"{results['somme'][0]}/{results['somme'][1]},"
                        f"{results['max_cle'][0]}/{results['max_cle'][1]},"
                        f"{results['filtrer'][0]}/{results['filtrer'][1]},"
                        f"{results['compter_mots'][0]}/{results['compter_mots'][1]},"
                        f"{total_passed}/{total_tests},{level}\n"
                    )

            except Exception:
                print(f"{student_name}: ERROR")
                f.write(f"{student_name},ERROR,ERROR,ERROR\n")


if __name__ == "__main__":
    main()