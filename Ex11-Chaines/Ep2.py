# On demande les 12 caractères de l'adresse MAC
mac_brut = input("Entrez une adresse MAC brute (12 caractères, ex: AABBCCDDEEFF) : ")

# On met en majuscules pour uniformiser
mac_brut = mac_brut.upper()

# On découpe en 6 groupes de 2 caractères
groupes = []
i = 0
while i < len(mac_brut):
    groupe = mac_brut[i : i+2]
    groupes.append(groupe)
    i = i + 2

# Format avec tirets
mac_tirets = "-".join(groupes)

# Format avec deux-points
mac_colons = ":".join(groupes)

# Format en groupes de 4 (Cisco)
groupe4_1 = groupes[0] + groupes[1]
groupe4_2 = groupes[2] + groupes[3]
groupe4_3 = groupes[4] + groupes[5]
mac_cisco = groupe4_1 + "." + groupe4_2 + "." + groupe4_3

print("\n--- Formats de l'adresse MAC ---")
print("Format tirets  :", mac_tirets)
print("Format colons  :", mac_colons)
print("Format Cisco   :", mac_cisco)