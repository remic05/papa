# Ce programme détermine si un nombre entré par l'utilisateur est pair
print("Je devine si votre nombre est pair ou impair.")
number = int(input("SVP, entrez un nombre entier différent de 0: "))
if number % 2 == 0:
    print("Le nombre", number, "est bien un nombre pair")
else:
    print("Le nombre", number, "n'est pas nombre pair, donc il est impair")

def nombre_pair (nombre):
    """
    # Cette fonction détermine si un nombre entier est un nombre pair.
    # Il n'y a pas de validation pour savoir si c'est nombre réel, 0 ou un caractère
    Args:
        nombre: un nombre entier
    
    Returns: True si cMest un nombre pair
    """
    return nombre % 2 == 0

print(nombre_pair(7)) # Appel de la fonction

if __name__ == '__main__':
    assert nombre_pair(8) == True
    print("Les tests ont réussis")

