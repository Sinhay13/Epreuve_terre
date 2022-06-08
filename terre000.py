alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def afficher(x):
    n = 0
    l = " "
    while n < len(x):
        l += str(x[n])
        n += 1
    print(l)


afficher(alphabet)
