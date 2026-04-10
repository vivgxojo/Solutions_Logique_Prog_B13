adresses_ip = []

print("=== Gestionnaire d'adresses IP ===")
print("Entrez les adresses IP (tapez 'fin' pour terminer) :")

continuer = True
while continuer:
    ip = input("Adresse IP : ")
    if ip == "fin":
        continuer = False
    else:
        adresses_ip.append(ip)

print("\n--- Analyse de la liste ---")

if len(adresses_ip) == 0:
    print("Avertissement : aucune adresse IP enregistrée.")
else:
    print("Nombre total d'adresses : " + str(len(adresses_ip)))

    try:
        print("Première adresse attribuée : " + adresses_ip[0])
        print("Dernière adresse attribuée  : " + adresses_ip[-1])

        index_milieu = len(adresses_ip) // 2
        print("Adresse centrale (index " + str(index_milieu) + ") : " + adresses_ip[index_milieu])

    except IndexError:
        print("Erreur : impossible d'accéder à un élément de la liste.")