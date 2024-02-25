def Addition_Nombres(nb_1, nb_2):
    """
    Cette fonction additionne 2 nombres fournies par l'utilisateur
    Args:
        nb_1: Est un entier
        nb_2: Esr un entier

    Returns: le resultat qui est un entier

    """
    return nb_1 + nb_2

if __name__ == '__main__':
    assert Addition_Nombres(3, 11) == 14
    print("Les tests ont réussis")