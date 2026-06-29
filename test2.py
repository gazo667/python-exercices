annee = int(input("Quelle est la duree du placement "))
somme_investi = int(input("Quelle est la somme place "))
taux = float(input("Quelle est le taux d'interet "))
interet = somme_investi*annee*taux/1200
print(f"les interet genere du placement est {interet}")