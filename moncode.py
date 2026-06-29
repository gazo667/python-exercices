def question(annonce, essais =4, please = 'oui ou non, s.v.p !'):
    while essais > 0:
        reponse = input(annonce)
        if reponse in ('o', 'oui','o','oui','OUI'):
            return 1
        if reponse in ('n', 'non','Non','NON'):
            return 0
        print(please)
        essais = essais - 1



    



   


