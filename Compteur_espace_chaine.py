def Est_caractere_espace(c):
    """
    Cette fonction valide si le caractere passé en paramètre est un espace
    Args:
        c: type caractère

    Returns:
        Boolean: True si vrai

    """
    return c == ' '

def Compteur_espace_chaine(chaine):
    """
    Cette fonction compte le nombre d'espace qu'il y a entre les mots dans une phrase
    Elle utilise une autre fonction qui est dans le même module
    Args:
        chaine: Une chaine (type str)

    Returns: un entier, le nombre d'espace

    """
    nombre_espaces = 0
    for c in chaine:
        if Est_caractere_espace(c):
            nombre_espaces += 1
    return nombre_espaces

rep = Compteur_espace_chaine("Mon grand ami")
print(rep)