import sys


def input_data():
    nombres = sys.argv[1:]
    return nombres


def calculs(nombres):
    nb1 = int(nombres[0])
    nb2 = int(nombres[1])
    try:
        division = nb1//nb2
        reste = nb1 % nb2
        if division == 0:
            print("erreur.")
        else:
            print(f"resultat : {division}")
            print(f" reste : {reste}")
    except:
        print("erreur.")


nombres = input_data()
calculs(nombres)
