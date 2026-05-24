import importlib.util, os, traceback

def load():
    files = [f for f in os.listdir() if f.startswith("eval1")]
    if len(files) != 1:
        return None
    spec = importlib.util.spec_from_file_location("student", files[0])
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m, files[0]

def test(label, value, expected, results):
    if value == expected:
        return 1
    results.append((label, value, expected))
    return 0

def run(student):
    results = []
    score = 0

    score += test("EX1", student.prixTotalPatates, 25*5.89, results)
    score += test("EX2", student.prixKgPatates, 5.89/1.5, results)
    score += test("EX3", student.prixTotal, 3.7*(5.89/1.5)+5.8*3.99, results)
    score += test("EX4", student.prixFinal, (3.7*(5.89/1.5)+5.8*3.99)*0.85, results)
    score += test("EX5", student.message, "Produit : Sac de patates Prix : 5.89 Poids : 1.5kg", results)

    return score, results

def show(score, results, total):
    print("\n--- RESULTS ---")
    print(f"Score: {score}/{total}")

    level = "Advanced" if score==total else "Intermediate" if score>=3 else "Beginner"
    print("Level:", level)

    print("\nDetails:")
    for r in results:
        print(f"❌ {r[0]} → received {r[1]} expected {r[2]}")

def main():
    try:
        res = load()
        if not res:
            print("No file")
            return
        student, name = res
        score, results = run(student)
        show(score, results, 5)
    except:
        traceback.print_exc()

main()