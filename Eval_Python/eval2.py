## ÉVALUATION 2 – Géométrie & réutilisation de fonctions
## =========================================================
## Les fonctions mathématiques de base sont déjà fournies ci-dessous.
## Tu n'as pas besoin de les modifier — utilise-les dans tes réponses !

## ── Fonctions fournies ────────────────────────────────────────────
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def square(a):
    return multiply(a, a)

def divide(a, b):
    return a / b
## ──────────────────────────────────────────────────────────────────


## PARTIE 1 – Rectangle
## =====================

## Calcule le périmètre d'un rectangle : 2 × (longueur + largeur)
## Utilise multiply et add.
def rectangle_perimeter(length, width):
    pass

## Calcule l'aire d'un rectangle : longueur × largeur
## Utilise multiply.
def rectangle_area(length, width):
    pass


## PARTIE 2 – Carré
## =================

## Calcule le périmètre d'un carré.
## 💡 Astuce : un carré est un rectangle dont les deux côtés sont égaux...
##    Est-ce qu'on peut réutiliser rectangle_perimeter ?
def square_perimeter(a):
    pass

## Calcule l'aire d'un carré.
## 💡 Astuce : même idée qu'au-dessus !
def square_area(a):
    pass


## PARTIE 3 – Triangle
## ====================

## Calcule le périmètre d'un triangle : somme de ses 3 côtés.
## Utilise add.
def triangle_perimeter(a, b, c):
    pass

## Retourne True si le triangle est équilatéral (les 3 côtés sont égaux),
## False sinon.
def is_equilateral(a, b, c):
    pass


## PARTIE 4 – Comparaison de formes
## ==================================

## Retourne "rectangle" si le rectangle est plus grand, "square" si le carré
## est plus grand, ou "equal" si les deux ont la même aire.
## Paramètres : les côtés du rectangle (l, w) et le côté du carré (a).
## Utilise rectangle_area, square_area.
## 💡 Les retours doivent être exactement : "rectangle", "square", "equal"
def compare_areas(l, w, a):
    pass


## PARTIE 5 – Défi final 🏆
## =========================

## Évalue le polynôme ax² + bx + c pour une valeur de x donnée.
## Exemple : polynomial(1, 2, 3, 4) → 1×16 + 2×4 + 3 = 27
## Utilise square, multiply et add.
def polynomial(a, b, c, x):
    pass


## ── Affichage ─────────────────────────────────────────────────────
print("📐 Périmètre rectangle (4, 3) :", rectangle_perimeter(4, 3))
print("📐 Aire rectangle (4, 3)      :", rectangle_area(4, 3))
print("🟦 Périmètre carré (5)        :", square_perimeter(5))
print("🟦 Aire carré (5)             :", square_area(5))
print("🔺 Périmètre triangle (3,4,5) :", triangle_perimeter(3, 4, 5))
print("🔺 Équilatéral (3,3,3) ?      :", is_equilateral(3, 3, 3))
print("⚖️  Compare (4,3) vs carré(3) :", compare_areas(4, 3, 3))
print("📈 Polynôme 1x²+2x+3 en x=4  :", polynomial(1, 2, 3, 4))