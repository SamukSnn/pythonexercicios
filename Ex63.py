soma = cont = n = 0
while True:
    n = int(input("Digite um valor (999 para parar): "))
    if n == 999:
        break
    soma += n #Soma todos os números
print(f"A soma dos valores foi {soma}")