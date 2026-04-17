# On demande le nom complet à l'utilisateur
fqdn = input("Entrez un FQDN (ex: router1.montreal.example.com) : ")

# On découpe selon les points
parties = fqdn.split(".")

# Le hostname est le premier élément
hostname = parties[0]

# Le domaine est tout ce qui suit le premier point
domaine = ".".join(parties[1:])

# Le nombre de niveaux = nombre de parties
niveaux = len(parties)

print("\n--- Décomposition du FQDN ---")
print("FQDN complet :", fqdn)
print("Hostname     :", hostname)
print("Domaine      :", domaine)
print("Niveaux      :", niveaux)

# On vérifie si c'est un nom court ou long
if niveaux >= 4:
    print("→ Nom de domaine complet (4 niveaux ou plus)")
else:
    print("→ Nom de domaine court")