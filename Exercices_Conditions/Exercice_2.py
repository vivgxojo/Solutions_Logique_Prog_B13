# Demander la distance et le débit à l'utilisateur
distance = float(input("Entrez la distance en mètres : "))
debit = float(input("Entrez le débit souhaité en Gbps : "))

# Déterminer le type de câble
if 0 < distance <= 100:
    if debit == 1:
        type_cable = "Câble cuivre Cat5e"
    elif debit == 10:
        type_cable = "Câble cuivre Cat6"
    elif 10 < debit <= 40:
        type_cable = "Câble cuivre Cat6a/Cat7"
    else:
        type_cable = "Aucun câble approprié pour ces paramètres"
elif 100 < distance <= 550 and 1 < debit <= 100:
    type_cable = "Fibre optique multimode"
elif distance > 550 and debit > 100:
    type_cable = "Fibre optique monomode"
else:
    type_cable = "Aucun câble approprié pour ces paramètres"

# Afficher le résultat
print(f"Type de câble recommandé : {type_cable}")
