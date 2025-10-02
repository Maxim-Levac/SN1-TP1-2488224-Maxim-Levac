import random
import time
import math

def racine_nombre_par_nombre_n(nombre, decimal=7, n=2):
    """
    Trouver la racine carrée d'un chiffre à l'aide de la méthode nombre par nombre
    Paramètres :
    nombre (float) : Nombre à calculer la racine carrée
    decimal (int) : Nombre de décimal à calculée
    n (float) : nieme racine

    Retourne :
    float : racine carrée du chiffre

    Exemple d'utilisation :
    >>> racine_nombre_par_nombre_n(27, 2, 3)
    3.0
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
    for i in range(decimal + 1):
        chiffre_trouver = False
        chiffre = 0

        # Trouver décimal
        while not chiffre_trouver:
            #Nouveau chiffre haut et bas à tester
            nouveau_chiffre_haut = (premier_chiffre + (chiffre * 10 ** -i))
            nouveau_chiffre_bas = (premier_chiffre + ((chiffre-1) * 10 ** -i))
            #Vérifier si nouveau chiffre est égale au nombre
            if nouveau_chiffre_haut ** n == nombre:
                premier_chiffre = nouveau_chiffre_haut
                chiffre_trouver = True
                break


            #vérifier si les deux chiffres sont entre le vrai chiffre
            if nouveau_chiffre_haut ** n >= nombre and nouveau_chiffre_bas ** n <= nombre:
                premier_chiffre = nouveau_chiffre_bas
                chiffre_trouver = True

            else:
                chiffre += 1

    return(round(premier_chiffre, decimal -1))


def racine_dichotomie_n(chiffre, n=2):
    """
    Trouver la racine carrée d'un chiffre à l'aide de la méthode dichotomie
    Paramètres :
    nombre (float) : Nombre à calculer la racine carrée
    n (float): n-ième racine

    Retourne :
    float : racine carrée du chiffre

    Exemple d'utilisation :
    >>> racine_dichotomie_n(27,3)
    3.0
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
    else:
        bas = chiffre
        haut = 1
    #début de méthode de dichotomie
    while True:

        milieu = (bas + haut) / 2

        #vérifier si milieu est égale au chiffre
        if milieu ** 2 == chiffre:
            return round(milieu,6)
        if milieu ** n < chiffre:
            bas = milieu
        elif milieu ** n > chiffre:
            haut = milieu
        else:
            return round(milieu,6)
        if haut - bas < (0.0000001):
            break
    return round(((haut + bas)/2), 6)


#calcul de temps nombre par nombre
print("Résultats des performances : ")
start = time.perf_counter()
for _ in range(100000):
    racine_nombre_par_nombre_n(random.uniform(10, 10_00), 14)

end = time.perf_counter()
temps_total = (end - start)
moyenne = temps_total / 100000
print(f"Le temps pour compléter les 100 000 calculations avec la méthode de chiffre par chiffre est de {temps_total * 1000:.0f}ms et le temps moyen est de {moyenne*1000:.4f}ms")

#calcul de temps dichotomie
start = time.perf_counter()
for _ in range(100000):
    racine_dichotomie_n(random.uniform(10, 10_00))

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

nombres = [8,9,81,123]
for i in range(3):
    for j in range(len(nombres)):
        print(f"la racine {i+2}-ieme de {nombres[j]} est de {racine_nombre_par_nombre_n(nombres[j], 7, (i+2))} (nombre par nombre)")
        print(f"la racine {i+2}-ième de {nombres[j]} est de {racine_dichotomie_n(nombres[j], (i+2))} (dichotomie)")