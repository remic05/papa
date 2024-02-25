def Est_caractere_espace(c):
    """
    Cette fonction valide si le caractere passé en paramètre est un espace
    Args:
        c: type caractère

    Returns:
        Boolean: True si vrai

    """
    return c == ' '

if __name__ == '__main__':
    assert Est_caractere_espace(' ')
    print("Les tests ont réussis")