# demandons a l'utilisateur sa liste de note

saisie = input("Entrez vos notes separees par des espaces: ")

liste_de_notes = [int(n) for n in saisie.split()]
moyenne = sum(liste_de_notes) / len(liste_de_notes)
print(moyenne)