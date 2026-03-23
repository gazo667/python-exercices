
def  get_vowel_numbers(word):
    vowels = "aiouyAIOUY"
    compteur = 0
    for lettre in word:
        if lettre in vowels:
            compteur =+ 1
            return compteur
        word = input("entrez le mot : ")
        result = get_vowel_numbers(word)
        print("nombre de voyelles :", result)