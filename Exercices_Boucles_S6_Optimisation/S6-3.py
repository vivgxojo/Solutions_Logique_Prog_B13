nb = int(input("Combien de fichiers veux-tu convertir? "))
for i in range(nb):

    print()
    # Données (type int)
    fichier1_bytes = int(input("Entrez le nombre de bytes: "))

    # Constantes de conversion
    BYTES_PAR_KB = 1024
    BYTES_PAR_MB = 1024 * 1024  # 1048576
    BYTES_PAR_GB = 1024 * 1024 * 1024  # 1073741824

    # Fichier 1
    fichier1_kb = fichier1_bytes / BYTES_PAR_KB  # Résultat: float
    fichier1_mb = fichier1_bytes / BYTES_PAR_MB
    fichier1_gb = fichier1_bytes / BYTES_PAR_GB

    print("--- Fichier 1 ---")
    print("Taille:", fichier1_bytes, "bytes")
    print("Taille:", fichier1_kb, "KB")
    print("Taille:", fichier1_mb, "MB")
    print("Taille:", fichier1_gb, "GB")

    # Résultats attendus:
    # Fichier 1: 2048 bytes = 2.0 KB = 0.001953125 MB
    # Fichier 2: 5242880 bytes = 5120.0 KB = 5.0 MB
    # Fichier 3: 1073741824 bytes = 1048576.0 KB = 1024.0 MB = 1.0 GB
