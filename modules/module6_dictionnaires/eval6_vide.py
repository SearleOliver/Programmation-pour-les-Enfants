## ══════════════════════════════════════════════════════════════
## ÉVALUATION 6 – Dictionnaires
## ══════════════════════════════════════════════════════════════
## Règles :
##   • Remplace chaque `pass` par ton code
##   • Enregistre : eval6_Prenom.py  →  lance grader6.exe
## ══════════════════════════════════════════════════════════════


## ──────────────────────────────────────────────────────────────
## PARTIE 1 – Créer et remplir des dictionnaires
## ──────────────────────────────────────────────────────────────
## Rappel :
##   d = {}                →  dictionnaire vide
##   d[cle] = valeur       →  ajouter / modifier
##   if cle in d:          →  tester si la clé existe

## Retourne le nombre d'occurrences de chaque élément
## Exemple : compter_elements(["a","b","a"]) → {"a":2, "b":1}
def compter_elements(liste):
    pass

## Retourne un dictionnaire construit à partir de deux listes :
## une liste de clés et une liste de valeurs
## Exemple : dico_depuis_listes(["a","b"],  [1, 2]) → {"a":1, "b":2}
## 💡 Les deux listes ont toujours la même longueur
def dico_depuis_listes(cles, valeurs):
    pass


## ──────────────────────────────────────────────────────────────
## PARTIE 2 – Manipuler les dictionnaires
## ──────────────────────────────────────────────────────────────
## Rappel :
##   for cle in dico:              →  parcourt les clés
##   for cle, val in dico.items(): →  clés + valeurs

## Inverse clés et valeurs — on suppose que les valeurs sont uniques
## Exemple : {"a":1, "b":2} → {1:"a", 2:"b"}
def inverser_dictionnaire(dico):
    pass

## Retourne la somme de toutes les valeurs
## Exemple : {"a":1, "b":2, "c":3} → 6
def somme_valeurs(dico):
    pass

## Retourne la clé associée à la plus grande valeur
## Exemple : {"a":1, "b":5, "c":3} → "b"
## 💡 Garde une variable pour le max courant
def max_cle(dico):
    pass

## Retourne un nouveau dictionnaire ne contenant que les entrées
## dont la valeur est >= seuil
## Exemple : filtrer_par_valeur({"a":1,"b":5,"c":3}, 3) → {"b":5,"c":3}
def filtrer_par_valeur(dico, seuil):
    pass


## ──────────────────────────────────────────────────────────────
## PARTIE 3 – Chaînes + dictionnaires
## ──────────────────────────────────────────────────────────────
## Rappel :
##   phrase.split()  →  liste de mots

## Retourne le nombre d'occurrences de chaque mot
## Exemple : "hello world hello" → {"hello":2, "world":1}
def compter_mots(phrase):
    pass

## Retourne le mot qui apparaît le plus souvent dans la phrase
## Exemple : "le chat et le chien" → "le"
## 💡 Réutilise compter_mots() et max_cle() !
def mot_le_plus_frequent(phrase):
    pass


## ──────────────────────────────────────────────────────────────
## Affichage
## ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("── Partie 1 ──────────────────────")
    print("compter_elements(['a','b','a'])    →", compter_elements(["a","b","a"]))         # {"a":2,"b":1}
    print("dico_depuis_listes(['a','b'],[1,2])→", dico_depuis_listes(["a","b"],[1,2]))     # {"a":1,"b":2}

    print("\n── Partie 2 ──────────────────────")
    print("inverser_dictionnaire({'a':1,'b':2})→", inverser_dictionnaire({"a":1,"b":2}))  # {1:"a",2:"b"}
    print("somme_valeurs({'a':1,'b':2,'c':3}) →", somme_valeurs({"a":1,"b":2,"c":3}))    # 6
    print("max_cle({'a':1,'b':5,'c':3})       →", max_cle({"a":1,"b":5,"c":3}))          # b
    print("filtrer_par_valeur({'a':1,'b':5,'c':3},3)→",
          filtrer_par_valeur({"a":1,"b":5,"c":3}, 3))                                     # {"b":5,"c":3}

    print("\n── Partie 3 ──────────────────────")
    print("compter_mots('hello world hello')  →", compter_mots("hello world hello"))      # {"hello":2,"world":1}
    print("mot_le_plus_frequent('le chat et le chien')→",
          mot_le_plus_frequent("le chat et le chien"))                                     # le