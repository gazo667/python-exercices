# exo 1
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in nombres:
    if n % 2 ==0:
        print(nombres)

#exo 2
liste_de_nom = ['aboubacar', 'moussa', 'Laye', 'abdoulaye']
for nom in liste_de_nom:
    print(nom.upper())


# exo 3
liste_de_nombre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for x in liste_de_nombre:
    total += x
print(total)

#exo 4
liste = [2, 4, 6, 8, 10, 12]
sup = []
moyenne = sum(liste)/ len(liste)
for n in liste:
        if n > moyenne:
             sup.append(n)
             print(sup)

# exo 5
   
doublons  = ['bsb', 'bsb', 'prada', 'prada', 'Gucci', 'gucci']
ndbl = []
for n in doublons:
    if n not in ndbl:
      ndbl.append(n)
      

