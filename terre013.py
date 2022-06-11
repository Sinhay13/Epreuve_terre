import sys


def input_data():
    nombres = sys.argv[1:]
    list=[1,2,3]
    list[0] = int(nombres[0])
    list[1] = int(nombres[1])
    list[2] = int(nombres[2])
    return list 

def Max(list):
    max=0
    for i in range(len(list)):
        if list[i] > max:
            max=list[i]
    return max

def Min(list,max):
    min=max
    for i in range(len(list)):
        if list[i] < min:
            min=list[i]
    return min

def Suisse (list,max,min):
    suisse =0
    if min==max:
        suisse="erreur"
    else:
        for i in range(len(list)):
            if i!=max and i!=min:
                suisse=list[i]
    print(suisse)
    



try:
    list=input_data()
    max=Max(list)
    min=Min(list,max)
    Suisse(list,max,min)
except:
    print("erreur")

