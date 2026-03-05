for i in range(24, 31):

    nb_hotes = 2**(32 - i) - 2

    # Affichage
    print("Sous-réseau /" + str(i), ":", nb_hotes, "hôtes disponibles")
