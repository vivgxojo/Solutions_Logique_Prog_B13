
for i in range(0, 8): # 0-7

    # Entrées
    difficulte = int(input(f"Entrez le niveau de difficulté pour un message de sévérité {i} : "))

    if difficulte == 0:
        print("Erreur")
    else:
        # Calcul de la priorité
        priority = 8 / difficulte + i # i = sévérité
        delai = 15 * priority

        # Affichage des détails
        print(f"Priorité    : {priority:.0f}")
        print(f"Délai       : {delai:.0f} minutes")
        print()