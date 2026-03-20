# =============================================================================
# Question 1 — Validation d'un PORT réseau
# =============================================================================

valide = False

while not valide:
    saisie = input("Entrez un numéro de port (0–65535) : ")
    try:
        port = int(saisie)
        if not (0 <= port <= 65535):
            print("Saisie invalide — entrez un nombre entre 0 et 65535.")
        else:
            valide = True
    except ValueError:
        print("Saisie invalide — entrez un entier.")

if 0 <= port <= 1023:
    categorie = "Port système (well-known)"
elif 1024 <= port <= 49151:
    categorie = "Port enregistré"
else:
    categorie = "Port dynamique / privé"

print(f"Port {port} — {categorie}")