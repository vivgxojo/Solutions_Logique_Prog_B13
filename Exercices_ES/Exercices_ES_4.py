# Exercice 4 : Calculer le coût mensuel d'une bande passante louée

# Demander les informations
bande_passante = float(input("Entrez la bande passante requise (Mbps) : "))
tarif_par_mbps = float(input("Entrez le tarif par Mbps ($) : "))

# Frais d'installation
frais_installation = 500

# Calcul du coût de base
cout_base = bande_passante * tarif_par_mbps

# Calcul des taxes (TPS + TVQ au Québec)
taux_taxes = 14.975  # 5% TPS + 9.975% TVQ
cout_total_mensuel = cout_base * (1 + taux_taxes)

# Affichage du rapport
print("===== RAPPORT DE COÛTS =====")
print(f"Frais d'installation : {frais_installation:.2f}$")
print(f"Coût de base : {cout_base:.2f}$")
print("Taxes", str(taux_taxes) + "%")
print(f"COÛT TOTAL MENSUEL : {cout_total_mensuel:.2f}$")

# Exemple d'exécution :
# Entrez la bande passante requise (Mbps) : 600
# Entrez le tarif par Mbps ($) : 8
# ===== RAPPORT DE COÛTS =====
# Frais d'installation : 500.00 $
# Coût de base : 4800.00 $
# Taxes 14.975%
# COÛT TOTAL MENSUEL : 76680.00 $