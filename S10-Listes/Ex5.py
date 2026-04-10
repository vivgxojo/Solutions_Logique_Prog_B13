pings = []

print("=== Analyseur de temps de ping ===")
print("Entrez les temps de ping en ms (tapez 'fin' pour terminer) :")

continuer = True
while continuer:
    valeur = input("Ping (ms) : ")
    if valeur == "fin":
        continuer = False
    else:
        try:
            ping_ms = float(valeur)
            if ping_ms < 0:
                print("Erreur : un temps de ping ne peut pas être négatif.")
            else:
                pings.append(ping_ms)
                print("Valeur enregistrée.")
        except ValueError:
            print("Erreur : entrez un nombre valide.")

print("\n--- Résultats ---")

if len(pings) == 0:
    print("Aucune donnée enregistrée.")
else:
    print("Nombre de pings : " + str(len(pings)))

    minimum = pings[0]
    maximum = pings[0]
    total = 0

    i = 0
    while i < len(pings):
        if pings[i] < minimum:
            minimum = pings[i]
        if pings[i] > maximum:
            maximum = pings[i]
        total = total + pings[i]
        i = i + 1

    moyenne = total / len(pings)

    print("Ping minimum : " + str(minimum) + " ms")
    print("Ping maximum : " + str(maximum) + " ms")
    print("Ping moyen   : " + str(round(moyenne, 2)) + " ms")

    if moyenne > 100:
        print("Avertissement : latence élevée détectée !")
    else:
        print("Latence normale.")