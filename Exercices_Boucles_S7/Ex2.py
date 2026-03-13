print("=== Ports bien connus (10 premiers) ===")
for port in range(0, 10):
    print("Port : " + str(port))

print("=== Ports enregistrés (10 premiers) ===")
for port in range(1024, 1034):
    print("Port : " + str(port))

print("=== Ports dynamiques (10 premiers) ===")
for port in range(49152, 49162):
    print("Port : " + str(port))