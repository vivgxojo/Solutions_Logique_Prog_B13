# Données IP 1, IP 2 et IP 3 :
ip1 = "192.168.1.100" # Concept : Type str car entre guillemets
ip2 = "10.0.0.1"
ip3 = "172.16.254.1"

# Étape 1: Afficher le type de la variable IP
print("Type de ip1:", type(ip1)) # Concept : Type str affiché.

# Étape 2 : Séparer l'IP en octets
octets = ip1.split(".") # Concept : Méthode .split()
print("Octets de", ip1, ":", octets)  # Question 1 : Comment ça marche .split(), pourquoi le résultat est entre [ ] ?
print("Type de octets:", type(octets)) # Concept : Type list

# Étape 3 : Afficher le premier et le dernier octet
premier_octet = octets[0] # Question 2 : Pourquoi on met [0] et [3] ?
dernier_octet = octets[3]
print("Premier octet:", premier_octet)  # Concept : Type str (on voit les guillemets seulement lors du débogage : '192')
print("Dernier octet:", dernier_octet)  #

# Étape 4 : Convertir en entier
dernier_octet_int = int(dernier_octet)              # Concept : Type int
print("Dernier octet en int:", dernier_octet_int)   # Concept : Type int
print("Type:", type(dernier_octet_int))             # Concept : Type int

# Étape 4 : Vérifier si pair (utilise l'opérateur modulo %)
est_pair = dernier_octet_int % 2 == 0
print("Le dernier octet est pair:", est_pair)  # True

# Mêmes choses pour ip2 et ip3...
print("\n--- IP2 ---")
octets2 = ip2.split(".") # 2. .split() --> Type list
print("Dernier octet de", ip2, ":", octets2[3]) # 3. Type str dans la liste
est_pair2 = int(octets2[3]) % 2 == 0 # 4. Type int
print("Est pair:", est_pair2)

print("\n--- IP3 ---")
octets3 = ip3.split(".")
print("Dernier octet de", ip3, ":", octets3[3])
est_pair3 = int(octets3[3]) % 2 == 0
print("Est pair:", est_pair3)