
def racine_nombre_par_nombre(nombre, decimal):
    """

    :param nombre:
    :param decimal:
    :return:
    """

    #S'assurer que l'entrée est un chiffre et positif
    try:
        nombre1 = int(nombre)
        decimal2 = int(decimal)
    except ValueError:
        print("Entrer un chiffre")
        return None
    if nombre < 0 or decimal < 0:
        raise ValueError("La racine d'un nombre négatif est impossible, s'il vous plaît insérer un chiffre positif")

    premier_chiffre = 0
    #Combien de décimal
    for i in range(decimal):
        chiffre_trouver = False
        chiffre = 0

        # Trouver décimal
        while not chiffre_trouver:
            #Nouveau chiffre haut et bas à tester
            nouveau_chiffre_haut = (premier_chiffre + (chiffre * (0.1) ** i))
            nouveau_chiffre_bas = (premier_chiffre + ((chiffre-1) * (0.1) ** i))

            #vérificer si le chiffre du haut est égale au nombre
            if nouveau_chiffre_haut ** 2 == nombre:
                premier_chiffre = nouveau_chiffre_haut
                break
            # vérifier si les deux chiffres sont entre le vrai chiffre
            if nouveau_chiffre_haut ** 2 >= nombre and nouveau_chiffre_bas ** 2 <= nombre:
                premier_chiffre = nouveau_chiffre_bas
                chiffre_trouver = True

            else:
                chiffre += 1

    return(premier_chiffre)

def racine_dichotomie(chiffre):
    if chiffre >= 1:
        bas = 0
        haut = chiffre
    if 0 < chiffre < 1:
        bas = chiffre
        haut = 1
    while True:
        milieu  = (bas + haut) / 2
        if milieu ** 2 < chiffre:
            bas = milieu
        if milieu ** 2 > chiffre:
            haut = milieu
        if haut - bas < (10 ** ):
            break
    print((haut + bas)/2)
racine_dichotomie(8)