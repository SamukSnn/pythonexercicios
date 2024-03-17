totpar = 0
cont = 0
for c in range(0, 6):
    num = int(input("Digite um valor: "))
    if num % 2 == 0:
        totpar += num
        cont += 1
print("Você informou {} números PARES e a soma deles é de {}.".format(cont, totpar))