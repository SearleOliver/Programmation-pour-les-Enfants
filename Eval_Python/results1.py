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

    # --- ajouter ---
    test(student.ajouter,  3,   1,   2)
    test(student.ajouter,  0,  -1,   1)
    test(student.ajouter, 15,  10,   5)
    test(student.ajouter,  0,   0,   0)
    test(student.ajouter, -5,  -2,  -3)

    # --- soustraire ---
    test(student.soustraire,  1,   3,  2)
    test(student.soustraire,  6,   3, -3)
    test(student.soustraire, -6,  -3,  3)
    test(student.soustraire,  0,   5,  5)
    test(student.soustraire, 42,  42,  0)

    # --- multiplier ---
    test(student.multiplier, 18,   3,   6)
    test(student.multiplier, 18,  -3,  -6)
    test(student.multiplier,-18,   3,  -6)
    test(student.multiplier,  0,   5,   0)
    test(student.multiplier,  7,   1,   7)

    # --- pair ---
    test(student.pair, True,   2)
    test(student.pair, False,  3)
    test(student.pair, True,   0)
    test(student.pair, False,  1)
    test(student.pair, True,  -4)
    test(student.pair, False, -7)

    # --- carre ---
    test(student.carre,  0,  0)
    test(student.carre,  1,  1)
    test(student.carre,  9,  3)
    test(student.carre, 25,  5)
    test(student.carre,  9, -3)

    # --- comparer ---
    test(student.comparer, "a > b",  5,  3)
    test(student.comparer, "a < b",  2,  7)
    test(student.comparer, "a == b", 4,  4)
    test(student.comparer, "a < b", -1,  0)
    test(student.comparer, "a > b",  0, -1)
    test(student.comparer, "a == b", 0,  0)

    percentage = (passed / total) * 100

    if percentage == 100:
        level = "Advanced"
    elif percentage >= 60:
        level = "Intermediate"
    else:
        level = "Beginner"

    return passed, total, level


def main():
    files = [f for f in os.listdir() if f.startswith("eval1_") and f.endswith(".py")]

    if not files:
        print("No student files found.")
        return

    with open("results.csv", "w") as f:
        f.write("Name,Score,Total,Level\n")

        for file in files:
            student_name = file.replace("eval1_", "").replace(".py", "")
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