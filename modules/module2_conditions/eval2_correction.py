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
    return n>0

## Retourne True si n est pair
def est_pair(n):
    return n%2==0

## Retourne True si n est compris entre a et b INCLUS
def dans_intervalle(n, a, b):
    return a<=n and n<=b

## Retourne True si a est divisible par b
def est_divisible(a, b):
    return a%b==0


## ──────────────────────────────────────────────────────────────
## PARTIE 2 – if / else
## ──────────────────────────────────────────────────────────────

## Retourne le plus grand des deux — sans utiliser max()
def maximum(a, b):
    if a<b :
        return b
    return a

## Retourne le plus petit des deux — sans utiliser min()
def minimum(a, b):
    if a<b :
        return a
    return b

## Retourne la valeur absolue — sans utiliser abs()
def valeur_absolue(n):
    if n<0:
        return -n
    return n


## ──────────────────────────────────────────────────────────────
## PARTIE 3 – if / elif / else
## ──────────────────────────────────────────────────────────────

## Retourne "positif", "negatif" ou "zero"
def signe(n):
    if n>0 :
        return "positif"
    elif n<0 :
        return "negatif"
    return "zero"

## Retourne le plus grand des TROIS nombres — sans max()
def max_trois(a, b, c):
    if a>b :
        if a > c:
            return a
        else :
            return c
    elif c > b :
        return c
    return b

## Retourne la mention selon la note sur 20 :
##   >= 16 → "Très bien"   >= 14 → "Bien"   >= 12 → "Assez bien"
##   >= 10 → "Passable"    sinon → "Insuffisant"
def mention(note):
    if note>=16 :
        return "Très bien"
    if note>=14:
        return "Bien"
    if note>=12:
        return "Assez bien"
    if note>=10:
        return "Passable"
    return "Insuffisant"


## ──────────────────────────────────────────────────────────────
## PARTIE 4 – and / or / not
## ──────────────────────────────────────────────────────────────

## Retourne True si l'année est bissextile.
## Règle : divisible par 4, SAUF si divisible par 100,
##         SAUF si divisible par 400.
## Exemples : 2024 → True   1900 → False   2000 → True
def est_bissextile(annee):
    return annee%4==0 and (annee%100!=0 or annee%400==0)

## Un personnage peut entrer si :
##   (age >= 18 OU vip == True) ET liste_noire == False
def peut_entrer(age, vip, liste_noire):
    return (age>=18 or vip) and not liste_noire

## Retourne True si les trois côtés forment un triangle valide.
## Règle : chaque côté doit être < à la somme des deux autres.
def triangle_valide(a, b, c):
    return a<b+c and b<a+c and c<b+a

## Retourne "fizz" si divisible par 3,
##          "buzz" si divisible par 5,
##          "fizzbuzz" si divisible par les deux,
##          le nombre lui-même (int) sinon
## ⚠️  Commence par le cas le plus restrictif !
def fizzbuzz_un(n):
    if n%3==0 and n%5==0:
        return "fizzbuzz"
    if n%3==0:
        return "fizz"
    if n%5==0:
        return "buzz"
    return n


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