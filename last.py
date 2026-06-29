##################################
# Programme python type          #
# auteur : G.Swinnen, Liee, 2003 #
# licence : GPL                  #
##################################

###########################
# importation de fonctions externes :
from math import sqrt

###########################
# definition locale de fonction :
def occurences(car, ch):
    "nombre de caractere <car> n\ dans la chaine <ch>"

    nc = 0
    i = 0
    while i < len(ch):
        if ch[i] == car:
            nc += 1
            i += 1

    return nc



###########################
# corps principal du programme:

print("Veuillez rentrez un nombre")
nbr = input()
print("Veuillez entrez une phrase :")
phr = input()
print("Entez le caractere a compter :")
cch = input()

no = occurences(cch, phr)
rc = sqrt(nbr**3)
print("la racine carree du cube")
print("du nombre fourni vaut")
print(rc)
print("La phrase contient")
print(no, "caracteres", cch)
