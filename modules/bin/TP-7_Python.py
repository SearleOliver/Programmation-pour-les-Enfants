import simplegui
import random

# Dimensions de la fenêtre


# Constantes


# Skins : couleurs et formes aléatoires


#Formes des objets qui tombent


# Variables globales
panier_x = LARGEUR // 2
objets = []  # chaque objet = [x, y, vitesse, delai, skin, forme]
score = 0
messages = []

# Générer les objets à faire tomber
def generer_objets():
    global objets
    objets = []
    for i in range(random.randint(NB_OBJETS_MIN, NB_OBJETS_MAX)):
        x = random.randint(40, LARGEUR - 40)
        skin = random.choice(SKINS)
        forme = #à toi
        delai = random.randint(0, DELAI_MAX)
        objets.append([x, 0, VITESSE_INIT, delai, skin, forme])


# Dessiner un objet (bonbon) selon sa forme
def dessiner_objet(canvas, x, y, skin, forme):
   contour, remplissage, eclat = skin
   taille = 20

   if forme == "cercle":

   elif forme == "carré":
        canvas.draw_polygon(
            [[x - taille, y - taille],
             [x + taille, y - taille],
             [x + taille, y + taille],
             [x - taille, y + taille]],
            3, contour, remplissage)

   elif forme == "triangle":
        canvas.draw_polygon(
            [[x, y - taille],
             [x - taille, y + taille],
             [x + taille, y + taille]],
            3, contour, remplissage)

# Fonction principale de dessin
def dessiner(canvas):
    global objets, score, messages

    objets_restants = []

    for obj in objets:
        x, y, v, delai, skin, forme = obj

        if delai > 0:
            obj[3] -= 1
            objets_restants.append(obj)
            continue

        dessiner_objet(canvas, x, y, skin, forme)

        obj[1] += obj[2]
        obj[2] *= FROTTEMENT

        if y >= HAUTEUR - 40:
            if panier_x <= x <= panier_x + LARGEUR_PANIER:
                score += 1
            else:
                messages.append(["Louper !", (250, 200), 30])
        else:
            objets_restants.append(obj)

    objets = objets_restants

    # Dessiner le panier en coupelle + effet brillant
    # Base verte fluo
    canvas.draw_polygon(
        [[panier_x, HAUTEUR - 30],
         [panier_x + LARGEUR_PANIER, HAUTEUR - 30],
         [panier_x + LARGEUR_PANIER - 10, HAUTEUR - 10],
         [panier_x + 10, HAUTEUR - 10]],
        1, "Black", "#00FF66")

    # Dessus plus clair pour effet de dégradé
    canvas.draw_polygon(
        [[panier_x + 10, HAUTEUR - 30],
         [panier_x + LARGEUR_PANIER - 10, HAUTEUR - 30],
         [panier_x + LARGEUR_PANIER - 20, HAUTEUR - 20],
         [panier_x + 20, HAUTEUR - 20]],
        1, "#33FF99", "#33FF99")

    # Affichage des messages temporaires
    nouveaux_messages = []
    for texte, pos, duree in messages:
        canvas.draw_text(texte, pos, 40, "Red")
        if duree > 0:
            nouveaux_messages.append([texte, pos, duree - 1])
    messages[:] = nouveaux_messages

    # Affichage du score
    canvas.draw_text("Score : " + str(score), (20, 40), 30, "#fff")

    # Relancer si tous les objets sont tombés
    if len(objets) == 0:
        generer_objets()



# Déplacement du panier avec les flèches
def touche(t):
  global panier_x


# Créer la fenêtre de jeu


# Démarrer le jeu
