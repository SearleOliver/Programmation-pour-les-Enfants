## ÉVALUATION 3 – Les Boucles : for et while
## =============================================
## Comme toujours : remplace chaque `pass` par ton code.
## Ces fonctions doivent RETOURNER un résultat, pas juste l'afficher.

## ── Fonctions utilitaires fournies (eval1) ────────────────────────
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
## ──────────────────────────────────────────────────────────────────


## =========================================================
## PARTIE 1 – Boucles for avec range()
## =========================================================
## Rappel :
##   for i in range(5):      → i vaut 0, 1, 2, 3, 4
##   for i in range(1, 6):   → i vaut 1, 2, 3, 4, 5


## Retourne la somme de tous les entiers de 1 à n (inclus).
## Exemple : sum_to(4) → 1 + 2 + 3 + 4 = 10
def sum_to(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum    
        
        


## Retourne le nombre d'entiers pairs entre 1 et n (inclus).
## Exemple : count_even_up_to(6) → 3  (2, 4, 6)
## 💡 Rappel : tu peux réutiliser l'opérateur % ici !
def count_even_up_to(n):
    sum = 0
    for i in range(1,n+1):
        if i%2==0:
            sum+=i
    return sum

## =========================================================
## PARTIE 2 – Boucles for sur des listes
## =========================================================
## Rappel :
##   for element in ma_liste:   → parcourt chaque élément


## Retourne la somme de tous les éléments d'une liste.
## Exemple : sum_list([1, 2, 3, 4]) → 10
def sum_list(lst):
    sum = 0
    for e in lst:
        sum+=e
    return sum


## Retourne le nombre de fois que val apparaît dans lst.
## Exemple : count_occurrences([1, 2, 2, 3], 2) → 2
def count_occurrences(lst, val):
    count = 0
    for e in lst:
        if e == val:
            count+=1
    return count


## Retourne le plus grand élément d'une liste.
## Exemple : max_list([3, 1, 4, 1, 5, 9]) → 9
## 💡 Astuce : commence par supposer que le premier élément est le max,
##    puis parcours le reste pour vérifier.
## ⚠️  Interdiction d'utiliser la fonction max() de Python !
def max_list(lst):
    max = lst[0]
    for e in lst:
        if e>max:
            max = e
    return max


## =========================================================
## PARTIE 3 – Boucles while
## =========================================================
## Rappel :
##   while condition:   → répète TANT QUE la condition est vraie


## Affiche un compte à rebours de n jusqu'à 0.
## Exemple : countdown(3) affiche :  3  2  1  0
## 💡 Celui-ci est le seul qui affiche au lieu de retourner — c'est normal !
def countdown(n):
    while (n>=0):
        print (n)
        n-=1


## Retourne la somme de tous les entiers de 1 à n en utilisant while.
## Exemple : sum_while(4) → 10
## 💡 C'est le même résultat que sum_to() — mais avec while cette fois !
def sum_while(n):
    sum=0
    while (n>0):
        sum+=n
        n-=1
    return sum


## =========================================================
## PARTIE 4 – Factorielle
## =========================================================
## La factorielle de n, notée n!, c'est :
##   n! = 1 × 2 × 3 × ... × n
## Exemples : 0! = 1    1! = 1    4! = 24    5! = 120
##
## Utilise une boucle (for ou while, à toi de choisir !)
## et la fonction multiply() fournie en haut.
def factorial(n):
    fact=1
    while (n>0):
        fact*=n
        n-=1
    return fact


## =========================================================
## PARTIE 5 – Défi final 🏆 : FizzBuzz
## =========================================================
## FizzBuzz est un classique de la programmation !
## Pour chaque entier de 1 à n (inclus) :
##   - si divisible par 3 ET par 5 → ajoute "FizzBuzz" à la liste
##   - si divisible par 3 seulement → ajoute "Fizz"
##   - si divisible par 5 seulement → ajoute "Buzz"
##   - sinon → ajoute le nombre lui-même (comme entier, pas string)
##
## Retourne la liste complète.
## Exemple : fizzbuzz(5) → [1, 2, "Fizz", 4, "Buzz"]
##
## ⚠️  L'ordre des if/elif compte — commence par le cas le plus restrictif !
def fizzbuzz(n):
    result = []
    for i in range(1, n+1):
        div3 = i % 3 == 0
        div5 = i % 5 == 0
        if div3 and div5:
            result.append("FizzBuzz")
        elif div3:
            result.append("Fizz")
        elif div5:
            result.append("Buzz")
        else:
            result.append(i)
    return result
            
            


## ── Affichage ─────────────────────────────────────────────────────
print("PARTIE 1 ──────────────────────────────")
print("sum_to(4)           :", sum_to(4))          # 10
print("sum_to(10)          :", sum_to(10))          # 55
print("count_even_up_to(6) :", count_even_up_to(6)) # 3

print("\nPARTIE 2 ──────────────────────────────")
print("sum_list([1,2,3,4]) :", sum_list([1, 2, 3, 4]))        # 10
print("count_occurrences   :", count_occurrences([1,2,2,3],2)) # 2
print("max_list            :", max_list([3, 1, 4, 1, 5, 9]))   # 9

print("\nPARTIE 3 ──────────────────────────────")
print("countdown(3)        :", end=" ") ; countdown(3)          # 3 2 1 0
print("sum_while(4)        :", sum_while(4))                    # 10

print("\nPARTIE 4 ──────────────────────────────")
print("factorial(0)        :", factorial(0))   # 1
print("factorial(5)        :", factorial(5))   # 120

print("\nPARTIE 5 ──────────────────────────────")
print("fizzbuzz(15)        :", fizzbuzz(15))