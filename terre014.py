import sys


def input_data():
    nombres = sys.argv[1:]
    return nombres

def test_data(nombres):
    valeur="".join(nombres)
    try:
        int_1=int(valeur)
    except:
        print("erreur")
        sys.exit()
    return int_1

def trie(nombres):
    nombres2=[]
    while nombres:
        mini=nombres[0]
        for z in nombres:
            if z < mini:
                mini=z
        nombres.remove(mini)
        nombres2.append(mini)
    return nombres2




def compare(nombres, int_1):
    #nombres.sort()
    nombres2 = trie(nombres)
    valeur="".join(nombres2)
    int_2=int(valeur)
    if int_1==int_2:
        print("Triée !")
    else:
        print("Pas triée !")
    
    



nombres=input_data()
int_1=test_data(nombres)
compare(nombres, int_1)
