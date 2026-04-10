vlans_actifs = []

print("=== Gestionnaire de VLANs ===")

continuer = True
while continuer:
    print("\nOptions : 1=Ajouter | 2=Vérifier | 3=Retirer | 4=Afficher | 5=Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        try:
            numero = int(input("Numéro du VLAN à ajouter (1-4094) : "))
            if numero < 1 or numero > 4094:
                print("Erreur : numéro de VLAN invalide.")
            elif numero in vlans_actifs:
                print("Avertissement : le VLAN " + str(numero) + " est déjà actif.")
            else:
                vlans_actifs.append(numero)
                print("VLAN " + str(numero) + " ajouté.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre entier.")

    elif choix == "2":
        try:
            numero = int(input("Numéro du VLAN à vérifier : "))
            if numero in vlans_actifs:
                print("VLAN " + str(numero) + " est ACTIF.")
            else:
                print("VLAN " + str(numero) + " est INACTIF.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre entier.")

    elif choix == "3":
        try:
            numero = int(input("Numéro du VLAN à retirer : "))
            if numero in vlans_actifs:
                vlans_actifs.remove(numero)
                print("VLAN " + str(numero) + " retiré.")
            else:
                print("VLAN " + str(numero) + " non trouvé dans la liste.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre entier.")

    elif choix == "4":
        print("\nVLANs actifs : ")
        if len(vlans_actifs) == 0:
            print("  Aucun VLAN actif.")
        else:
            i = 0
            while i < len(vlans_actifs):
                print("  VLAN " + str(vlans_actifs[i]))
                i = i + 1

    elif choix == "5":
        continuer = False

    else:
        print("Option invalide.")