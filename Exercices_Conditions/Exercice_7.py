# Programme de recommandation de protocole de routage

print("=== RECOMMANDATION DE PROTOCOLE DE ROUTAGE ===\n")

# Entrées
taille = int(input("Taille du réseau (nombre de routeurs) : "))
complexite = input("Complexité du réseau (simple/moyenne/élevée) : ").lower()
convergence = input("Besoins de convergence (lente/rapide/très rapide) : ").lower()

# Variable pour stocker le protocole recommandé
protocole = ""

# Logique de recommandation
if taille < 15:
    if complexite == "simple" and convergence == "lente":
        protocole = "RIP"
    elif convergence == "rapide" or convergence == "très rapide":
        protocole = "OSPF"
    else:
        protocole = "OSPF"

elif taille >= 15 and taille < 200:
    if convergence == "très rapide":
        protocole = "EIGRP"
    elif convergence == "rapide":
        protocole = "OSPF"
    else:
        protocole = "OSPF"

elif taille >= 200:
    if complexite == "élevée" and convergence == "très rapide":
        protocole = "EIGRP"
    elif complexite == "élevée":
        protocole = "IS-IS"
    else:
        protocole = "OSPF"

else:
    protocole = "OSPF"

# Sortie
print("\n--- RECOMMANDATION ---")
print(f"Protocole recommandé : {protocole}")
print("\n=== FIN ===")