## Dans Cette Evaluation on va tester votre capacité à crée des focntions simples.
## Vous trouverez dans ce fichier des fonctions dites squelettes a compléter.
## Pour cela remplissez les corps de fonction.

def add (a,b) :
    return a+b

def substract (a,b) :
    return a-b

def multiply (a,b) :
    return a*b

## Celui ci est un peu spécial, il doit retourner un Boolean donc True si a est pair et False sinon.
## Rappel le symbole % calcule le module
def is_even(a) : 
    return a%2==0

## Pour une fonction carré es qu'il y a une manière ou l'on peut réutiliser nos fonctions préexistantes ?
def square(a):
    return multiply(a,a)

## Ecris une fonction qui compare a et b retournant "a < b" "a > b" ou "a == b".
## Attention les retours doivent être exactement comme ici.
def compare(a,b):
    if a<b:
        return "a < b"
    elif a > b:
        return "a > b"
    else :
        return "a == b"

## Pour la dernière question on va réutiliser nos fonctions pour un calcul plus complexe.
## On va vérifier l'équation (a + b) * (a - b) = a^2 - b^2
## Pour faciliter on va séparer la partie gauche et la partie droite
def difference_squares_left(a,b):
    return multiply(add(a,b),substract(a,b))

def difference_squares_right(a,b):
    return substract(square(a),square(b))