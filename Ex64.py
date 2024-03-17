while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    if n < 0:
        break
    print("---"*10)
    for c in range(1, 10):
        print(f"{n} X {c} == {n*c}")
    print("---"*10)
print("---"*10)
print("PROGRAMA TABUÁDA ENCERRADO. Volte Sempre!")