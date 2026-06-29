def ligneCar(n, ca):
    return n*ca

def surfCercle(R):
    
    return R* R * 3.141559
print(surfCercle(2.5))

def volboite(x1,x2,x3):
    volume = x1 * x2 * x3
    return volume
print(volboite(5.2, 7.7, 3.3))


def maximum(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
     print(f"{n1} est le maximun")
    elif n2 >= n3 and n3 > n1:
        print(f"{n2} est le maximum")
    else:
        print(f"{n3} est le maximun et {n1} et {n2} sont les minimuns")
        print(maximum(2, 10, 25))

    


    