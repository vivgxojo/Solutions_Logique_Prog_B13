# Demander le type de trafic à l'utilisateur
print("=== Détermination de la priorité QoS ===")
print("\nTypes de trafic disponibles :")
print("1. Contrôle réseau")
print("2. Voix (VoIP)")
print("3. Vidéo en temps réel (vidéoconférence)")
print("4. Streaming vidéo")
print("5. Données critiques (transactions)")
print("6. Données standard (navigation web)")
print("7. Trafic de fond (téléchargements)")
print("8. Sauvegardes, mises à jour")

choix = int(input("\nEntrez le numéro du type de trafic : "))

# Déterminer la priorité et les paramètres
if choix == 1:
    priorite = "Priorité 7 (Critique) : Contrôle réseau"
    parametres = "Latence max : < 10 ms | Bande passante : Variable"
elif choix == 2:
    priorite = "Priorité 6 (Très haute) : Voix (VoIP)"
    parametres = "Latence max : < 30 ms | Gigue max : < 10 ms | Perte paquets : < 1%"
elif choix == 3:
    priorite = "Priorité 5 (Haute) : Vidéo en temps réel (vidéoconférence)"
    parametres = "Latence max : < 100 ms | Gigue max : < 30 ms | Perte paquets : < 1%"
elif choix == 4:
    priorite = "Priorité 4 (Moyenne-haute) : Streaming vidéo"
    parametres = "Latence max : < 200 ms | Perte paquets : < 2%"
elif choix == 5:
    priorite = "Priorité 3 (Moyenne) : Données critiques (transactions)"
    parametres = "Latence max : < 500 ms | Fiabilité importante"
elif choix == 6:
    priorite = "Priorité 2 (Basse) : Données standard (navigation web)"
    parametres = "Pas de contrainte stricte"
elif choix == 7:
    priorite = "Priorité 1 (Très basse) : Trafic de fond (téléchargements)"
    parametres = "Best effort"
elif choix == 8:
    priorite = "Priorité 0 (Background) : Sauvegardes, mises à jour"
    parametres = "Pas de garantie"
else:
    priorite = "Erreur : Type invalide"
    parametres = "N/A"

# Afficher les résultats
print("\n" + "="*50)
print(priorite)
print(parametres)
print("="*50)
