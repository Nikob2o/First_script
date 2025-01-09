#!/usr/bin/python3

import sys


def demander_nom():
    import sys  # Assurez-vous d'importer `sys` si ce n'est pas déjà fait
    print("Comment t'appelles-tu ?")
    nom = input("- ").strip()  # Supprime les espaces avant/après l'entrée de l'utilisateur

    # Correction de la condition
    condition = nom == "Nicolas" or nom == "Marc"

    print(condition)  # Affiche True ou False
    if condition:
        print(f"- Bonjour {nom}")
    else:
        print("- Je ne te connais pas")
        sys.exit()  # Quitte le programme si le nom ne correspond pas
    return nom


#####################################################################



def demander_calcul():
    rep = ""

    print("- Veux-tu faire un calcul ?")
    rep = input("- ")
    condition = rep ==  "oui"
    print(condition)
    if condition:
        print("- Quel est le calcul que tu voudrais faire ? ")
    else:
        print("Bonne journé")
        sys.exit()

######################################################################


def calcul_a_faire():

    somme = 0
    while somme == 0:
        somme_str = input("- Je voudrait calculer : ")
        print(somme)
        somme = float(somme_str)
        print(somme)
        try:
            somme = float(somme)
        except:
            print("Un calcul c'est avec des chiffres et non des lettres ")

    else:
        print(f"- Le resultat est : {somme} ")

########################################################################

demander_nom()
demander_calcul()
calcul_a_faire()
#Nocob
