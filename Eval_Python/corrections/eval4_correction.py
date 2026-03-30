## ÉVALUATION 4 – Listes et Dictionnaires
## =============================================
## Comme toujours : remplace chaque `pass` par ton code.
## Ces fonctions doivent RETOURNER un résultat, pas juste l'afficher.


## =========================================================
## PARTIE 1 – Dictionnaires : compter
## =========================================================
## Rappel :
##   d = {}                → créer un dictionnaire vide
##   d[cle] = valeur       → ajouter / modifier une valeur
##   if cle in d:          → vérifier si une clé existe


## Retourne un dictionnaire avec le nombre d'occurrences de chaque élément.
## Exemple : compter_elements(["a","b","a"]) → {"a": 2, "b": 1}
def compter_elements(liste):
    num = {}
    for elem in liste :
        if elem in num :
            num[elem]+=1
        else :
            num[elem]=1
    return num


## =========================================================
## PARTIE 2 – Listes
## =========================================================
## Rappel :
##   nouvelle_liste = []
##   liste.append(x)      → ajouter un élément
##   l1 + l2              → concaténer deux listes


## Retourne une nouvelle liste contenant les éléments des deux listes.
## Exemple : fusion_listes([1,2],[3,4]) → [1,2,3,4]
def fusion_listes(l1, l2):
    return l1+l2


## Retourne une liste contenant seulement les nombres pairs.
## Exemple : filtrer_pairs([1,2,3,4]) → [2,4]
## 💡 Astuce : utilise % 2 == 0
def filtrer_pairs(liste):
    pairs = []
    for elem in liste :
        if elem%2==0 :
            pairs.append(elem)
    return pairs


## =========================================================
## PARTIE 3 – Dictionnaires : manipulation
## =========================================================
## Rappel :
##   for cle in dico:             → parcourir les clés
##   for cle, val in dico.items() → clés + valeurs


## Inverse clés et valeurs d'un dictionnaire.
## Exemple : {"a":1,"b":2} → {1:"a",2:"b"}
## ⚠️ On suppose que toutes les valeurs sont différentes.
def inverser_dictionnaire(dico):
    rev = {}
    for elem in dico :
        rev[dico[elem]]=elem
    return rev


## Retourne la somme des valeurs du dictionnaire.
## Exemple : {"a":1,"b":2,"c":3} → 6
def somme_valeurs(dico):
    somme=0
    for elem in dico :
        somme+=dico[elem]
    return somme


## Retourne la clé associée à la plus grande valeur.
## Exemple : {"a":1,"b":5,"c":3} → "b"
## 💡 Astuce : garde une variable pour le max
def max_cle(dico):
    max_key = None
    max_val = None

    for key, val in dico.items():
        if max_val is None or val > max_val:
            max_val = val
            max_key = key

    return max_key
            


## =========================================================
## PARTIE 4 – Chaînes de caractères + dictionnaires
## =========================================================
## Rappel :
##   phrase.split() → transforme une phrase en liste de mots


## Retourne un dictionnaire avec le nombre d'occurrences de chaque mot.
## Exemple : "hello world hello" → {"hello":2,"world":1}
def compter_mots(phrase):
    liste =phrase.split()
    num = {}
    for mot in liste :
        if mot in num :
            num[mot]+=1
        else :
            num[mot]=1
    return num
        

## =========================================================
## TESTS (pour aider à vérifier)
## =========================================================

print("PARTIE 1 ──────────────────────────────")
print("compter_elements :", compter_elements(["a","b","a"]))  # {"a":2,"b":1}

print("\nPARTIE 2 ──────────────────────────────")
print("fusion_listes    :", fusion_listes([1,2],[3,4]))       # [1,2,3,4]
print("filtrer_pairs    :", filtrer_pairs([1,2,3,4]))         # [2,4]

print("\nPARTIE 3 ──────────────────────────────")
print("inverser_dico    :", inverser_dictionnaire({"a":1,"b":2})) # {1:"a",2:"b"}
print("somme_valeurs    :", somme_valeurs({"a":1,"b":2,"c":3}))   # 6
print("max_cle          :", max_cle({"a":1,"b":5,"c":3}))         # "b"

print("\nPARTIE 4 ──────────────────────────────")
print("compter_mots     :", compter_mots("hello world hello"))