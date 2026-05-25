## ÉVALUATION 6 – Dictionnaires
## =============================================
## Comme toujours : remplace chaque `pass` par ton code.
## Ces fonctions doivent return un résultat, pas juste l'afficher.

## =========================================================
## PARTIE 1 : compter
## =========================================================
## Rappel :
##   d = {}                → créer un dictionnaire vide
##   d[cle] = valeur       → ajouter / modifier une valeur
##   if cle in d:          → vérifier si une clé existe


## Retourne un dictionnaire avec le nombre d'occurrences de chaque élément.
## Exemple : compter_elements(["a","b","a"]) → {"a": 2, "b": 1}
def compter_elements(liste):
    pass


## =========================================================
## PARTIE 2 : manipulation
## =========================================================
## Rappel :
##   for cle in dico:             → parcourir les clés
##   for cle, val in dico.items() → clés + valeurs


## Inverse clés et valeurs d'un dictionnaire.
## Exemple : {"a":1,"b":2} → {1:"a",2:"b"}
## ⚠️ On suppose que toutes les valeurs sont différentes.
def inverser_dictionnaire(dico):
    pass


## Retourne la somme des valeurs du dictionnaire.
## Exemple : {"a":1,"b":2,"c":3} → 6
def somme_valeurs(dico):
    pass


## Retourne la clé associée à la plus grande valeur.
## Exemple : {"a":1,"b":5,"c":3} → "b"
## 💡 Astuce : garde une variable pour le max
def max_cle(dico):
    pass


## =========================================================
## PARTIE 3 – Chaînes de caractères + dictionnaires
## =========================================================
## Rappel :
##   phrase.split() → transforme une phrase en liste de mots


## Retourne un dictionnaire avec le nombre d'occurrences de chaque mot.
## Exemple : "hello world hello" → {"hello":2,"world":1}
def compter_mots(phrase):
    pass


## =========================================================
## TESTS (pour aider à vérifier)
## =========================================================

print("PARTIE 1 ──────────────────────────────")
print("compter_elements :", compter_elements(["a","b","a"]))  # {"a":2,"b":1}

print("\nPARTIE 2 ──────────────────────────────")
print("inverser_dico    :", inverser_dictionnaire({"a":1,"b":2})) # {1:"a",2:"b"}
print("somme_valeurs    :", somme_valeurs({"a":1,"b":2,"c":3}))   # 6
print("max_cle          :", max_cle({"a":1,"b":5,"c":3}))         # "b"

print("\nPARTIE 3 ──────────────────────────────")
print("compter_mots     :", compter_mots("hello world hello"))