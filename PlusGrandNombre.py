# Ce programme demande deux nombres à l'utilisateur et détermine le plus grand
number_1 = int(input("Entrer un premier nombre entier SVP: ")) # La fonction int convertie la chaine en entier
number_2 = int(input("Entrer un deuixème nombre entier SVP: "))
if number_1 > number_2:
    print("Le nombre le plus grand est: ", number_1)
elif number_2 > number_1:
    print("Le nombre le plus grand est: ", number_2)
else:
    print("Vous avez entré 2 nombres identiques") #Cas de figure d'exception