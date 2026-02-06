# Exercice 5 : Créer un rapport formaté de performance réseau

# Collecte des données
print("===== OUTIL DE RAPPORT DE PERFORMANCE RÉSEAU =====\n")
nom_site = input("Nom du site/client : ")
adresse_ip = input("Adresse IP testée : ")
vitesse_download = float(input("Vitesse de téléchargement (Mbps) : "))
vitesse_upload = float(input("Vitesse de téléversement (Mbps) : "))
latence = float(input("Latence moyenne (ms) : "))
perte_paquets = float(input("Perte de paquets (%) : "))
date_test = input("Date du test (JJ/MM/AAAA) : ")

# Calculs
debit_download_mbs = vitesse_download / 8
debit_upload_mbs = vitesse_upload / 8
# Score de qualité
score = 100 - (latence / 2) - (perte_paquets * 10)

# Génération du rapport
print()
print("="*60)
print(" "*15 + "RAPPORT DE PERFORMANCE RÉSEAU")
print("="*60)
print("\n--- INFORMATIONS GÉNÉRALES ---")
print("Site/Client       :", nom_site)
print("Adresse IP testée :", adresse_ip)
print("Date du test      :", date_test)

print("\n--- RÉSULTATS DES TESTS ---")
print("Vitesse téléchargement : ", vitesse_download, "Mbps (", round(debit_download_mbs, 2), "MB/s )")
print("Vitesse téléversement  : ", vitesse_upload, "Mbps (", round(debit_upload_mbs, 2), "MB/s )")
print("Latence moyenne        : ", latence, "ms")
print("Perte de paquets       : ", perte_paquets, "%")

print("\n--- ÉVALUATION ---")
print("Score de qualité       : ", round(score, 1), "/ 100")

print()
print("="*60)
print("Fin du rapport")
print("="*60)

# Exemple d'exécution :
# Site : Succursale Montréal
# IP : 192.168.100.50
# Download : 250 Mbps (31.25 MB/s)
# Upload : 100 Mbps (12.5 MB/s)
# Latence : 25 ms
# Perte : 0.5%
# Score : 82.5 / 100