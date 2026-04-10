whitelist = []
blacklist = []

print("=== Création d'une ACL ===")
print("Commandes : W = whitelist | B = blacklist | fin = terminer")

continuer = True
while continuer:
    choix = input("\nAjouter à (W/B/fin) : ")

    if choix == "fin":
        continuer = False

    elif choix == "W" or choix == "w":
        ip = input("Adresse IP à ajouter à la whitelist : ")
        whitelist.append(ip)
        print("Ajouté à la whitelist.")

    elif choix == "B" or choix == "b":
        ip = input("Adresse IP à ajouter à la blacklist : ")
        blacklist.append(ip)
        print("Ajouté à la blacklist.")

    else:
        print("Choix invalide, recommencez.")

print("\n--- WHITELIST ---")
if len(whitelist) == 0:
    print("(vide)")
else:
    i = 0
    while i < len(whitelist):
        print("  ALLOW  " + whitelist[i])
        i = i + 1

print("\n--- BLACKLIST ---")
if len(blacklist) == 0:
    print("(vide)")
else:
    i = 0
    while i < len(blacklist):
        print("  DENY   " + blacklist[i])
        i = i + 1

print("\n--- Vérification des conflits ---")
conflit_trouve = False
i = 0
while i < len(whitelist):
    if whitelist[i] in blacklist:
        print("CONFLIT détecté : " + whitelist[i] + " est dans les deux listes !")
        conflit_trouve = True
    i = i + 1

if not conflit_trouve:
    print("Aucun conflit détecté.")