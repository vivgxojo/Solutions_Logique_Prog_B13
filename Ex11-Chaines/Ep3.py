lignes = [
    "GigabitEthernet0/0  192.168.1.1   YES  manual  up    up",
    "GigabitEthernet0/1  10.0.0.1      YES  manual  up    up",
    "GigabitEthernet0/2  unassigned    YES  unset   down  down",
    "Loopback0           172.16.0.1    YES  manual  up    up",
]

print("--- État des interfaces ---")
print(f"{'Interface':<25} {'IP':<18} {'État'}")
print("-" * 55)

for ligne in lignes:
    # On découpe la ligne en morceaux (séparés par des espaces)
    parties = ligne.split()

    interface = parties[0]
    ip        = parties[1]
    etat_line = parties[-1]  # dernier mot = état de la ligne

    if etat_line == "up":
        etat = "Active"
    else:
        etat = "Inactive"

    print(f"{interface:<25} {ip:<18} {etat}")