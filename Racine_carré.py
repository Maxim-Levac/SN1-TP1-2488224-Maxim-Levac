
def racine(nombre, decimal):
    premier_chiffre = 0
    # Combien de décimal
    for i in range(decimal):
        chiffre_trouver = False
        chiffre = 0

        # Trouver décimal
        while not chiffre_trouver:

            nouveau_chiffre = premier_chiffre + (chiffre * (0.1) ** i)

            if nouveau_chiffre ** 2 >= nombre:
                nouveau_chiffre = premier_chiffre + ((chiffre-1) * (0.1) ** i)
                premier_chiffre = nouveau_chiffre
                chiffre_trouver = True

            else:
                chiffre += 1

    print(str(premier_chiffre))


racine(8, 14)