# On demande l'adresse IP à l'utilisateur
ip = input("Entrez une adresse IP (ex: 192.168.1.10) : ")

# On découpe la chaîne en morceaux en utilisant le point comme séparateur
octets = ip.split(".")

# On affiche chaque octet un par un avec une boucle
print("\n--- Analyse de l'adresse IP ---")
numero = 1
for octet in octets:
    print("Octet", numero, ":", octet)
    numero = numero + 1

# On calcule la somme des 4 octets (conversion en entier nécessaire)
somme = int(octets[0]) + int(octets[1]) + int(octets[2]) + int(octets[3])
print("Somme des octets :", somme)