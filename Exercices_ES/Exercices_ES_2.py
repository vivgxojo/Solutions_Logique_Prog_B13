# Exercice 2 : Saisir la vitesse de connexion et calculer le débit théorique et le temps de téléchargement

# Demander la vitesse de connexion
vitesse_mbps = float(input("Entrez la vitesse de connexion (Mbps) : "))

# Calcul du débit théorique en MB/s
debit_mbs = vitesse_mbps / 8

# Tailles de fichiers à tester (en MB)
fichier_100mb = 100
fichier_1gb = 1024  # 1 GB = 1024 MB
fichier_5gb = 5120  # 5 GB = 5120 MB

# Calcul des temps de téléchargement
temps_100mb_sec = fichier_100mb / debit_mbs
temps_1gb_sec = fichier_1gb / debit_mbs
temps_5gb_sec = fichier_5gb / debit_mbs

# Conversion en minutes
temps_100mb_min = temps_100mb_sec / 60
temps_1gb_min = temps_1gb_sec / 60
temps_5gb_min = temps_5gb_sec / 60

# Affichage
print("\n===== DÉBIT THÉORIQUE =====")
print("Vitesse de connexion :", vitesse_mbps, "Mbps")
print("Débit théorique :", debit_mbs, "MB/s")

print("\n===== TEMPS DE TÉLÉCHARGEMENT =====")
print("Fichier de 100 MB :")
print("  -", round(temps_100mb_sec, 2), "secondes")
print("  -", round(temps_100mb_min, 2), "minutes")

print("Fichier de 1 GB :")
print("  -", round(temps_1gb_sec, 2), "secondes")
print("  -", round(temps_1gb_min, 2), "minutes")

print("Fichier de 5 GB :")
print("  -", round(temps_5gb_sec, 2), "secondes")
print("  -", round(temps_5gb_min, 2), "minutes")

# Exemple d'exécution avec 100 Mbps :
# Débit théorique : 12.5 MB/s
# 100 MB : 8.0 secondes
# 1 GB : 81.92 secondes (1.37 minutes)
# 5 GB : 409.6 secondes (6.83 minutes)
