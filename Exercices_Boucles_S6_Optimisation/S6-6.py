# Demander la vitesse de connexion
vitesse_mbps = float(input("Entrez la vitesse de connexion (Mbps) : "))

# Calcul du débit théorique en MB/s
debit_mbs = vitesse_mbps / 8

while True:
    fichier = int(input("Entrez la taille du fichier en MB ou -1 pour terminer: "))
    if fichier == -1:
        break

    # Calcul des temps de téléchargement
    temps_sec = fichier / debit_mbs

    # Conversion en minutes
    temps_min = temps_sec / 60

    # Affichage
    print("\n===== DÉBIT THÉORIQUE =====")
    print("Vitesse de connexion :", vitesse_mbps, "Mbps")
    print("Débit théorique :", debit_mbs, "MB/s")

    print("\n===== TEMPS DE TÉLÉCHARGEMENT =====")
    print("  -", round(temps_sec, 2), "secondes")
    print("  -", round(temps_min, 2), "minutes")

    # Exemple d'exécution avec 100 Mbps :
    # Débit théorique : 12.5 MB/s
    # 100 MB : 8.0 secondes
    # 1 GB : 81.92 secondes (1.37 minutes)
    # 5 GB : 409.6 secondes (6.83 minutes)
