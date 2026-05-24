## ══════════════════════════════════════════════════════════════
## ÉVALUATION 3 – Fonctions
## ══════════════════════════════════════════════════════════════
## Règles :
##   • Remplace chaque `pass` par ton code
##   • Réutilise les fonctions fournies ET tes propres fonctions
##     autant que possible — ne réécris pas ce que tu as déjà !
##   • Enregistre : eval3_Prenom.py  →  lance grader3.exe
## ══════════════════════════════════════════════════════════════

## ── Fonctions fournies (ne pas modifier) ─────────────────────
def ajouter(a, b):      return a + b
def soustraire(a, b):   return a - b
def multiplier(a, b):   return a * b
def diviser(a, b):      return a / b
## ─────────────────────────────────────────────────────────────


## ──────────────────────────────────────────────────────────────
## PARTIE 1 – Fonctions de base
## ──────────────────────────────────────────────────────────────

## Retourne a² — utilise multiplier()
def carre(a):
    pass

## Retourne a³ — utilise multiplier() deux fois
def cube(a):
    pass

## Retourne True si a est pair (utilise % 2)
def est_pair(a):
    pass

## Retourne "a < b", "a > b" ou "a == b" — utilise if/elif/else
def comparer(a, b):
    pass


## ──────────────────────────────────────────────────────────────
## PARTIE 2 – Géométrie (réutilise les fonctions ci-dessus)
## ──────────────────────────────────────────────────────────────

## Périmètre rectangle : 2 × (longueur + largeur)
def perimetre_rectangle(longueur, largeur):
    pass

## Surface rectangle : longueur × largeur
def surface_rectangle(longueur, largeur):
    pass

## Périmètre carré — réutilise perimetre_rectangle()
def perimetre_carre(a):
    pass

## Surface carré — réutilise surface_rectangle()
def surface_carre(a):
    pass

## Périmètre triangle — somme des 3 côtés
def perimetre_triangle(a, b, c):
    pass

## True si triangle équilatéral (3 côtés égaux)
def equilateral(a, b, c):
    pass

## "rectangle", "carré" ou "égaux" selon laquelle des deux
## surfaces est plus grande (rectangle l×w vs carré a×a)
def comparer_surfaces(l, w, a):
    pass


## ──────────────────────────────────────────────────────────────
## PARTIE 3 – Fonctions composées 🏆
## ──────────────────────────────────────────────────────────────

## IMC = poids / taille²  — utilise diviser() et carre()
def imc(poids, taille):
    pass

## Évalue ax² + bx + c pour x donné
## Exemple : polynome(1, 2, 3, 4) → 1×16 + 2×4 + 3 = 27
## Utilise carre(), multiplier(), ajouter()
def polynome(a, b, c, x):
    pass

## Identité remarquable : (a+b)(a-b) = a²-b²
## Calcule les deux membres et retourne True s'ils sont égaux.
## Utilise tes fonctions — ne calcule pas directement !
def verifier_identite(a, b):
    gauche = None  # TODO : (a+b)(a-b)  via multiplier, ajouter, soustraire
    droite = None  # TODO : a² - b²     via carre, soustraire
    pass           # TODO : retourne gauche == droite


## ──────────────────────────────────────────────────────────────
## Affichage
## ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("── Partie 1 ──────────────────────")
    print("carre(5)                  →", carre(5))                   # 25
    print("cube(3)                   →", cube(3))                    # 27
    print("est_pair(4)               →", est_pair(4))                # True
    print("est_pair(7)               →", est_pair(7))                # False
    print("comparer(3,7)             →", comparer(3, 7))             # a < b
    print("comparer(5,5)             →", comparer(5, 5))             # a == b

    print("\n── Partie 2 ──────────────────────")
    print("perimetre_rectangle(4,3)  →", perimetre_rectangle(4, 3))  # 14
    print("surface_rectangle(4,3)   →", surface_rectangle(4, 3))    # 12
    print("perimetre_carre(5)        →", perimetre_carre(5))         # 20
    print("surface_carre(5)          →", surface_carre(5))           # 25
    print("perimetre_triangle(3,4,5) →", perimetre_triangle(3,4,5)) # 12
    print("equilateral(3,3,3)        →", equilateral(3,3,3))        # True
    print("comparer_surfaces(4,3,3)  →", comparer_surfaces(4,3,3))  # rectangle

    print("\n── Partie 3 ──────────────────────")
    print("imc(70,1.75)              →", imc(70, 1.75))             # ~22.86
    print("polynome(1,2,3,4)         →", polynome(1, 2, 3, 4))      # 27
    print("verifier_identite(5,3)    →", verifier_identite(5, 3))   # True
    print("verifier_identite(7,2)    →", verifier_identite(7, 2))   # True