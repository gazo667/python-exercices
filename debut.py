from turtle import*
def triangle(couleur):
    color(couleur)
    for i in range(3):
        forward(100)
        left(120)

        couleurs = ['red', 'blue', 'green','orange']
        x = -250

        for c in couleurs:
            penup()
            goto(x, 0)
            pendown()

            triangle(c)
            x+= 120
    done()


