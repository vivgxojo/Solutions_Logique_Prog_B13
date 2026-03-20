"""
BOUCLE INFINI
    AFFICHER menu
    DEMANDE choix
    SI choix = a
        DEMANDER nom
        DEMANDER prenom
        BOUCLE INFINI
            ESSAYER
                DEMANDER age
                SI age > 0
                    FIN BOUCLE
                SINON
                    AFFICHER erreur
            ATTRAPPER ERREUR
                AFFICHER erreur
        DEMANDER username
        DEMANDER password
        BOUCLE INFINIE
            DEMANDER conditions_acceptées
            SI conditions_acceptées
                FIN BOUCLE
            SINON
                AFFICHER erreur
        AFFICHER confirmation
    SINON SI choix = b
        DEMANDER username2
        DEMANDER password2
        SI username2 != username OU password2 != password
            AFFICHER erreur
        SINON
            BOUCLE INFINIE
                AFFICHER sous-menu
                DEMANDER choix2
                SI choix2 = 1
                    REDEMANDER LES INFO
                SINON SI choix2 = 2
                    FIN BOUCLE
                SINON
                    AFFICHER erreur
    SINON SI choix = c
        FIN BOUCLE
    SINON
        AFFICHER erreur
"""
username = ""
password = ""
while True:
    print("a) Créer un compte")
    print("b) Se connecter")
    print("c) Quitter")
    choix = input("Que voulez-vous faire? ")
    if choix == "a":
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        while True:
            try:
                age = int(input("Âge : "))
                if age > 0:
                    break
                else:
                    print("Erreur : l'âge doit être plus grand que 0")
            except ValueError: # OPTIONNEL: Préciser le type d'erreur à attrapper
                print("Erreur : l'âge doit être un nombre entier")
        username = input("Username : ")
        password = input("Password : ")
        while True:
            conditions_acceptees = bool(input("Accepter les conditions? "))
            if conditions_acceptees:
                break
            else:
                print("Erreur : Vous devez accepter les conditions!")
        print("Le compte a bien été créé.")
    elif choix == "b":
        username2 = input("Username : ")
        password2 = input("Password : ")
        if username2 != username or password2 != password:
            print("Erreur : Username ou password non valide")
        else:
            while True:
                print("1. Modifier compte")
                print("2. Déconnecter")
                choix2 = input("Entrez votre choix : ")
                if choix2 == "1":
                    nom = input("Nom : ")
                    prenom = input("Prénom : ")
                    while True:
                        try:
                            age = int(input("Âge : "))
                            if age > 0:
                                break
                            else:
                                print("Erreur : l'âge doit être plus grand que 0")
                        except ValueError:  # OPTIONNEL: Préciser le type d'erreur à attrapper
                            print("Erreur : l'âge doit être un nombre entier")
                    username = input("Username : ")
                    password = input("Password : ")

                    print("Le compte a bien été modifié.")
                elif choix2 == "2":
                    break
                else:
                    print("Erreur : Choix non valide")
    elif choix == "c":
        break
    else:
        print("Erreur : Choix non valide")