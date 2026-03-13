ip_valide = False

while not ip_valide:

    octets_valides = 0
    octet1 = 0
    octet2 = 0
    octet3 = 0
    octet4 = 0

    # Boucle imbriquée : demander et valider chaque octet un par un
    for num_octet in range(1, 5):

        octet_ok = False

        while not octet_ok:
            valeur = int(input("  Entrez l'octet " + str(num_octet) + " (0-255) : "))

            if valeur < 0 or valeur > 255:
                print("  Erreur : l'octet doit être entre 0 et 255.")
            else:
                # Stocker dans la bonne variable selon le numéro d'octet
                if num_octet == 1:
                    octet1 = valeur
                elif num_octet == 2:
                    octet2 = valeur
                elif num_octet == 3:
                    octet3 = valeur
                elif num_octet == 4:
                    octet4 = valeur

                octet_ok = True
                octets_valides += 1

    # Si les 4 octets sont valides, afficher l'adresse complète
    if octets_valides == 4:
        ip_valide = True
        adresse = str(octet1) + "." + str(octet2) + "." + str(octet3) + "." + str(octet4)
        print("\n  Adresse IP valide : " + adresse)
