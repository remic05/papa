# a)
# Demander a l'utilisateur de chosiir deux nombres , s'assurer que ce soit un nombre
# Et calculer la moyenne de ses nombres


# b) Demander à l'utilisateur un nombre, s'assurer que ce soit un nombre, et crée une liste en ajoutant 1 à la fin.
# montrer la liste jusqu'a 10 valeurs.
nb1 = input("Entrer un numéro: ")
liste = []
somme = 0

if nb1.isnumeric():
    nb1 = int(nb1)

    while len(liste) != 10:
        liste.append(nb1)
        print(liste)
        nb1 += 1
else:
    nb1 = input("Entrer un numéro: ")
# b.2) Adittioner tous les nombres de la liste

for i in liste:
    print(i)
    i = liste[i]
    somme += i

print(somme)
