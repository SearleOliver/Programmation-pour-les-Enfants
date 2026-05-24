def ajouter (a,b) :
    return a+b

def soustraire (a,b) :
    return a-b

def multiplier (a,b) :
    return a*b

def pair(a) : 
    return a%2==0

def carre(a):
    return multiplier(a,a)

def comparer(a,b):
    if a<b:
        return "a < b"
    elif a > b:
        return "a > b"
    else :
        return "a == b"

def difference_carres_gauche(a,b):
    return multiplier(ajouter(a,b),soustraire(a,b))

def difference_carres_droite(a,b):
    return soustraire(carre(a),carre(b))