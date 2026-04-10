dns_servers = []

print("=== Gestionnaire de serveurs DNS ===")
print("Entrez vos serveurs DNS (tapez 'fin' pour arrêter) :")

continuer = True
while continuer:
    serveur = input("Adresse du serveur DNS : ")
    if serveur == "fin":
        continuer = False
    else:
        dns_servers.append(serveur)
        print("Serveur ajouté.")

print("\n--- Serveurs DNS enregistrés ---")
if len(dns_servers) == 0:
    print("Aucun serveur enregistré.")
else:
    i = 0
    while i < len(dns_servers):
        print(str(i + 1) + ". " + dns_servers[i])
        i = i + 1

a_supprimer = input("\nEntrez l'adresse du serveur à supprimer : ")

if a_supprimer in dns_servers:
    dns_servers.remove(a_supprimer)
    print("Serveur supprimé.")
else:
    print("Erreur : ce serveur n'est pas dans la liste.")

print("\n--- Liste finale ---")
if len(dns_servers) == 0:
    print("La liste est vide.")
else:
    i = 0
    while i < len(dns_servers):
        print(str(i + 1) + ". " + dns_servers[i])
        i = i + 1