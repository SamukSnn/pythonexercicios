n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
parar = False
maior = 0

while not parar == True:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior 
[ 4 ] novos números
[ 5 ] sair do programa''')
    opção = int(input(">>>>> Qual é a sua opção? "))
    if opção == 1:
        soma = n1 + n2
        print("A soma entre {} + {} é {}".format(n1, n2, soma))
        print("=-=" * 10)
    elif opção == 2:
        multiplicação = n1 * n2
        print("A multiplicação entre {} x {} é {}".format(n1, n2, multiplicação))
        print("=-=" * 10)
    elif opção == 3:
        if n1>n2:
            maior = n1
        elif n2>n1:
            maior = n2
        print("Entre {} e {} o maior valor é {}".format(n1, n2, maior))
        print("=-=" * 10)
    elif opção == 4:
        print("Informe os números novamente: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opção == 5:
        parar = True
print("Finalizando...")
print("=-=" * 10)