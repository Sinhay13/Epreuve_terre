import sys


def input_data():
    l = sys.argv[1:]
    return l


def transformation(l):
    l1 = l[::-1]
    n = 0
    l2 = []
    while n < len(l1):
        l2.append(l1[n][::-1])
        n += 1
    l3 = " ".join(l2)
    print(l3)


data = input_data()
transformation(data)
