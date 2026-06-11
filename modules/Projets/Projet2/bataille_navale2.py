from IPython.display import HTML, display
import random


style = """
<style>
body {
    font-family: Arial;
}
.grille {
    display: inline-block;
    margin: 20px;
}
.ligne {
    display: flex;
}
.case {
    width: 40px;
    height: 40px;
    border: 1px solid black;
}
.indice {
    width: 40px;
    height: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
}
.eau {
    background-color: blue;
}
.bateau {
    background-color: gray;
}
.touche {
    background-color: red;
}
.rate {
    background-color: white;
}
</style>
"""


debut = '<div class="grille">'
fin = '</div>'
eau = '<div class="case eau"></div>'
bateau = '<div class="case bateau"></div>'
touche = '<div class="case touche"></div>'
rate = '<div class="case rate"></div>'
debut_ligne = '<div class="ligne">'
fin_ligne = '</div>'


def creer_grille(taille):
    grille = []
    for i in range(taille):
        ligne = []
        for j in range(taille):


            """
            """
            ligne.append("0")  

            
        grille.append(ligne)
        """
        """

    return grille

bateaux = {
    "Porte-avions": 5,
    "Croiseur": 4,
    "Contre-torpilleur": 3,
    "Sous-marin": 3,
    "Torpilleur": 2
}

def verifier_placement(grille, ligne, colonne, taille, orientation):
   
    n = len(grille)

    if orientation == "H":
        # Sortie de grille
        """
        """
        if colonne + taille > n:
            return False

        # Collision
        """
        """
        for i in range(taille):
            if grille[ligne][colonne + i] != "0":
                return False

    elif orientation == "V":
        # Sortie de grille
        if ligne + taille > n:
            return False

        # Collision
        for i in range(taille):
            if grille[ligne + i][colonne] != "0":
                return False
    
    return True  
    
    

def placer_bateau(grille, ligne, colonne, taille, orientation):
    if verifier_placement(grille, ligne, colonne, taille, orientation) :
        if orientation == "H":
            for i in range(taille):
                grille[ligne][colonne + i] = "X"
            return True
        else:  
            for i in range(taille):
                grille[ligne + i][colonne] ="X"
            return True
    return False




#grille = creer_grille(10)
#placement_joueur(grille)


def tire(grille1,grille2):
    ligne = int(input("Ligne (0-9) : "))
    colonne_lettre = input("Colonne (A-J) : ").upper()
    colonne = ord(colonne_lettre) - ord('A')
    if grille1[ligne][colonne] == "0":
        grille1[ligne][colonne] = "O"
        grille2[ligne][colonne] = "O"
        print("Tir dans l'eau !")
        return True 
    else:
        grille1[ligne][colonne] = "X" 
        grille2[ligne][colonne] = "X" 
        print("Touché !")
        return False

#grille2 = creer_grille(10)
#tire(grille,grille2)
#afficher_grille(grille2)
#tire(grille,grille2)
#afficher_grille(grille2)

    