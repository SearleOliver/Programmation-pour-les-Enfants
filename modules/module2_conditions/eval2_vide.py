## ══════════════════════════════════════════════════════════════
## ÉVALUATION 2 – Conditions
## ══════════════════════════════════════════════════════════════
## Règles :
##   • Remplace chaque `pass` par ton code
##   • Les fonctions doivent RETOURNER (return) un résultat
##   • Enregistre : eval2_Prenom.py  →  lance grader2.exe
## ══════════════════════════════════════════════════════════════


## ──────────────────────────────────────────────────────────────
## PARTIE 1 – Booléens et comparaisons
## ──────────────────────────────────────────────────────────────

## Retourne True si n est strictement positif, False sinon
def est_positif(n):
    pass

## Retourne True si n est pair
def est_pair(n):
    pass

## Retourne True si n est compris entre a et b INCLUS
def dans_intervalle(n, a, b):
    pass

## Retourne True si a est divisible par b
def est_divisible(a, b):
    pass


## ──────────────────────────────────────────────────────────────
## PARTIE 2 – if / else
## ──────────────────────────────────────────────────────────────

## Retourne le plus grand des deux — sans utiliser max()
def maximum(a, b):
    pass

## Retourne le plus petit des deux — sans utiliser min()
def minimum(a, b):
    pass

## Retourne la valeur absolue — sans utiliser abs()
def valeur_absolue(n):
    pass


## ──────────────────────────────────────────────────────────────
## PARTIE 3 – if / elif / else
## ──────────────────────────────────────────────────────────────

## Retourne "positif", "negatif" ou "zero"
def signe(n):
    pass

## Retourne le plus grand des TROIS nombres — sans max()
def max_trois(a, b, c):
    pass

## Retourne la mention selon la note sur 20 :
##   >= 16 → "Très bien"   >= 14 → "Bien"   >= 12 → "Assez bien"
##   >= 10 → "Passable"    sinon → "Insuffisant"
def mention(note):
    pass


## ──────────────────────────────────────────────────────────────
## PARTIE 4 – and / or / not
## ──────────────────────────────────────────────────────────────

## Retourne True si l'année est bissextile.
## Règle : divisible par 4, SAUF si divisible par 100,
##         SAUF si divisible par 400.
## Exemples : 2024 → True   1900 → False   2000 → True
def est_bissextile(annee):
    pass

## Un personnage peut entrer si :
##   (age >= 18 OU vip == True) ET liste_noire == False
def peut_entrer(age, vip, liste_noire):
    pass

## Retourne True si les trois côtés forment un triangle valide.
## Règle : chaque côté doit être < à la somme des deux autres.
def triangle_valide(a, b, c):
    pass

## Retourne "fizz" si divisible par 3,
##          "buzz" si divisible par 5,
##          "fizzbuzz" si divisible par les deux,
##          le nombre lui-même (int) sinon
## ⚠️  Commence par le cas le plus restrictif !
def fizzbuzz_un(n):
    pass


## ──────────────────────────────────────────────────────────────
## Affichage
## ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("── Partie 1 ──────────────────────")
    print("est_positif(5)            →", est_positif(5))              # True
    print("est_positif(-3)           →", est_positif(-3))             # False
    print("est_pair(4)               →", est_pair(4))                 # True
    print("dans_intervalle(5,1,10)   →", dans_intervalle(5, 1, 10))   # True
    print("est_divisible(9,3)        →", est_divisible(9, 3))         # True

    print("\n── Partie 2 ──────────────────────")
    print("maximum(3,7)              →", maximum(3, 7))               # 7
    print("minimum(3,7)              →", minimum(3, 7))               # 3
    print("valeur_absolue(-5)        →", valeur_absolue(-5))          # 5

    print("\n── Partie 3 ──────────────────────")
    print("signe(-3)                 →", signe(-3))                   # negatif
    print("max_trois(1,9,4)          →", max_trois(1, 9, 4))          # 9
    print("mention(15)               →", mention(15))                 # Bien

    print("\n── Partie 4 ──────────────────────")
    print("est_bissextile(2024)      →", est_bissextile(2024))        # True
    print("est_bissextile(1900)      →", est_bissextile(1900))        # False
    print("peut_entrer(20,False,False)→", peut_entrer(20,False,False))# True
    print("peut_entrer(16,True,False) →", peut_entrer(16,True,False)) # True
    print("peut_entrer(20,False,True) →", peut_entrer(20,False,True)) # False
    print("triangle_valide(3,4,5)    →", triangle_valide(3, 4, 5))    # True
    print("triangle_valide(1,2,10)   →", triangle_valide(1, 2, 10))   # False
    print("fizzbuzz_un(9)            →", fizzbuzz_un(9))              # fizz
    print("fizzbuzz_un(15)           →", fizzbuzz_un(15))             # fizzbuzz
    print("fizzbuzz_un(7)            →", fizzbuzz_un(7))              # 7