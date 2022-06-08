import sys


def afficher():
    arguments = sys.argv[1:]
    for i in range(len(arguments)):
        print(arguments[i])


afficher()
