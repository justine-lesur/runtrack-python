chaine = input('Entrez une chaîne de caractères: ')

fichier = open("output.txt", "a")
fichier.write(chaine)
fichier.close()