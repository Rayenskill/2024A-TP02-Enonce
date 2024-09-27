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

collection_default = open("collection_bibliotheque.csv", newline="")
collection_biblio = csv.DictReader(collection_default)

bibliotheque = {}

for row in collection_biblio:
    bibliotheque[row["cote_rangement"]] = {"titre" : row["titre"], "auteur" : row["auteur"], "date_publication" : row["date_publication"]}

print(f' \n Bibliotheque initiale : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici

new_collection = open("nouvelle_collection.csv", newline="")
collection_biblio2 = csv.DictReader(new_collection)

bibliotheque2 = {}

for row in collection_biblio2:
    bibliotheque2[row["cote_rangement"]] = {"titre" : row["titre"], "auteur" : row["auteur"], "date_publication" : row["date_publication"]}

for n in bibliotheque2:
    if n in bibliotheque:
        print(f"Le livre {n} ---- {bibliotheque2[n]["titre"]} par {bibliotheque2[n]["auteur"]} ---- est déjà présent dans la bibliothèque")
    else:
        print(f"Le livre {n} ---- {bibliotheque2[n]["titre"]} par {bibliotheque2[n]["auteur"]} ---- a été ajouté avec succès")

bibliotheque.update(bibliotheque2)

########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
auteur = "William Shakespeare"
copy_bibliotheque = bibliotheque.copy()

for i in copy_bibliotheque:
    if copy_bibliotheque[i]["auteur"] == auteur:
        bibliotheque["W" + i] = bibliotheque.pop(i)


print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')


########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

emprunts = open("emprunts.csv", newline="")
gestion_collection = csv.DictReader(emprunts)

emprunt_default = {"emprunts" : "disponible", "date_emprunt" : "ND"}
livres_emprunts = {}

for livres in bibliotheque:
    bibliotheque[livres].update(emprunt_default)

for lignes in gestion_collection:
        if lignes["cote_rangement"] in bibliotheque:
            livres_emprunts[lignes["cote_rangement"]] = {"emprunts" : "emprenté", "date_emprunt" : lignes["date_emprunt"]}
            bibliotheque[lignes["cote_rangement"]].update(livres_emprunts[lignes["cote_rangement"]])

print(bibliotheque)

########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici

import datetime




