# =============================================================================
# Question 2 — Validation d'un VLAN
# =============================================================================

# --- ID VLAN ---
valide = False

while not valide:
    saisie = input("Entrez l'ID VLAN (1–4094) : ")

    try:
        vlan_id = int(saisie)
        if (1 <= vlan_id <= 4094):
            break
        else:
            print("ID invalide — entrez un nombre entre 1 et 4094")
    except ValueError:
        print("ID invalide — entrez un entier.")

# --- Nom ---
nom = input("Entrez le nom du VLAN : ")

# --- Priorité STP ---
valide = False

while not valide:
    saisie = input("Entrez la priorité STP (0–61440, multiple de 4096) : ")
    try:
        priorite = int(saisie)
        if (0 <= priorite <= 61440) and priorite % 4096 != 0:
            break
        print("Priorité invalide — multiple de 4096 entre 0 et 61440")
    except ValueError:
        print("Priorité invalide — entrez en entier")

# --- Résumé ---
print(f"Résumé VLAN")
print(f"    ID       : {vlan_id}")
print(f"    Nom      : {nom}")
print(f"    Priorité : {priorite}")