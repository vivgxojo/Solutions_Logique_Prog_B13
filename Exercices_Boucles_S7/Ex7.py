vlan_valide = False

while not vlan_valide:
    entree = input("Entrez un numéro de VLAN (1-4094) : ")

    # Vérifier que tous les caractères sont des chiffres
    entree_ok = True
    for caractere in entree:
        if caractere < "0" or caractere > "9":
            entree_ok = False
            break

    if not entree_ok or entree == "":
        print("  Veuillez entrer un nombre entier positif.")
        continue

    vlan = int(entree)

    if vlan < 1 or vlan > 4094:
        print("  Le VLAN doit être entre 1 et 4094.")
    elif 1002 <= vlan <= 1005:
        print("  Les VLANs 1002 à 1005 sont réservés.")
    else:
        vlan_valide = True
        if vlan == 1:
            print("  VLAN " + str(vlan) + " accepté (VLAN natif par défaut).")
        else:
            print("  VLAN " + str(vlan) + " valide.")