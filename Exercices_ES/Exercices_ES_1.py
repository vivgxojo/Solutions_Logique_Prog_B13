# Exercice 1 : Demander une adresse IP et un masque, afficher les infos réseau

# Demander les données à l'utilisateur
adresse_ip = input("Entrez l'adresse IP : ")
cidr = int(input("Entrez le masque CIDR (ex: 24) : "))

# Calculs
bits_reseau = cidr
bits_hotes = 32 - cidr
nb_adresses_total = 2 ** bits_hotes
nb_hotes_utilisables = nb_adresses_total - 2

# Affichage des résultats
print("===== INFORMATIONS RÉSEAU =====")
print("Bits réseau :", bits_reseau)
print("Bits hôtes :", bits_hotes)
print("Nombre total d'adresses :", nb_adresses_total)
print("Nombre d'hôtes utilisables :", nb_hotes_utilisables)

# Exemple d'exécution :
# Entrez l'adresse IP : 192.168.10.50
# Entrez le masque CIDR : 24
# ===== INFORMATIONS RÉSEAU =====
# Bits réseau : 24
# Bits hôtes : 8
# Nombre total d'adresses : 256
# Nombre d'hôtes utilisables : 254
