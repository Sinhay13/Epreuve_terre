import sys


def input_data():
    n = 0
    nombres = sys.argv[1:]
    nb = " "
    while n < len(nombres):
        nb += str(nombres[n])
        n += 1
    return nb


def try_data(nb):
    try:
        nb_int = int(nb)
        if nb_int == 0:
            print("Tu ne me la mettras pas à l'envers.")
        elif nb_int % 2 == 0:
            print("Pair")
        else:
            print("Impair")
    except:
        print("Tu ne me la mettras pas à l'envers.")


nb = input_data()
try_data(nb)
