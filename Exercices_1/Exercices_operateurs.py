# Exercice 1 : Calculer la bande passante disponible
# Données
bande_totale = 1000  # Mbps
bande_utilisee = 673  # Mbps

# Calculs
bande_disponible = bande_totale - bande_utilisee
pourcentage_utilisation = bande_utilisee * 100 / bande_totale

# Affichage
print("Bande passante totale:", bande_totale, "Mbps")
print("Bande passante utilisée:", bande_utilisee, "Mbps")
print("Bande passante disponible:", bande_disponible, "Mbps")
print("Pourcentage d'utilisation:", pourcentage_utilisation, "%")
print()

# Résultat attendu:
# Bande passante disponible: 327 Mbps
# Pourcentage d'utilisation: 67.3 %

# Exercice 2 : Convertir des vitesses de transfert (Mbps → MB/s)
# Données
vitesse_mbps_1 = 100
vitesse_mbps_2 = 500
vitesse_mbps_3 = 1000

# Conversion (diviser par 8 car 1 octet = 8 bits)
vitesse_mbs_1 = vitesse_mbps_1 / 8
vitesse_mbs_2 = vitesse_mbps_2 / 8
vitesse_mbs_3 = vitesse_mbps_3 / 8

# Affichage
print(vitesse_mbps_1, "Mbps =", vitesse_mbs_1, "MB/s")
print(vitesse_mbps_2, "Mbps =", vitesse_mbs_2, "MB/s")
print(vitesse_mbps_3, "Mbps =", vitesse_mbs_3, "MB/s")
print()

# Résultats attendus:
# 100 Mbps = 12.5 MB/s
# 500 Mbps = 62.5 MB/s
# 1000 Mbps = 125.0 MB/s

# Exercice 3 : Calculer le temps de téléchargement d'un fichier
# Données
taille_fichier_gb = 4.7  # GB
vitesse_mbps = 50  # Mbps

# Conversions
taille_fichier_mb = taille_fichier_gb * 1024  # GB en MB
vitesse_mbs = vitesse_mbps / 8  # Mbps en MB/s

# Calcul du temps
temps_secondes = taille_fichier_mb / vitesse_mbs
temps_minutes = temps_secondes / 60

# Affichage
print("Taille du fichier:", taille_fichier_gb, "GB =", taille_fichier_mb, "MB")
print("Vitesse de téléchargement:", vitesse_mbps, "Mbps =", vitesse_mbs, "MB/s")
print("Temps de téléchargement:", temps_secondes, "secondes")
print("Temps de téléchargement:", temps_minutes, "minutes")
print("Temps de téléchargement:", round(temps_minutes, 2), "minutes")
print()

# Résultats attendus:
# Taille du fichier: 4812.8 MB
# Vitesse: 6.25 MB/s
# Temps: 770.048 secondes ≈ 12.83 minutes

# Exercice 4 : Déterminer si un numéro de port est valide
# Données
port1 = 80
port2 = 65535
port3 = 70000
port4 = -5
port5 = 22

# Vérification (un port valide: 0 <= port <= 65535)
port1_valide = port1 >= 0 and port1 <= 65535
port2_valide = port2 >= 0 and port2 <= 65535
port3_valide = port3 >= 0 and port3 <= 65535
port4_valide = port4 >= 0 and port4 <= 65535
port5_valide = port5 >= 0 and port5 <= 65535

# Affichage
print("Port", port1, "valide:", port1_valide)
print("Port", port2, "valide:", port2_valide)
print("Port", port3, "valide:", port3_valide)
print("Port", port4, "valide:", port4_valide)
print("Port", port5, "valide:", port5_valide)
print()

# Résultats attendus:
# Port 80 valide: True
# Port 65535 valide: True
# Port 70000 valide: False
# Port -5 valide: False
# Port 22 valide: True

# Exercice 5 : Calculer le nombre d'hôtes disponibles dans un sous-réseau
# Données
cidr1 = 24
cidr2 = 25
cidr3 = 26
cidr4 = 30

# Calculs (formule: 2^(32-CIDR) - 2)
nb_hotes1 = 2**(32 - cidr1) - 2
nb_hotes2 = 2**(32 - cidr2) - 2
nb_hotes3 = 2**(32 - cidr3) - 2
nb_hotes4 = 2**(32 - cidr4) - 2

# Affichage
print("Sous-réseau /" + str(cidr1), ":", nb_hotes1, "hôtes disponibles")
print("Sous-réseau /" + str(cidr2), ":", nb_hotes2, "hôtes disponibles")
print("Sous-réseau /" + str(cidr3), ":", nb_hotes3, "hôtes disponibles")
print("Sous-réseau /" + str(cidr4), ":", nb_hotes4, "hôtes disponibles")
print()

# Résultats attendus:
# Sous-réseau /24: 254 hôtes disponibles
# Sous-réseau /25: 126 hôtes disponibles
# Sous-réseau /26: 62 hôtes disponibles
# Sous-réseau /30: 2 hôtes disponibles