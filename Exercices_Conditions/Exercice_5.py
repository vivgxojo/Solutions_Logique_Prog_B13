# Programme d'analyse d'utilisation CPU du routeur

print("===== ANALYSE D'UTILISATION CPU DU ROUTEUR =====\n")

# Collecter les données
cpu = float(input("Entrez l'utilisation CPU actuelle (%) : "))
duree = int(input("Depuis combien de minutes le CPU est-il élevé ? : "))
heure = int(input("Heure actuelle (0-23) : "))
print("\nType de routeur :")
print("1. Edge (accès)")
print("2. Core (cœur de réseau)")
print("3. Distribution")
routeur = int(input("Choisissez le type (1-3) : "))
nb_alertes = int(input("Nombre d'alertes dans les dernières 24h : "))

# Déterminer le niveau de base
if cpu <= 60:
    niveau = 1
elif cpu <= 75:
    niveau = 2
elif cpu <= 85:
    niveau = 3
elif cpu <= 95:
    niveau = 4
else:
    niveau = 5

# Aggravations
if duree > 30:
    niveau = niveau + 1
if (heure >= 8 and heure <= 11) or (heure >= 14 and heure <= 17):
    niveau = niveau + 1
if routeur == 2:
    niveau = niveau + 1
if nb_alertes >= 5:
    niveau = niveau + 1

if niveau == 1 :
    alerte = "Normal : 0-60% → Aucune alerte"
elif niveau == 2 :
    alerte = "Avertissement : 61-75% → Alerte jaune, surveiller"
elif niveau == 3 :
    alerte = "Attention : 76-85% → Alerte orange, investigation requise"
elif niveau == 4 :
    alerte = "Critique : 86-95% → Alerte rouge, action immédiate"
else :
    alerte = "Urgence : 96-100% → Alerte critique, risque de panne"

# Afficher les résultats
print("\n" + "="*60)
print("ALERTE")
print("="*60)
print(alerte)
print("\n" + "="*60)
