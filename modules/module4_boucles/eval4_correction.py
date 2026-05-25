## ══════════════════════════════════════════════════════════════
## ÉVALUATION 4 – Boucles
## ══════════════════════════════════════════════════════════════
## Règles :
##   • Remplace chaque `pass` par ton code
##   • Utilise for ou while selon les instructions
##   • Enregistre : eval4_Prenom.py  →  lance grader4.exe
## ══════════════════════════════════════════════════════════════


## ──────────────────────────────────────────────────────────────
## PARTIE 1 – Boucles for
## ──────────────────────────────────────────────────────────────

## Retourne la somme des entiers de 1 à n inclus
## Exemple : somme_n(5) → 15
def somme_n(n):
    pass

## Retourne la somme des entiers PAIRS de 1 à n inclus
## Exemple : somme_pairs(6) → 12  (2+4+6)
def somme_pairs(n):
    pass

## Retourne la somme des chiffres d'un entier positif
## Exemple : somme_chiffres(123) → 6
## 💡 Convertis n en str puis parcours chaque caractère
def somme_chiffres(n):
    pass


## ──────────────────────────────────────────────────────────────
## PARTIE 2 – Boucles while
## ──────────────────────────────────────────────────────────────

## Retourne n! avec une boucle while
## Exemple : factorielle(5) → 120   factorielle(0) → 1
def factorielle(n):
    pass

## Retourne base**exposant SANS utiliser **
## Utilise une boucle while et uniquement la multiplication
## Exemple : puissance_boucle(2, 8) → 256
def puissance_boucle(base, exposant):
    pass

## Compte le nombre d'étapes pour que n atteigne 1 (suite de Syracuse)
## Règle : si n pair → n = n//2 ; sinon → n = 3*n+1
## Exemple : syracuse(6) → 8
def syracuse(n):
    pass


## ──────────────────────────────────────────────────────────────
## PARTIE 3 – Algorithmes classiques 🏆
## ──────────────────────────────────────────────────────────────

## Retourne une liste FizzBuzz de 1 à n (inclus) :
##   "FizzBuzz" si divisible par 3 ET 5
##   "Fizz"     si divisible par 3 seulement
##   "Buzz"     si divisible par 5 seulement
##   le nombre  sinon
## ⚠️  Ordre des cas important !
def fizzbuzz(n):
    pass

## Retourne True si n est premier, False sinon
## 💡 Teste tous les diviseurs de 2 jusqu'à n-1
## Exemples : est_premier(7) → True   est_premier(9) → False
def est_premier(n):
    pass

## Retourne le nombre de multiples de k dans [1, n]
## Exemple : compter_multiples(10, 3) → 3  (3, 6, 9)
def compter_multiples(n, k):
    pass


## ──────────────────────────────────────────────────────────────
## Affichage
## ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("── Partie 1 ──────────────────────")
    print("somme_n(5)              →", somme_n(5))                # 15
    print("somme_pairs(6)          →", somme_pairs(6))            # 12
    print("somme_chiffres(123)     →", somme_chiffres(123))       # 6

    print("\n── Partie 2 ──────────────────────")
    print("factorielle(5)          →", factorielle(5))            # 120
    print("factorielle(0)          →", factorielle(0))            # 1
    print("puissance_boucle(2,8)   →", puissance_boucle(2, 8))   # 256
    print("syracuse(6)             →", syracuse(6))               # 8

    print("\n── Partie 3 ──────────────────────")
    print("fizzbuzz(15)            →", fizzbuzz(15))
    print("est_premier(7)          →", est_premier(7))            # True
    print("est_premier(9)          →", est_premier(9))            # False
    print("compter_multiples(10,3) →", compter_multiples(10, 3)) # 3