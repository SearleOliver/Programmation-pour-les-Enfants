ROUGE = "\033[91m"
VERT = "\033[92m"
RESET = "\033[0m"
ROUGE_FOND = "\033[41m"
VERT_FOND = "\033[42m"
RESET = "\033[0m"

def afficher_grille(grille):
    taille = len(grille)
    print("    ", end="")
    for i in range(taille):
        print(f"  {chr(ord('A') + i)}  ", end="")
    print()

    print("   +" + "----+" * taille)

    for i in range(taille):
        print(f"{i:2} |", end="")

        for j in range(taille):
            if grille[i][j] == "0":
                print("  ~ |", end="")
            else:
                print(f" {grille[i][j]}  |", end="")

        print()
        print("   +" + "----+" * taille)




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





