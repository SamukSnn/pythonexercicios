totc = 0
totn = 0
for c in range(0, 501, 3):
    if c % 2 == 1:
        totc += c
        totn += 1

print("A soma de todos os {} solicitados é {}".format(totn, totc))