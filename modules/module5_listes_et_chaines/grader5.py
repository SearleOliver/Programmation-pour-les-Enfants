import importlib.util
import traceback
import os

def load_student_file():
    files = [f for f in os.listdir() if f.startswith("eval5_") and f.endswith(".py")]

    if len(files) == 0:
        print("❌ Aucun fichier eval5 trouvé.")
        return None

    if len(files) > 1:
        print("❌ Plusieurs fichiers trouvés. Gardez seulement le vôtre.")
        return None

    file = files[0]

    spec = importlib.util.spec_from_file_location("student", file)
    student = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student)

    print(f"✔ Fichier chargé : {file}")
    return student


def run_tests(student):
    results = {}

    def run_tests_group(tests, label):
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
                        f"❌ {label}{args} → reçu {result}, attendu {expected}"
                    )
            except Exception as e:
                failures.append(
                    f"💥 {label}{args} → ERROR in {func.__name__}: {e}"
                )

        return passed, total, failures
    
    results["somme_liste"] = run_tests_group([
        (student.somme_liste,  0, ([],)),
        (student.somme_liste,  1, ([1],)),
        (student.somme_liste, 10, ([1, 2, 3, 4],)),
        (student.somme_liste, 15, ([1, 2, 3, 4, 5]),),
        (student.somme_liste,  0, ([-3, 0, 3]),),
    ], "somme_liste")
    
    results["nombre_occurences"] = run_tests_group([
        (student.nombre_occurrences, 0, ([],1)),
        (student.nombre_occurrences, 1, ([1],       1)),
        (student.nombre_occurrences, 2, ([1,2,2,3], 2)),
        (student.nombre_occurrences, 0, ([1,2,3],   9)),
        (student.nombre_occurrences, 3, ([5,5,5],   5)),
    ], "nombre_occurences")

    results["max_liste"] = run_tests_group([
        (student.max_liste,  1, ([1],)),
        (student.max_liste,  9, ([3, 1, 4, 1, 5, 9],)),
        (student.max_liste,  0, ([-3, -1, 0],)),
        (student.max_liste, 42, ([10, 42, 7],)),
        (student.max_liste,  5, ([5, 5, 5],)),
    ], "max_liste")

    results["compter_elements"] = run_tests_group([
        (student.compter_elements, {"a":2,"b":1}, (["a","b","a"],)),
        (student.compter_elements, {}, ([],)),
    ], "compter_elements")

    results["fusion_listes"] = run_tests_group([
        (student.fusion_listes, [1,2,3,4], ([1,2],[3,4])),
        (student.fusion_listes, [], ([],[])),
    ], "fusion_listes")

    results["inverser_dictionnaire"] = run_tests_group([
        (student.inverser_dictionnaire, {1:"a",2:"b"}, ({"a":1,"b":2},)),
    ], "inverser_dictionnaire")

    results["somme_valeurs"] = run_tests_group([
        (student.somme_valeurs, 6, ({"a":1,"b":2,"c":3},)),
        (student.somme_valeurs, 0, ({},)),
    ], "somme_valeurs")

    results["max_cle"] = run_tests_group([
        (student.max_cle, "b", ({"a":1,"b":5,"c":3},)),
    ], "max_cle")

    results["filtrer_pairs"] = run_tests_group([
        (student.filtrer_pairs, [2,4], ([1,2,3,4],)),
        (student.filtrer_pairs, [], ([1,3,5],)),
    ], "filtrer_pairs")

    results["compter_mots"] = run_tests_group([
        (student.compter_mots, {"hello":2,"world":1}, ("hello world hello",)),
    ], "compter_mots")

    return results


def display(results):
    total_passed = 0
    total_tests = 0

    print("\n--- RESULTS ---")

    for ex, (p, t, fails) in results.items():
        print(f"{ex}: {p}/{t}")
        total_passed += p
        total_tests += t
        for f in fails:
            print(f)

    percent = (total_passed / total_tests) * 100

    if percent == 100:
        level = "Advanced"
    elif percent >= 60:
        level = "Intermediate"
    else:
        level = "Beginner"

    print(f"\nTOTAL: {total_passed}/{total_tests} ({level})")
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    try:
        student = load_student_file()
        if student is None:
            input("\nAppuyez sur Entrée pour quitter...")
        else:
            results = run_tests(student)
            display(results)
    except Exception:
        print("Crash du programme.")
        traceback.print_exc()