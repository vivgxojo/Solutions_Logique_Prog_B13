octet1 = int(input("Entrez le premier nombre de l'adresse IP : "))
octet2 = int(input("Entrez le deuxième nombre de l'adresse IP : "))
octet3 = int(input("Entrez le troisième nombre de l'adresse IP : "))
octet4 = int(input("Entrez le dernier nombre de l'adresse IP : "))

if octet1 < 0 or octet1 > 255:
    valide = False
if octet2 < 0 or octet2 > 255:
    valide = False
if octet3 < 0 or octet3 > 255:
    valide = False
if octet4 < 0 or octet4 > 255:
    valide = False
else:
    valide = True

if valide:
    print("L'adressse ip "+ str(octet1)+ "."+ str(octet2)+ "." +str(octet3)+"."+ str(octet4) +" est valide.")
else:
    print("L'adressse ip " +str(octet1) +"."+ str(octet2)+ "." +str(octet3)+"."+ str(octet4)+ " n'est pas valide.")

"""
valide = True
RÉPÉTER 4 FOIS
    DEMANDER octet
    SI octet < 0 OU octet > 255
        non valide
AFFICHER Valide
"""
valide = True
for i in range(4):
    octet = int(input("Entrez l'octet " + str(i + 1) + " de l'adresse IP : "))
    if octet < 0 or octet > 255:
        valide = False

print("L'adresse est valide :", valide)