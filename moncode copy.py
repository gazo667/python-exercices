point = (1, 2)
match point:
    case (0, 0):
        print("Voici l'origine")
        case (0, y)
        print(f"Voici l'axe des ordonnées, y = {y}")
    case (x, 0):
        print(f"Voici l'axe des abscisses, x = {x}")
    case (x, y):
        print(f"Voici le point ({x}, {y})")
    case _ :
        raise ValueError("Point non reconnu")
    