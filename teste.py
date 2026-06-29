eleves = ["Ali", "jean", "sophie", "jean", "marc"]

eleves_compte = []
for eleve in eleves :
   if eleve not in eleves_compte:
      eleves_compte.append(eleve)
      repeat = eleves.count(eleve)
      print(f"\n {eleve} apparait une fois " if repeat==1 else f"\n {eleve} apparait {repeat} fois")

      
 # suppression des doublon
eleves = eleves_compte
print(f"\nAprès suppression des doublons, on a : eleves = {eleves} ")
  
 # tri de la liste
eleves.sort(key= len) # selon la longueur des mots
print(f"\nAprès le tri de la liste , on a : eleves = {eleves}")


 # ajoutons un nouvelle eleve Paul
eleves.append("Paul")

 # verifions si sophie est dans la liste
print("\nSophie est dans la liste " if "Sophie" in eleves else f"\nSophie n'est pas dans liste")

 #suprimons le doublons jean
eleves.remove("jean")

 # affichage de la liste finie
print(f"\nAprès toute les modifications, la nouvelle liste est : eleves = {eleves}")
