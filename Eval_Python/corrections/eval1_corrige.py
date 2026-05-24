# ÉVALUATION 1 — Bases Python
## =========================================================
## Dans cette évaluation on va tester vos connaissances des opérations de base.
## Vous trouverez dans ce fichier des variables pré definies et des variables à compléter
## Enregistrez votre travail en nommant le fichier comme ceci : eval1_Prenom.py
## Pour évaluer votre travail lancez ./grader.exe

# Voici les variables a manipuler :

# infos article
nom = "Sac de patates"
prix = 5.89
poids = 1.5

# Exercice 1 : donne le prix pour 25 articles.
# Utilise la variable prix et un des operateurs de base.
prixTotalPatates = 25*prix

# Exercice 2 : Si chaque article pèse 1.5kg quel est le prix par kilo ?
# Utilise les variables prix et poids.
prixKgPatates = prix/poids

# Exercice 3 : Donne le prix total pour 3.7kg de patates et 5.8 kg d'onions.
prixKgOnions = 3.99

prixTotal = 3.7*prixKgPatates+5.8*prixKgOnions

# Exercice 4 : Calcule le prix final après une réduction de 15% sur le prixTotal
prixFinal = prixTotal*(1-0.15)

# Exercice 5 : Complète la variable mess age pour qu'elle affiche :
# "Produit : Sac de patates Prix : 5.99 Poids : 1.5kg"
# Attention au espaces
message = "Produit : "+nom+" Prix : "+str(prix)+" Poids : "+str(poids)+"kg"

print(prixTotalPatates)
print(prixKgPatates)
print(prixTotal)
print(prixFinal)
print(message)