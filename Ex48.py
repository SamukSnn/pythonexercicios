n = int(input("Digite um número para ver sua tabuada: "))
for c in range(1, 11):
    tot = c * n
    print("{} x {:2} = {}".format(n, c, tot))