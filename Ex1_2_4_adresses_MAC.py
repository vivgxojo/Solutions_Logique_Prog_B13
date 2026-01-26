# Données
mac1 = "00:1A:2B:3C:4D:5E"
mac2 = "AA-BB-CC-DD-EE-FF"
mac3 = "001a2b3c4d5e"

# Analyse de mac1
print("--- MAC 1 ---")
print("Adresse:", mac1)
print("Type:", type(mac1))
print("Longueur de la chaîne:", len(mac1))  # 17 caractères

# Séparer les octets
octets1 = mac1.split(":")
print("Octets:", octets1)  # ['00', '1A', '2B', '3C', '4D', '5E']
print("Nombre d'octets:", len(octets1))  # 6

# Convertir en minuscules
mac1_lower = mac1.lower()
print("En minuscules:", mac1_lower)

# Analyse de mac2
print("\n--- MAC 2 ---")
print("Adresse:", mac2)
octets2 = mac2.split("-")
print("Octets:", octets2)

# Convertir en minuscules
mac2_lower = mac2.lower()
print("En minuscules:", mac2_lower)

# Uniformiser le format (remplacer - par :)
mac2_uniforme = mac2.replace("-", ":")
print("Format uniforme:", mac2_uniforme)

# Analyse de mac3 (sans séparateurs)
print("\n--- MAC 3 ---")
print("Adresse:", mac3)
print("Longueur:", len(mac3))  # 12 caractères

# Ajouter les séparateurs (prendre 2 caractères à la fois)
# Note: cette technique sera approfondie dans le chapitre sur les boucles
octets3 = []
for i in range(0, 12, 2):  # De 0 à 12, par pas de 2
    octets3.append(mac3[i:i+2])

mac3_formate = ":".join(octets3)
print("Formatée:", mac3_formate)

# Convertir en majuscules
mac3_upper = mac3_formate.upper()
print("En majuscules:", mac3_upper)

# Comparaison de formats
print("\n--- Uniformisation ---")
print("MAC 1:", mac1.lower().replace(":", ""))
print("MAC 2:", mac2.lower().replace("-", ""))
print("MAC 3:", mac3.lower())
print("Toutes sont maintenant en minuscules sans séparateurs")

# Résultats:
# MAC 1: 17 caractères, 6 octets séparés par ":"
# MAC 2: format avec "-", peut être converti en ":"
# MAC 3: 12 caractères, besoin d'ajouter des séparateurs
