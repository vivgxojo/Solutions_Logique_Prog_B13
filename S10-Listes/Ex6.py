equipements = []
macs = []
nb_conflits = 0

print("=== Détecteur de doublons d'adresses MAC ===")
print("Entrez les équipements (tapez 'fin' pour terminer) :")

continuer = True
while continuer:
    nom = input("\nNom de l'équipement : ")

    if nom == "fin":
        continuer = False

    else:
        mac = input("Adresse MAC de " + nom + " : ")

        # Vérifier si la MAC est déjà présente
        doublon_trouve = False
        i = 0
        while i < len(macs):
            if macs[i] == mac:
                print("ALERTE CONFLIT : " + mac + " est déjà attribuée à " + equipements[i] + " !")
                nb_conflits = nb_conflits + 1
                doublon_trouve = True
            i = i + 1

        if not doublon_trouve:
            print("Adresse MAC unique, enregistrement OK.")

        equipements.append(nom)
        macs.append(mac)

print("\n--- Inventaire des équipements ---")
i = 0
while i < len(equipements):
    print("  " + equipements[i] + "  →  " + macs[i])
    i = i + 1

print("\nTotal d'équipements enregistrés : " + str(len(equipements)))
print("Total de conflits MAC détectés  : " + str(nb_conflits))

if nb_conflits > 0:
    print("Attention : des conflits d'adresses MAC doivent être corrigés !")
else:
    print("Aucun conflit détecté. Réseau sain.")