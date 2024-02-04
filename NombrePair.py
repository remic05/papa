# Ce programme détermine si un nombre entré par l'utilisateur est pair
number = int(input("SVP, entrez un nombre entier différent de 0: "))
if number % 2 == 0:
    print("Le nombre", number, "est bien un nombre pair")
else:
    print("Le nombre", number, "n'est pas nombre pair, donc il est impair")
