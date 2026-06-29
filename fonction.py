def calculer_prix(quantite, prix_unitaire=1000):
  total =  quantite * prix_unitaire
  return total
"""
Calculer le prix total.
Quantite : nombre d'articles
prix_unitaire : prix  par article (defaut 1000 GNF)
total : c;est la multiplication entre la quantite et le prix
"""


calculer_prix(625, 5000)
print(calculer_prix(625, 5000))
print(calculer_prix.__doc__)
