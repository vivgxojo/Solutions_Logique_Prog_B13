pool_disponible = []
pool_attribue = []

print("=== Simulateur de pool DHCP ===")

try:
    reseau = input("Entrez la base du réseau (ex: 192.168.1) : ")
    debut = int(input("Octet de début (ex: 10) : "))
    fin = int(input("Octet de fin   (ex: 50) : "))

    if debut < 1 or fin > 254 or debut > fin:
        print("Erreur : plage invalide.")
    else:
        i = debut
        while i <= fin:
            pool_disponible.append(reseau + "." + str(i))
            i = i + 1
        print(str(len(pool_disponible)) + " adresses générées dans le pool.")

except ValueError:
    print("Erreur : veuillez entrer des entiers valides.")

continuer = True
while continuer and len(pool_disponible) > 0 or continuer and len(pool_attribue) > 0:
    print("\nOptions : 1=Attribuer IP | 2=Libérer IP | 3=Afficher pool | 4=Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        if len(pool_disponible) == 0:
            print("Pool épuisé ! Aucune adresse disponible.")
        else:
            ip_attribuee = pool_disponible[0]
            pool_disponible.remove(ip_attribuee)
            pool_attribue.append(ip_attribuee)
            print("IP attribuée : " + ip_attribuee)
            print("Adresses restantes : " + str(len(pool_disponible)))

    elif choix == "2":
        if len(pool_attribue) == 0:
            print("Aucune adresse actuellement attribuée.")
        else:
            ip_a_liberer = input("Entrez l'IP à libérer : ")
            if ip_a_liberer in pool_attribue:
                pool_attribue.remove(ip_a_liberer)
                pool_disponible.append(ip_a_liberer)
                print("IP " + ip_a_liberer + " remise dans le pool.")
            else:
                print("Cette IP n'est pas dans la liste des IP attribuées.")

    elif choix == "3":
        print("\nPool disponible (" + str(len(pool_disponible)) + ") :")
        i = 0
        while i < len(pool_disponible):
            print("  " + pool_disponible[i])
            i = i + 1
        print("\nPool attribué (" + str(len(pool_attribue)) + ") :")
        i = 0
        while i < len(pool_attribue):
            print("  " + pool_attribue[i])
            i = i + 1

    elif choix == "4":
        continuer = False

    else:
        print("Option invalide.")