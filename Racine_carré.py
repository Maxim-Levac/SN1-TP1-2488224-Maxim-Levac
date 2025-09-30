import random
import time
import math


def racine_nombre_par_nombre(nombre, decimal):
    """
    Trouver la racine carrée d'un chiffre à l'aide de la méthode nombre par nombre
    Paramètres :
    nombre (float) : Nombre à calculer la racine carrée
    decimal (int) : Nombre de décimal à calculée

    Retourne :
    float : racine carrée du chiffre

    Exemple d'utilisation :
    >>> racine_nombre_par_nombre(3, 2)
    1.7
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

    return(round(premier_chiffre, decimal))

def racine_dichotomie(chiffre):
    """
    Trouver la racine carrée d'un chiffre à l'aide de la méthode dichotomie
    Paramètres :
    nombre (float) : Nombre à calculer la racine carrée

    Retourne :
    float : racine carrée du chiffre

    Exemple d'utilisation :
    >>> racine_dichotomie(3)
    1.7318115234375
    """
    #S'assurer que l'entrée est un chiffre et positif
    try:
        nombre1 = int(chiffre)
    except ValueError:
        print("Entrer un chiffre")
        return None
    if chiffre < 0:
        raise ValueError("La racine d'un nombre négatif est impossible, s'il vous plaît insérer un chiffre positif")
    #vérifier si le chiffre est plus grand ou plus petit que 1
    if chiffre >= 1:
        bas = 0
        haut = chiffre
    if 0 < chiffre < 1:
        bas = chiffre
        haut = 1
    #début de méthode de dichotomie
    while True:
        milieu  = (bas + haut) / 2
        if milieu ** 2 < chiffre:
            bas = milieu
        if milieu ** 2 > chiffre:
            haut = milieu
        if haut - bas < (0.001):
            break
    return((haut + bas)/2)



def racine_nombre_par_nombre_n(nombre, decimal, n):
    """
    Trouver la racine carrée d'un chiffre à l'aide de la méthode nombre par nombre
    Paramètres :
    nombre (float) : Nombre à calculer la racine carrée
    decimal (int) : Nombre de décimal à calculée
    n (float) : nieme racine

    Retourne :
    float : racine carrée du chiffre

    Exemple d'utilisation :
    >>> racine_nombre_par_nombre(3, 2)
    1.7
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
            if nouveau_chiffre_haut ** n == nombre:
                premier_chiffre = nouveau_chiffre_haut
                break
            # vérifier si les deux chiffres sont entre le vrai chiffre
            if nouveau_chiffre_haut ** n >= nombre and nouveau_chiffre_bas ** n <= nombre:
                premier_chiffre = nouveau_chiffre_bas
                chiffre_trouver = True

            else:
                chiffre += 1

    return(round(premier_chiffre, decimal))


def racine_dichotomie_n(chiffre, n):
    """
    Trouver la racine carrée d'un chiffre à l'aide de la méthode dichotomie
    Paramètres :
    nombre (float) : Nombre à calculer la racine carrée
    n (float): nieme racine

    Retourne :
    float : racine carrée du chiffre

    Exemple d'utilisation :
    >>> racine_dichotomie(3)
    1.7318115234375
    """
    #S'assurer que l'entrée est un chiffre et positif
    try:
        nombre1 = int(chiffre)
    except ValueError:
        print("Entrer un chiffre")
        return None
    if chiffre < 0:
        raise ValueError("La racine d'un nombre négatif est impossible, s'il vous plaît insérer un chiffre positif")
    #vérifier si le chiffre est plus grand ou plus petit que 1
    if chiffre >= 1:
        bas = 0
        haut = chiffre
    if 0 < chiffre < 1:
        bas = chiffre
        haut = 1
    #début de méthode de dichotomie
    while True:
        milieu  = (bas + haut) / 2
        if milieu ** n < chiffre:
            bas = milieu
        if milieu ** n > chiffre:
            haut = milieu
        if haut - bas < (0.001):
            break
    return((haut + bas)/2)


#calcul de temps nombre par nombre
start = time.perf_counter()
for _ in range(100000):
    racine_nombre_par_nombre(random.uniform(10, 10_00), 5)

end = time.perf_counter()
temps_total = (end - start)
moyenne = temps_total / 100000
print(f"Le temps pour compléter les 100 000 calculations avec la méthode de chiffre par chiffre est de {temps_total * 1000:.0f}ms et le temps moyen est de {moyenne*1000:.4f}ms")

#calcul de temps dichotomie
start = time.perf_counter()
for _ in range(100000):
    racine_dichotomie(random.uniform(10, 10_00))

end = time.perf_counter()
temps_total = (end - start)
moyenne = temps_total / 100000
print(f"Le temps pour compléter les 100 000 calculations avec la méthode de dichotomie est de {temps_total * 1000:.0f}ms et le temps moyen est de {moyenne*1000:.4f}ms")

#calcul de temps math.sqrt
start = time.perf_counter()
for _ in range(100000):
    math.sqrt(random.uniform(10, 10_00))

end = time.perf_counter()
temps_total = (end - start)
moyenne = temps_total / 100000
print(f"Le temps pour compléter les 100 000 calculations avec la méthode de math.sqrt est de {temps_total * 1000:.0f}ms et le temps moyen est de {moyenne*1000:.4f}ms")
#racine carrée, cubique et quatrième de 8, 9, 81 et 123.
list = [8,9,81,123]
for i in range(3):
    for j in range(len(list)):
        print(racine_nombre_par_nombre_n(list[j], 4, (i+2)))
        print(racine_dichotomie_n(list[j], (i+2)))
print(list[0])