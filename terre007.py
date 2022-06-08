import sys


def input_data():
    n = 0
    l = sys.argv[1:]
    if len(l)>1:
        chaine="erreur"
    else:
        chaine = " "
        while n < len(l):
            chaine += str(l[n])
            n += 1
    return chaine
    
def compter(x):
    if x == "erreur":
        print(x)
    else:
        try:
            x_int=int(x)
            print("erreur")
        except:
            print(len(x))

chaine=input_data()
compter(chaine)

    

        
