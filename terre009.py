import sys

def input_data():
    nb = sys.argv[1:]
    return nb

def calcul_racine(x):
    r=0
    if x > 0:
        r= x**(0.5)
        print(r)
    else:
        print("erreur")


def test_data(nb):
    if len(nb) != 1:
        print("erreur")
    else:
        try:
            x=int(nb[0])
            calcul_racine(x)
        except:
            print("erreur")





nb=input_data()
test_data(nb)   