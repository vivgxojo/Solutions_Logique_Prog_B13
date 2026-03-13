import random

print("Heure   Utilisation (Mbps)")
print("-" * 30)

total = 0
for heure in range(24):
    utilisation = round(random.uniform(10.0, 1000.0), 2)
    total += utilisation
    if heure < 10:
        heure_str = "0" + str(heure) + "h"
    else:
        heure_str = str(heure) + "h"
    print(heure_str + "      " + str(utilisation) + " Mbps")

moyenne = round(total / 24, 2)
print("-" * 30)
print("Moyenne sur 24h : " + str(moyenne) + " Mbps")