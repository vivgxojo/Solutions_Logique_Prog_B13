# Demander le numéro de port à l'utilisateur
port = int(input("Entrez un numéro de port (0-65535) : "))

# Vérifier la validité du port et déterminer la catégorie
if port < 0:
    categorie = "Erreur : Le numéro de port ne peut pas être négatif."
elif port > 65535:
    categorie = "Erreur : Le numéro de port ne peut pas dépasser 65535."
elif port <= 1023:
    categorie = "Ports bien connus"
elif port <= 49151:
    categorie = "Ports enregistrés"
else:
    categorie = "Ports dynamiques/privés"

# Afficher le résultat
print(f"Le port {port} appartient à la catégorie : {categorie}")