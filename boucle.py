
# comme en algorithme au niveau de des boucle for veut dire tant que elle est utilise lorsque le nombre de boucle est connu de la valeur de depart jusqu'a la valeur d'arrivé
#for numeros_client in range(1, 5):
   # print("Vous etes le client numero", numeros_client)
# for each : qui signifie pour chaque valeur d'une liste données
#emails = ["bsbwolrd@gmail.com", "667ffg@gmail.com", "syliholding@gmail.com"]

#black_list = ["chichalouge224@gmail.com", "cocobeauty@gmail.com"]

#for email in emails:

 #if email in black_list:
        #print("Email {} interdit, envoie impossble ...".format(email))
        #break
#print(f"Email envoye a : {email}")      

   
 # black list

# exo 1
 
i = 100
for i in range(0, 101):
    print(i)
    i += 1
    # exercice 2
i = 50
for i in range(1, 51):
    if i % 2 == 0:
      print(i)
    
# exo 3
n = int(input("Quelle est la valeur de n "))
somme = 0
for i in range(1, n + 1):
   somme += i

   print(f"la somme est {somme}")
   # exo 4
n = int(input("Quelle le nombre "))
table_de_multiplication = 0
for i in range(1, 11):
    table_de_multiplication = n * i
print(f"{n} fois {i} donne {table_de_multiplication}")

# exo 5
chiffre = 12345
nb_chiffre = len(str(chiffre))
print(chiffre)
    # exo 6



multiple = []
for i in range (1, 101):
   if i % 3 == 0 and i % 5 == 0:
      multiple.append(i)
      print(multiple)
      


      
      #exo 8
      
      
nb_premier = [2]
for i in range(1, 11):
   if i % 1 == 0 and i % i == 1 :
      
    nb_premier.append(i)
   print(nb_premier)





   


