# a)
# Demander a l'utilisateur de chosiir deux nombres , s'assurer que ce soit un nombre
# Et calculer la moyenne de ses nombres


# b) Demander à l'utilisateur un nombre, s'assurer que ce soit un nombre, et crée une liste en ajoutant 1 à la fin.
# montrer la liste jusqu'a 10 valeurs.
nb1 = input("Entrer un numéro: ")
liste = []
somme = 0
y = 0


if nb1.isnumeric(): #or nb1.isfloat(): trouver un nombre flottant
    nb1 = int(nb1)

#     if nb1.replace('.', '', 1).isdigit():  # Vérifie si la chaîne ne contient que des chiffres et au plus un point
# Convertir en flottant si la chaîne contient un point
#    if '.' in nb1:
#       nb1 = float(nb1)
#   else:
#       nb1 = int(nb1)

    while len(liste) != 10:
        liste.append(nb1)
        print(liste)
        nb1 += 1
else:
    nb1 = input("Entrer un numéro: ")
# b.2) Adittioner tous les nombres de la liste

for i in liste:
    print(i)
    somme += i

print(somme)


# b.3 cr.ation d,un objet, ajout de 2 caractéristiques
def crea_robot(modele, carburant):
    robot = {
        modele: modele,
        carburant: carburant,
    }

    def bruit():
        print("bip bop")
        print(modele + carburant)

    return robot


rp = crea_robot("rp1", "diesel")
