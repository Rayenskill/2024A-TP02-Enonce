"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 01
Numéro d'équipe :  30
Noms et matricules : Rayen Bouriel (2390589), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici

import csv

csvfile = open("2024A-TP02-Enonce\collection_bibliotheque.csv", newline="")
collection_biblio = csv.reader(csvfile)

bibliotheque = {}

for row in collection_biblio:
    bibliotheque[row[3]] = [row[0], row[1], row[2]]
del bibliotheque["cote_rangement"]
print(f' \n Bibliotheque initiale : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici

csvfile_2 = open("2024A-TP02-Enonce\\nouvelle_collection.csv", newline="")
collection_biblio2 = csv.reader(csvfile_2)

bibliotheque2 = {}

for row in collection_biblio2:
    bibliotheque2[row[3]] = [row[0], row[1], row[2]]
del bibliotheque2["cote_rangement"]

for n in bibliotheque2:
    if n in bibliotheque:
        print(f"Le livre {n} ---- {bibliotheque2[n][0]} par {bibliotheque2[n][1]} ---- est déjà présent dans la bibliothèque")
    else:
        print(f"Le livre {n} ---- {bibliotheque2[n][0]} par {bibliotheque2[n][1]} ---- a été ajouté avec succès")

bibliotheque.update(bibliotheque2)

########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
auteur = "William Shakespeare"
copy_bibliotheque = bibliotheque.copy()

for i in copy_bibliotheque:
    if copy_bibliotheque[i][1] == auteur:
        bibliotheque["W" + i] = bibliotheque.pop(i)


print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






