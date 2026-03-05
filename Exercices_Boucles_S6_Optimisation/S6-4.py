# Exercice 4 : Gérer les codes d'état HTTP

while True:
    code1 = int(input("Entre un code http: "))

    categorie1 = code1 // 100  # Division entière

    print("Catégorie:", categorie1)

    if categorie1 == 2:
        print("Succès")
    elif categorie1 == 3:
        print("Redirection")
    elif categorie1 == 4:
        print("Erreur client")
    elif categorie1 == 5:
        print("Erreur serveur")

    continuer = bool(input("Veux-tu continuer? "))
    if not continuer: # if continuer == False
        break
