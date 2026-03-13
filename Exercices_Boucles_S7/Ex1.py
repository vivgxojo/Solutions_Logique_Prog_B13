octet1 = 192
octet2 = 168
octet3 = 1
octet4_base = 0

print("Adresses du sous-réseau 192.168.1.0/29 :")
for i in range(8):
    print(str(octet1) + "." + str(octet2) + "." + str(octet3) + "." + str(octet4_base + i))