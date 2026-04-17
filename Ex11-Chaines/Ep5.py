# Liste de noms d'interfaces à normaliser
interfaces = [
    "GigabitEthernet0/0",
    "GigabitEthernet0/1",
    "FastEthernet1/0",
    "Serial0/0/0",
    "Gi0/2",
    "Fa2/1",
]

print("--- Normalisation des interfaces ---")
print(f"{'Nom original':<22} {'Nom normalisé':<12} {'Type'}")
print("-" * 50)

for interface in interfaces:
    # On remplace les noms longs par les abréviations
    nom_norm = interface.replace("GigabitEthernet", "Gi")
    nom_norm = nom_norm.replace("FastEthernet", "Fa")
    nom_norm = nom_norm.replace("Serial", "Se")

    # On détermine le type selon le début du nom normalisé
    if nom_norm.startswith("Gi"):
        type_if = "Gigabit"
    elif nom_norm.startswith("Fa"):
        type_if = "Fast"
    else:
        type_if = "Autre"

    print(f"{interface:<22} {nom_norm:<12} {type_if}")