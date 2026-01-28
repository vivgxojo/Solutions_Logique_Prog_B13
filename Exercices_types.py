# Exercice 2 : Convertir des tailles de fichiers

# Données (type int)
fichier1_bytes = 2048
fichier2_bytes = 5242880
fichier3_bytes = 1073741824

# Constantes de conversion
BYTES_PAR_KB = 1024
BYTES_PAR_MB = 1024 * 1024  # 1048576
BYTES_PAR_GB = 1024 * 1024 * 1024  # 1073741824

# Fichier 1
fichier1_kb = fichier1_bytes / BYTES_PAR_KB  # Résultat: float
fichier1_mb = fichier1_bytes / BYTES_PAR_MB
fichier1_gb = fichier1_bytes / BYTES_PAR_GB

print("--- Fichier 1 ---")
print("Taille:", fichier1_bytes, "bytes")
print("Taille:", fichier1_kb, "KB")
print("Taille:", fichier1_mb, "MB")
print("Taille:", fichier1_gb, "GB")

# Fichier 2
fichier2_kb = fichier2_bytes / BYTES_PAR_KB
fichier2_mb = fichier2_bytes / BYTES_PAR_MB
fichier2_gb = fichier2_bytes / BYTES_PAR_GB

print("\n--- Fichier 2 ---")
print("Taille:", fichier2_bytes, "bytes")
print("Taille:", round(fichier2_kb, 2), "KB")  # round() pour 2 décimales
print("Taille:", fichier2_mb, "MB")
print("Taille:", round(fichier2_gb, 2), "GB")

# Fichier 3
fichier3_kb = fichier3_bytes / BYTES_PAR_KB
fichier3_mb = fichier3_bytes / BYTES_PAR_MB
fichier3_gb = fichier3_bytes / BYTES_PAR_GB

print("\n--- Fichier 3 ---")
print("Taille:", fichier3_bytes, "bytes")
print("Taille:", round(fichier3_kb, 2), "KB")
print("Taille:", round(fichier3_mb, 2), "MB")
print("Taille:", fichier3_gb, "GB")
print()

# Résultats attendus:
# Fichier 1: 2048 bytes = 2.0 KB = 0.001953125 MB
# Fichier 2: 5242880 bytes = 5120.0 KB = 5.0 MB
# Fichier 3: 1073741824 bytes = 1048576.0 KB = 1024.0 MB = 1.0 GB


# Exercice 3 : Gérer les codes d'état HTTP

# Données (types mixtes)
code1 = 200  # int
code2 = "404"  # str
code3 = 500  # int
code4 = "301"  # str

# Affichage des types
print("Code 1:", code1, "- Type:", type(code1))
print("Code 2:", code2, "- Type:", type(code2))
print("Code 3:", code3, "- Type:", type(code3))
print("Code 4:", code4, "- Type:", type(code4))

# Conversion des chaînes en int
code2_int = int(code2)
code4_int = int(code4)

print("\nAprès conversion:")
print("Code 2:", code2_int, "- Type:", type(code2_int))
print("Code 4:", code4_int, "- Type:", type(code4_int))

# Déterminer la catégorie (diviser par 100 pour obtenir la centaine)
categorie1 = code1 // 100  # Division entière
categorie2 = code2_int // 100
categorie3 = code3 // 100
categorie4 = code4_int // 100

print("\nCatégories:")
print("Code 1 :", code1, "- Catégorie:", str(categorie1) + "xx (Succès)")
print("Code 2 :", code2, "- Catégorie:", str(categorie2) + "xx (Erreur client)")
print("Code 3 :", code3, "- Catégorie:", str(categorie3) + "xx (Erreur serveur)")
print("Code 4 :", code4, "- Catégorie:", str(categorie4) + "xx (Redirection)")
print()

# Résultats:
# Code 1: 200 (int) → catégorie 2xx
# Code 2: "404" (str) → 404 (int) → catégorie 4xx
# Code 3: 500 (int) → catégorie 5xx
# Code 4: "301" (str) → 301 (int) → catégorie 3xx


## Exercice 5 : Comprendre les types pour les numéros de VLAN

# Données (types mixtes)
vlan1 = 10
vlan2 = "20"
vlan3 = 100
vlan4 = "1005"

# Affichage des types originaux
print("--- Types originaux ---")
print("VLAN 1:", vlan1, "- Type:", type(vlan1))
print("VLAN 2:", vlan2, "- Type:", type(vlan2))
print("VLAN 3:", vlan3, "- Type:", type(vlan3))
print("VLAN 4:", vlan4, "- Type:", type(vlan4))

# Conversion en int si nécessaire
vlan2_int = int(vlan2)
vlan4_int = int(vlan4)

print("\n--- Après conversion ---")
print("VLAN 2:", vlan2_int, "- Type:", type(vlan2_int))
print("VLAN 4:", vlan4_int, "- Type:", type(vlan4_int))

# Validation (VLAN valides: 1-4094)
print("\n--- Validation ---")
vlan1_valide = vlan1 >= 1 and vlan1 <= 4094
vlan2_valide = vlan2_int >= 1 and vlan2_int <= 4094
vlan3_valide = vlan3 >= 1 and vlan3 <= 4094
vlan4_valide = vlan4_int >= 1 and vlan4_int <= 4094

print("VLAN", vlan1, "valide:", vlan1_valide)
print("VLAN", vlan2_int, "valide:", vlan2_valide)
print("VLAN", vlan3, "valide:", vlan3_valide)
print("VLAN", vlan4_int, "valide:", vlan4_valide)

# Vérifier si c'est un VLAN réservé
print("\n--- VLANs réservés ---")
vlan1_reserve = vlan1 == 1 or (vlan1 >= 1002 and vlan1 <= 1005)
vlan2_reserve = vlan2_int == 1 or (vlan2_int >= 1002 and vlan2_int <= 1005)
vlan3_reserve = vlan3 == 1 or (vlan3 >= 1002 and vlan3 <= 1005)
vlan4_reserve = vlan4_int == 1 or (vlan4_int >= 1002 and vlan4_int <= 1005)

print("VLAN", vlan1, "réservé:", vlan1_reserve)  # False
print("VLAN", vlan2_int, "réservé:", vlan2_reserve)  # False
print("VLAN", vlan3, "réservé:", vlan3_reserve)  # False
print("VLAN", vlan4_int, "réservé:", vlan4_reserve)  # True
print()

# Résultats:
# VLAN 1: 10 (int) → valide,  non réservé
# VLAN 2: "20" (str) → 20 (int) → valide,  non réservé
# VLAN 3: 100 (int) → valide,  non réservé
# VLAN 4: "1005" (str) → 1005 (int) → valide,  réservé
