import sys


def input_data():
    nombres = sys.argv[1:]
    return nombres

def calcul_puis(a,b):
    r=1
    for i in range(0,b):
        r=a*r
    return r

def test_data(nombres):
    x=0
    x1=0
    x2=0
    if len(nombres) != 2:
        print("erreur")
    else:
        try:
            x=int(nombres[0])
            x1=int(nombres[1])
            x2=calcul_puis(x,x1)
            print(x2)
        except:
                print("erreur")
    
        
    
    

nombres=input_data()
test_data(nombres)




    