
while True:
    vlan1 = input("Entrez un numéro de VLAN : ")
    if vlan1 == "":
        break

    # Conversion des types str en int
    vlan1 = int(vlan1)

    # Validation (VLAN valides: 1-4094)
    print("\n--- Validation ---")
    vlan1_valide = vlan1 >= 1 and vlan1 <= 4094

    print("VLAN", vlan1, "valide:", vlan1_valide)

    # Déterminer le type de VLAN
    print("\n--- Type de VLAN ---")

    # VLAN 1 - Standard et Étendu
    vlan1_standard = vlan1 >= 1 and vlan1 <= 1005
    vlan1_etendu = vlan1 >= 1006 and vlan1 <= 4094


    # Affichage
    print("VLAN", vlan1, "- Standard:", vlan1_standard, "- Étendu:", vlan1_etendu)


    # Vérifier si c'est un VLAN réservé
    print("\n--- VLANs réservés ---")
    vlan1_reserve = vlan1 == 0 or vlan1 == 1 or (vlan1 >= 1002 and vlan1 <= 1005)

    print("VLAN", vlan1, "réservé:", vlan1_reserve)  # False
    print()

    # Résultats:
    # VLAN 1: 10 → valide, standard, non réservé
    # VLAN 2: 20  → valide, standard, non réservé
    # VLAN 3: 100  → valide, standard, non réservé
    # VLAN 4: 1005  → valide, standard, réservé
