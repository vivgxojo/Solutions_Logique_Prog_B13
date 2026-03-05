# Convertir 5 vitesses au choix de l’utilisateur
for i in range(5):
    vitesse = float(input("Entrez une vitesse en Mbps: "))
    vitesse_convertie = vitesse / 8
    print(f"{vitesse_convertie} MB/s")