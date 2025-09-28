
def racine(nombre):
    """

    :param nombre:
    :return:
    """
    for i in range(nombre):
        if i ** 2 >= nombre:
            premier_chiffre = i -1
            print(premier_chiffre)
            break
racine(8)