def AdditionEntier_0_a_Nombre(nombre):
    """
    Cette fonction accepte additionne tous les nombres de zéro jusqu'au nombre qui est entré (exclu ou -1)
    Args:
        Nombre: Un nombre entier qui n'est pas zéro, aucune validation pour caractère ou nombre réel

    Returns: Résultat qui est un nombre de type entier
    """
    resultat = 0
    for i in range(nombre):
        resultat += i
    return resultat

# def valide_AdditionEntier_0_a_Nombre

# Validation de la fonction par des tests unitaires
if __name__ == '__main__':
    assert AdditionEntier_0_a_Nombre(5) == 10
    print("Les tests ont réussis")