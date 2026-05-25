## ══════════════════════════════════════════════════════════════
## ÉVALUATION 5 – Listes & Chaînes de caractères
## ══════════════════════════════════════════════════════════════
## Règles :
##   • Remplace chaque `pass` par ton code
##   • Enregistre : eval5_Prenom.py  →  lance grader5.exe
## ══════════════════════════════════════════════════════════════


## ──────────────────────────────────────────────────────────────
## PARTIE 1 – Opérations sur les listes
## ──────────────────────────────────────────────────────────────
## Rappel :
##   for elem in liste  →  parcourt chaque élément
##   liste.append(x)    →  ajoute x à la fin
##   l1 + l2            →  concatène deux listes

## Retourne la somme de tous les éléments
## Exemple : somme_liste([1,2,3,4]) → 10
def somme_liste(lst):
    pass

## Retourne le plus petit élément — sans utiliser min()
## Exemple : min_liste([3,1,4,1,5]) → 1
def min_liste(lst):
    pass

## Retourne le plus grand élément — sans utiliser max()
## Exemple : max_liste([3,1,4,1,5,9]) → 9
def max_liste(lst):
    pass

## Retourne la moyenne des éléments
## Exemple : moyenne_liste([2,4,6]) → 4.0
def moyenne_liste(lst):
    pass

## Retourne le nombre de fois que val apparaît dans lst
## Exemple : nombre_occurrences([1,2,2,3], 2) → 2
def nombre_occurrences(lst, val):
    pass

## Retourne une nouvelle liste avec seulement les nombres pairs
## Exemple : filtrer_pairs([1,2,3,4,5,6]) → [2,4,6]
def filtrer_pairs(lst):
    pass

## Retourne la liste dans l'ordre inverse — sans utiliser reverse() ni [::-1]
## Exemple : inverser_liste([1,2,3]) → [3,2,1]
def inverser_liste(lst):
    pass

## Retourne une nouvelle liste = l1 + l2
## Exemple : fusion_listes([1,2],[3,4]) → [1,2,3,4]
def fusion_listes(l1, l2):
    pass


## ──────────────────────────────────────────────────────────────
## PARTIE 2 – Opérations sur les chaînes
## ──────────────────────────────────────────────────────────────
## Rappel :
##   for c in chaine    →  parcourt chaque caractère
##   chaine[i]          →  caractère à l'index i
##   len(chaine)        →  longueur
##   chaine.lower()     →  minuscules

## Retourne le nombre de voyelles (a e i o u y, majuscules ou minuscules)
## Exemple : compter_voyelles("Bonjour") → 3
def compter_voyelles(s):
    pass

## Retourne True si la chaîne est un palindrome (se lit pareil à l'endroit et à l'envers)
## Ignore la casse : "Radar" → True
## Exemple : est_palindrome("radar") → True   est_palindrome("hello") → False
def est_palindrome(s):
    pass

## Retourne la chaîne avec les mots dans l'ordre inverse
## Exemple : inverser_mots("bonjour le monde") → "monde le bonjour"
## 💡 Utilise .split() et une boucle
def inverser_mots(phrase):
    pass

## Retourne True si la chaîne contient uniquement des chiffres
## Exemple : est_numerique("1234") → True   est_numerique("12a4") → False
## 💡 Parcours chaque caractère et vérifie "0" <= c <= "9"
def est_numerique(s):
    pass


## ──────────────────────────────────────────────────────────────
## Affichage
## ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("── Partie 1 – Listes ─────────────")
    print("somme_liste([1,2,3,4])      →", somme_liste([1,2,3,4]))          # 10
    print("min_liste([3,1,4,1,5])      →", min_liste([3,1,4,1,5]))          # 1
    print("max_liste([3,1,4,1,5,9])    →", max_liste([3,1,4,1,5,9]))        # 9
    print("moyenne_liste([2,4,6])      →", moyenne_liste([2,4,6]))          # 4.0
    print("nombre_occurrences([1,2,2,3],2)→", nombre_occurrences([1,2,2,3],2)) # 2
    print("filtrer_pairs([1,2,3,4,5,6])→", filtrer_pairs([1,2,3,4,5,6]))   # [2,4,6]
    print("inverser_liste([1,2,3])     →", inverser_liste([1,2,3]))         # [3,2,1]
    print("fusion_listes([1,2],[3,4])  →", fusion_listes([1,2],[3,4]))      # [1,2,3,4]

    print("\n── Partie 2 – Chaînes ────────────")
    print("compter_voyelles('Bonjour') →", compter_voyelles("Bonjour"))     # 3
    print("est_palindrome('radar')     →", est_palindrome("radar"))         # True
    print("est_palindrome('Radar')     →", est_palindrome("Radar"))         # True
    print("est_palindrome('hello')     →", est_palindrome("hello"))         # False
    print("inverser_mots('a b c')      →", inverser_mots("a b c"))          # c b a
    print("est_numerique('1234')       →", est_numerique("1234"))           # True
    print("est_numerique('12a4')       →", est_numerique("12a4"))           # False