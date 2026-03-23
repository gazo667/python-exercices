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

# pour clear poir vider totalement une liste ou un set

listes_des_invités = {"Peter thiel", "Marc andersen", "Marc Zuckerberg", "Palmer luckey"}
listes_des_invités.clear ()
print(listes_des_invités)









