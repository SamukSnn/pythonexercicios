num = int(input("Digite um número [999 para parar]: "))
soma = num
tot = 0
while not num == 999:
    num = int(input("Digite um número [999 para parar]: "))
    soma += num
    tot1 = soma- 999
    tot += 1
print("Você digitou {} números e a soma entre eles foi {}.".format(tot, tot1))