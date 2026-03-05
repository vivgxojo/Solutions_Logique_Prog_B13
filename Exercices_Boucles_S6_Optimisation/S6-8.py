# Déterminer si un numéro de port est valide et les classifier
for i in range(10):
    # Demander le numéro de port à l'utilisateur
    port = int(input("Entrez un numéro de port (0-65535) : "))

    # Vérification (un port valide: 0 <= port <= 65535)
    port_valide = port >= 0 and port <= 65535

    # Affichage
    print("Port", port, "valide:", port_valide)

    # Vérifier la validité du port et déterminer la catégorie
    if not port_valide:
        categorie = "Erreur : Le numéro de port ne peut pas être négatif et ne peut pas dépasser 65535."
    elif port <= 1023:
        categorie = "Ports bien connus"
    elif port <= 49151:
        categorie = "Ports enregistrés"
    else:
        categorie = "Ports dynamiques/privés"

    # Afficher le résultat
    print(f"Le port {port} appartient à la catégorie : {categorie}")
