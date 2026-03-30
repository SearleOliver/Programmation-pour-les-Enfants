## ÉVALUATION 1 – Fonctions simples
## =========================================================
## Dans cette évaluation on va tester votre capacité à créer des fonctions simples.
## Vous trouverez dans ce fichier des fonctions dites squelettes à compléter.
## Pour évaluer votre travail lancez ./grader.exe
## Pour cela remplissez les corps de fonction.

## PARTIE 1 – Fonctions de calcul
## ==============================

def ajouter(a, b):
    pass

def soustraire(a, b):
    pass

def multiplier(a, b):
    pass

## Celui-ci est un peu spécial : il doit retourner un booléen,
## donc True si a est pair et False sinon.
## Rappel : le symbole % calcule le modulo.
def pair(a):
    pass

## Écris une fonction qui compare a et b en retournant
## "a < b", "a > b" ou "a == b".
## Attention : les retours doivent être exactement comme indiqué ici. Attention pas de print !
def comparer(a, b):
    pass



## PARTIE 2 – Réutilisation de fonction
## ====================================

## Pour une fonction carré, est-ce qu'il y a une manière
## de réutiliser nos fonctions préexistantes ?
def carre(a):
    pass

## Pour la dernière question on va réutiliser nos fonctions
## pour vérifier l'identité remarquable :
##
##   (a + b) × (a - b) = a² - b²
##
## On sépare le membre gauche et le membre droit :

def difference_carres_gauche(a, b):
    ## Calcule (a + b) × (a - b)
    ## Utilise add, substract et multiply
    pass

def difference_carres_droite(a, b):
    ## Calcule a² - b²
    ## Utilise square et substract
    pass

## Affichage du résultat :
left  = difference_carres_gauche(4, 7)
right = difference_carres_droite(4, 7)
print(comparer(left, right))