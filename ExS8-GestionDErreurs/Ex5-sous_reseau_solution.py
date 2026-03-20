# ── Adresse IP ───────────────────────────────────────────────────────────────

octet_ok = False
while not octet_ok:
    try:
        ip1 = int(input("IP - Octet 1 : "))
        if ip1 < 0 or ip1 > 255:
            print("Erreur : octet hors plage (0-255).")
        else:
            octet_ok = True
    except ValueError:
        print("Erreur : entrez un entier.")

octet_ok = False
while not octet_ok:
    try:
        ip2 = int(input("IP - Octet 2 : "))
        if ip2 < 0 or ip2 > 255:
            print("Erreur : octet hors plage (0-255).")
        else:
            octet_ok = True
    except ValueError:
        print("Erreur : entrez un entier.")

octet_ok = False
while not octet_ok:
    try:
        ip3 = int(input("IP - Octet 3 : "))
        if ip3 < 0 or ip3 > 255:
            print("Erreur : octet hors plage (0-255).")
        else:
            octet_ok = True
    except ValueError:
        print("Erreur : entrez un entier.")

octet_ok = False
while not octet_ok:
    try:
        ip4 = int(input("IP - Octet 4 : "))
        if ip4 < 0 or ip4 > 255:
            print("Erreur : octet hors plage (0-255).")
        else:
            octet_ok = True
    except ValueError:
        print("Erreur : entrez un entier.")

# ── Masque ────────────────────────────────────────────────────────────────────

octet_ok = False
while not octet_ok:
    try:
        m1 = int(input("Masque - Octet 1 : "))
        if m1 < 0 or m1 > 255:
            print("Erreur : octet hors plage (0-255).")
        else:
            octet_ok = True
    except ValueError:
        print("Erreur : entrez un entier.")

octet_ok = False
while not octet_ok:
    try:
        m2 = int(input("Masque - Octet 2 : "))
        if m2 < 0 or m2 > 255:
            print("Erreur : octet hors plage (0-255).")
        else:
            octet_ok = True
    except ValueError:
        print("Erreur : entrez un entier.")

octet_ok = False
while not octet_ok:
    try:
        m3 = int(input("Masque - Octet 3 : "))
        if m3 < 0 or m3 > 255:
            print("Erreur : octet hors plage (0-255).")
        else:
            octet_ok = True
    except ValueError:
        print("Erreur : entrez un entier.")

octet_ok = False
while not octet_ok:
    try:
        m4 = int(input("Masque - Octet 4 : "))
        if m4 < 0 or m4 > 255:
            print("Erreur : octet hors plage (0-255).")
        else:
            octet_ok = True
    except ValueError:
        print("Erreur : entrez un entier.")

# ── Calcul du réseau de l'IP (IP AND masque, octet par octet) ─────────────────

reseau1 = ip1 & m1
reseau2 = ip2 & m2
reseau3 = ip3 & m3
reseau4 = ip4 & m4

# ── Réseau de référence ───────────────────────────────────────────────────────

print("\nAdresse du réseau à vérifier :")

octet_ok = False
while not octet_ok:
    try:
        r1 = int(input("Réseau - Octet 1 : "))
        if r1 < 0 or r1 > 255:
            print("Erreur : octet hors plage (0-255).")
        else:
            octet_ok = True
    except ValueError:
        print("Erreur : entrez un entier.")

octet_ok = False
while not octet_ok:
    try:
        r2 = int(input("Réseau - Octet 2 : "))
        if r2 < 0 or r2 > 255:
            print("Erreur : octet hors plage (0-255).")
        else:
            octet_ok = True
    except ValueError:
        print("Erreur : entrez un entier.")

octet_ok = False
while not octet_ok:
    try:
        r3 = int(input("Réseau - Octet 3 : "))
        if r3 < 0 or r3 > 255:
            print("Erreur : octet hors plage (0-255).")
        else:
            octet_ok = True
    except ValueError:
        print("Erreur : entrez un entier.")

octet_ok = False
while not octet_ok:
    try:
        r4 = int(input("Réseau - Octet 4 : "))
        if r4 < 0 or r4 > 255:
            print("Erreur : octet hors plage (0-255).")
        else:
            octet_ok = True
    except ValueError:
        print("Erreur : entrez un entier.")

# ── Vérification ──────────────────────────────────────────────────────────────

print("")
print("IP      :", ip1, ".", ip2, ".", ip3, ".", ip4)
print("Masque  :", m1,  ".", m2,  ".", m3,  ".", m4)
print("Réseau  :", r1,  ".", r2,  ".", r3,  ".", r4)
print("")

if reseau1 == r1 and reseau2 == r2 and reseau3 == r3 and reseau4 == r4:
    print("L'adresse IP appartient au sous-réseau.")
else:
    print("L'adresse IP n'appartient PAS au sous-réseau.")
    print("(Son réseau calculé est :", reseau1, ".", reseau2, ".", reseau3, ".", reseau4, ")")
