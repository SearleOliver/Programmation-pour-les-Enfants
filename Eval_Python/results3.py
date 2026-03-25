import os
import importlib.util

def load_student(file_name):
    spec = importlib.util.spec_from_file_location(file_name, file_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def grade_student(student, student_name):
    total = 0
    passed = 0

    def test(func, expected, *args):
        nonlocal total, passed
        total += 1
        try:
            if func(*args) == expected:
                passed += 1
        except:
            pass

        # --- somme_a : 1 + 2 + ... + n ---
    test(student.somme_a,  0,  0)   # aucun entier à additionner
    test(student.somme_a,  1,  1)
    test(student.somme_a, 10,  4)   # 1+2+3+4
    test(student.somme_a, 15,  5)   # 1+2+3+4+5
    test(student.somme_a, 55, 10)   # classique

    # --- somme_paire_a ---
    test(student.somme_paire_a, 0,  1)   # 1..1 : aucun pair
    test(student.somme_paire_a, 1,  2)   # 1..2 : juste 2
    test(student.somme_paire_a, 2,  5)   # 1..5 : 2 et 4
    test(student.somme_paire_a, 3,  6)   # 1..6 : 2, 4, 6
    test(student.somme_paire_a, 5, 10)   # 1..10 : 2,4,6,8,10

    # --- somme_liste ---
    test(student.somme_liste,  0, [])
    test(student.somme_liste,  1, [1])
    test(student.somme_liste, 10, [1, 2, 3, 4])
    test(student.somme_liste, 15, [1, 2, 3, 4, 5])
    test(student.somme_liste,  0, [-3, 0, 3])     # négatifs qui s'annulent

    # --- nombre_occurrences ---
    test(student.nombre_occurrences, 0, [],        1)   # liste vide
    test(student.nombre_occurrences, 1, [1],       1)
    test(student.nombre_occurrences, 2, [1,2,2,3], 2)
    test(student.nombre_occurrences, 0, [1,2,3],   9)   # valeur absente
    test(student.nombre_occurrences, 3, [5,5,5],   5)   # tous identiques

    # --- max_list ---
    test(student.max_liste,  1, [1])
    test(student.max_liste,  9, [3, 1, 4, 1, 5, 9])
    test(student.max_liste,  0, [-3, -1, 0])
    test(student.max_liste, 42, [10, 42, 7])
    test(student.max_liste,  5, [5, 5, 5])        # tous égaux

    # --- sum_while : même résultat que sum_to mais avec while ---
    test(student.somme_while,  0,  0)
    test(student.somme_while,  1,  1)
    test(student.somme_while, 10,  4)
    test(student.somme_while, 15,  5)
    test(student.somme_while, 55, 10)

    # --- factorial ---
    test(student.factorielle,   1,  0)   # 0! = 1 — erreur fréquente de retourner 0 !
    test(student.factorielle,   1,  1)
    test(student.factorielle,   2,  2)
    test(student.factorielle,   6,  3)
    test(student.factorielle,  24,  4)
    test(student.factorielle, 120,  5)

    # --- fizzbuzz ---
    test(student.fizzbuzz, [], 0)
    test(student.fizzbuzz, [1], 1)
    test(student.fizzbuzz,
        [1, 2, "Fizz", 4, "Buzz"],
        5)
    test(student.fizzbuzz,
        [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"],
        10)
    test(student.fizzbuzz,
        [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
         11, "Fizz", 13, 14, "FizzBuzz"],
        15)

    percentage = (passed / total) * 100

    if percentage == 100:
        level = "Advanced"
    elif percentage >= 60:
        level = "Intermediate"
    else:
        level = "Beginner"

    return passed, total, level


def main():
    files = [f for f in os.listdir() if f.startswith("eval3_") and f.endswith(".py")]

    if not files:
        print("No student files found.")
        return

    with open("results.csv", "w") as f:
        f.write("Name,Score,Total,Level\n")

        for file in files:
            student_name = file.replace("eval3_", "").replace(".py", "")
            student_name = student_name.replace("_", " ").title()

            try:
                student = load_student(file)
                passed, total, level = grade_student(student, student_name)

                print(f"{student_name}: {passed}/{total} ({level})")

                f.write(f"{student_name},{passed},{total},{level}\n")

            except Exception:
                print(f"{student_name}: ERROR")
                f.write(f"{student_name},ERROR,ERROR,ERROR\n")


if __name__ == "__main__":
    main()