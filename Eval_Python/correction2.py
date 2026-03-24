## ÉVALUATION 2 – Géométrie & réutilisation de fonctions
## =========================================================
## Les fonctions mathématiques de base sont déjà fournies ci-dessous.
## Tu n'as pas besoin de les modifier — utilise-les dans tes réponses !

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


## PARTIE 1 – Rectangle
## =====================

## Calcule le périmètre d'un rectangle : 2 × (longueur + largeur)
## Utilise multiply et add.
def perimetre_rectangle(length, width):
    return multiplier(2,ajouter(length,width))

## Calcule l'aire d'un rectangle : longueur × largeur
## Utilise multiply.
def surface_rectangle(length, width):
    return multiplier(length,width)


## PARTIE 2 – Carré
## =================

## Calcule le périmètre d'un carré.
## 💡 Astuce : un carré est un rectangle dont les deux côtés sont égaux...
##    Est-ce qu'on peut réutiliser rectangle_perimeter ?
def perimetre_carre(a):
    return perimetre_rectangle(a,a)

## Calcule l'aire d'un carré.
## 💡 Astuce : même idée qu'au-dessus !
def surface_carre(a):
    return surface_rectangle(a,a)


## PARTIE 3 – Triangle
## ====================

## Calcule le périmètre d'un triangle : somme de ses 3 côtés.
## Utilise add.
def perimetre_triangle(a, b, c):
    return ajouter(a,ajouter(b,c))

## Retourne True si le triangle est équilatéral (les 3 côtés sont égaux),
## False sinon.
def equilateral(a, b, c):
    return a == b == c


## PARTIE 4 – Comparaison de formes
## ==================================

## Retourne "rectangle" si le rectangle est plus grand, "square" si le carré
## est plus grand, ou "equal" si les deux ont la même aire.
## Paramètres : les côtés du rectangle (l, w) et le côté du carré (a).
## Utilise rectangle_area, square_area.
## 💡 Les retours doivent être exactement : "rectangle", "carré", "egal"
def comparer_surfaces(l, w, a):
    rect = surface_rectangle(l,w)
    square = surface_carre(a)
    if rect > square:
        return "rectangle"
    elif rect< square:
        return "carré"
    else :
        return "égal"


## PARTIE 5 – Défi final 🏆
## =========================

## Évalue le polynôme ax² + bx + c pour une valeur de x donnée.
## Exemple : polynomial(1, 2, 3, 4) → 1×16 + 2×4 + 3 = 27
## Utilise square, multiply et add.
def polynomial(a, b, c, x):
    return ajouter(multiplier(a,carre(x)),ajouter(multiplier(b,x),c))


## ── Affichage ─────────────────────────────────────────────────────
print("📐 Périmètre rectangle (4, 3) :", perimetre_rectangle(4, 3))
print("📐 Aire rectangle (4, 3)      :", surface_rectangle(4, 3))
print("🟦 Périmètre carré (5)        :", perimetre_carre(5))
print("🟦 Aire carré (5)             :", surface_carre(5))
print("🔺 Périmètre triangle (3,4,5) :", perimetre_triangle(3, 4, 5))
print("🔺 Équilatéral (3,3,3) ?      :", equilateral(3, 3, 3))
print("⚖️  Compare (4,3) vs carré(3) :", comparer_surfaces(4, 3, 3))
print("📈 Polynôme 1x²+2x+3 en x=4  :", polynomial(1, 2, 3, 4))