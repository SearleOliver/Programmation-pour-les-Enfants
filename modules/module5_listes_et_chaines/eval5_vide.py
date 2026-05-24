## ÉVALUATION 4 – Listes
## =============================================
## Comme toujours : remplace chaque `pass` par ton code.
## Ces fonctions doivent RETOURNER un résultat, pas juste l'afficher.

## =========================================================
## PARTIE 1 – Boucles for sur des listes
## =========================================================
## Rappel :
##   for element in ma_liste:   → parcourt chaque élément


## Retourne la somme de tous les éléments d'une liste.
## Exemple : somme_list([1, 2, 3, 4]) → 10
def somme_liste(lst):
    pass


## Retourne le nombre de fois que val apparaît dans lst.
## Exemple : nombre_occurrences([1, 2, 2, 3], 2) → 2
def nombre_occurrences(lst, val):
    pass


## Retourne le plus grand élément d'une liste.
## Exemple : max_liste([3, 1, 4, 1, 5, 9]) → 9
## 💡 Astuce : commence par supposer que le premier élément est le max,
##    puis parcours le reste pour vérifier.
## ⚠️  Interdiction d'utiliser la fonction max() de Python !
def max_liste(lst):
    pass


## =========================================================
## PARTIE 2 – Modification de listes
## =========================================================
## Rappel :
##   nouvelle_liste = []
##   liste.append(x)      → ajouter un élément
##   l1 + l2              → concaténer deux listes


## Retourne une nouvelle liste contenant les éléments des deux listes.
## Exemple : fusion_listes([1,2],[3,4]) → [1,2,3,4]
def fusion_listes(l1, l2):
    pass


## Retourne une liste contenant seulement les nombres pairs.
## Exemple : filtrer_pairs([1,2,3,4]) → [2,4]
## 💡 Astuce : utilise % 2 == 0
def filtrer_pairs(liste):
    pass


## =========================================================
## TESTS (pour aider à vérifier)
## =========================================================

print("\nPARTIE 1 ──────────────────────────────")
print("somme_liste([1,2,3,4]) :", somme_liste([1, 2, 3, 4]))        # 10
print("nombre_occurrences   :", nombre_occurrences([1,2,2,3],2)) # 2
print("max_liste            :", max_liste([3, 1, 4, 1, 5, 9]))   # 9

print("\nPARTIE 2 ──────────────────────────────")
print("fusion_listes    :", fusion_listes([1,2],[3,4]))       # [1,2,3,4]
print("filtrer_pairs    :", filtrer_pairs([1,2,3,4]))         # [2,4]

