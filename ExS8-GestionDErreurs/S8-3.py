# =============================================================================
# Question 3 — Validation d'un préfixe CIDR
# =============================================================================

while True:
    saisie = input("Entrez un préfixe CIDR (0–32) : ")
    try:
        cidr = int(saisie)
        if not (0 <= cidr <= 32):
            print("Saisie invalide — entrez un nombre entre 0 et 32.")
        else:
            break
    except ValueError:
        print("Saisie invalide — entrez un entier.\n")

hotes = 2 ** (32 - cidr) - 2

if hotes < 0:
    hotes = 0

print(f"/{cidr} — Adresses hôtes : 2^{32 - cidr} - 2 = {hotes}")