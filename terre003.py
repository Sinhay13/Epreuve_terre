import sys


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

L = str(sys.argv[-1]) # metre des non de para plus precis 


def chercher(a, L):
    n = 0
    for n in range(len(a)):
        if L != a[n]:
            n += 1
        else:
            return n


def afficher(n, a):
    l = ""
    while n < len(a):
        l += str(a[n])
        n += 1
    print(l)


n = chercher(alphabet, L)
afficher(n, alphabet)
