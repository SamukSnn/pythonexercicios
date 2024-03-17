import math

r = "s"
cont = soma = maior = menor = 0
while not r == "n":
    num = int(input("Digite um número: "))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input("Quer continuar? [S/N] "))[0].lower()
    média = soma / cont
    if r == "n":
        print("Você digitou {} números e a média foi {:.2f}".format(cont, média))
        print("O menor número digitado foi {} e o maior foi {}".format(menor, maior))

