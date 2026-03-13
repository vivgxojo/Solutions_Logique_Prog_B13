domaine = "@cegep.ca"
i = 10
while True:
    prenom = input("Prénom : ")
    if prenom == "":
        break
    nom = input("Nom    : ")
    print(prenom + "." + nom + str(i) + "@" + domaine)
    i += 1