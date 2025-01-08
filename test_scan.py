#!/usr/bin/python3

import sys

"""
def demander_nom():
    nom = ""

    print("Comment t'appelles-tu ? ")
    nom = input("- ")

    condition = nom == "Nicolas"# or "Marc"
    print(condition)
    if condition:
        print(f"- Bonjour {nom}")
    else:
        print("- Je ne te connais pas")
        sys.exit()
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
"""



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

#nom1 = demander_nom()

#demander_calcul()

calcul_a_faire()
#Nocob
