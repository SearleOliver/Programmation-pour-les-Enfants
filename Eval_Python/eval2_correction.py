
## ── Fonctions fournies ────────────────────────────────────────────
def ajouter(a, b):
    return a + b

def soustraire(a, b):
    return a - b

def multiplier(a, b):
    return a * b

def carre(a):
    return multiplier(a, a)

def diviser(a, b):
    return a / b
## ──────────────────────────────────────────────────────────────────

def perimetre_rectangle(length, width):
    return multiplier(2,ajouter(length,width))

def surface_rectangle(length, width):
    return multiplier(length,width)

def perimetre_carre(a):
    return perimetre_rectangle(a,a)

def surface_carre(a):
    return surface_rectangle(a,a)


def perimetre_triangle(a, b, c):
    return ajouter(a,ajouter(b,c))

def equilateral(a, b, c):
    return a == b == c

def comparer_surfaces(l, w, a):
    rect = surface_rectangle(l,w)
    square = surface_carre(a)
    if rect > square:
        return "rectangle"
    elif rect< square:
        return "carré"
    else :
        return "égaux"

def polynomial(a, b, c, x):
    return ajouter(multiplier(a,carre(x)),ajouter(multiplier(b,x),c))
