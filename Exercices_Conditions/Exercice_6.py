# Entrées
facility = int(input("Entrez le numéro de Facility: "))
severity = int(input("Entrez le numéro de Severity: "))

# Calcul de la priorité
priority = (facility * 8) + severity

# Détermination du délai et action selon le severity
if severity == 0:
    delai = "Immédiat"
    action = "Immédiate"
elif severity == 1:
    delai = "< 15 min"
    action = "Urgente"
elif severity == 2:
    delai = "< 1 heure"
    action = "Haute priorité"
elif severity == 3:
    delai = "< 4 heures"
    action = "Corriger"
elif severity == 4:
    delai = "< 1 jour"
    action = "Surveiller"
elif severity == 5:
    delai = "Inconnu"
    action = "Informationnel"
elif severity == 6:
    delai = "Inconnu"
    action = "Log seulement"
elif severity == 7:
    delai = "Inconnu"
    action = "Développement"
else:
    delai = "N/A"
    action = "N/A"

# Affichage des détails
print("DÉTAILS:")
print(f"PRIORITÉ CALCULÉE: {priority}")
print(f"Délai        : {delai}")
print(f"Action       : {action}")
print()
print("=" * 60)