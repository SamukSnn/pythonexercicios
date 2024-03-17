maior = 0
menor = 0

#Laço de 5 ciclos
for p in range(1, 6):
    peso = float(input("Peso da {}° pessoa: ".format(p))) #Pesos
    if p == 1: #Se estiver no primeiro ciclo, Maior e Menor definidos.
        maior = peso
        menor = peso
    else: #Se não estiver no primeiro ciclo, verificar se...
        if peso > maior: #Se o peso de outro ciclo for maior que o peso do primeiro ciclo então... 
            maior = peso
        if peso < menor: #Se o peso de outro ciclo for menor que o peso do primeiro ciclo então...
            menor = peso
print("O maior peso lido foi de {:.1f}Kg".format(maior))
print("O menor peso lido foi de {:.1f}Kg".format(menor))



