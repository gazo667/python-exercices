from statistics import mean
from random import shuffle
# chapitre sur les lites et sets en python




# fonction add et update pour ajouter des éléments dans un set
fruits_tropical = {"Pomme", "Banane", "Orange"}
fruits_tropical.update(["Papaye", "Dattes"])
fruits_tropical.add("Mangue")

print(fruits_tropical)

# supprimer des  éléments dans un set avec pop et discard (si l'élément est présent ) et remove
légumes = {"Aubergine", "Poivre", "Comcombre"}
légumes.discard("Aubergine")
légumes.remove("Comcombre")

print(légumes)
# Pour pop
liste_des_garçons = ["Aboubacar", "Ibrahima", "Moussa","Fatoumata"]
item = liste_des_garçons.pop()
print(item)
print(liste_des_garçons)

#pour clear poir vider totalement une liste ou un set

listes_des_invités = {"Peter thiel", "Marc andersen", "Marc Zuckerberg", "Palmer luckey"}
listes_des_invités.clear ()
print(listes_des_invités)
#apprentissage pour liste
#creer une liste pour stocker les pseudos pour tester les foctions des listes et simuler un jeu en ligne

#les pseudos sont gazo , gims , dadju, freeze, Sdm et werenoi
joueurs_en_ligne = ["gazo", "freeze", "gims", "dadju","sdm", "werenoi"]

#pour supprimer des elements dans une liste on peut utiliser del et pop, mais il y a aussi remove pour supprimer par le nom
del joueurs_en_ligne[3] 
joueurs_en_ligne.pop(3)






# modifier gazo en gazo des gazs
joueurs_en_ligne[0] = "gazo des gaz"
joueurs_en_ligne.extend(["cental cee", "NBA young boy"])


# exemple : Jouer a la maitresse
notes = [15, 13, 9,  7, 18, 11,]
print(notes)
shuffle(notes)
print(notes)
resultat = mean(notes)
print(f"la moyenne de l'élève est {resultat}")
# la fonction statistics est utile pour cacul les statistiqus, aussi la fonction mean pour la moyenne en utilisant statistique avec from et import
# en python il ya beaucoup de modules pour des taches spécifique
# radom est un module qui contient la fonction shufle pour melanger les elements d'une liste comme celui d'un set 
# la fonction split permet de utiliser l'element d'une chaine de caractere par un signe comme un tiret et peut etre utile quand on utilise input(la fonction pour lire) avec des chaines de caractere

text = input("Entrer une chaine (email-pseudo-mot_de_pass)").split("-")
print(text)

print("salut {}, ton email {} et ton mot de pass est {}".format(text[1], text[0], text[2]))
#exo1

listes_nombres = [1, 2, 3, 4, 5,
                   6, 7, 8, 9, 10]
plus_grand_nombre = max(listes_nombres)
print(f"le plus grand nombre est {plus_grand_nombre}")
 #exo2
notes = [
          13, 14, 9 , 8,
          18, 11, 5, 19
        ]
la_moyenne = mean(notes)
print(f"la moyenne de l'eleve est {la_moyenne}")
#exo 3



 











