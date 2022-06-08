import sys

def input_data():
    nb = sys.argv[1:]
    return nb



def test_data(nb):
    nbf=0
    if len(nb)==1:
        try:
            nbf=int(nb[0])
        except:
            nbf="erreur"
    else:
        nbf = "erreur"
    return nbf

def test_premier(nbf):
    if nbf == "erreur":
        print(nbf)
    else:
        if nbf <2:
            print("erreur")
        else:
            for i in range(2, nbf):
                if (nbf % i) == 0:
                    print(f"Non, {nbf} n’est pas un nombre premier.")
                    break
                else:
                    print(f"Oui, {nbf} est un nombre premier.")
                    break



nb =input_data()
nbf=test_data(nb)
test_premier(nbf)


