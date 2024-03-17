
num = int(input("Digite um número: "))
tot = 0 #Somatória

for c in range(1, num+1): #Ira repetir do número 1 ao número desejado
    if num % c == 0: #Se a divisão de número por c for igual a 0, então irá pintar o número 
        print("\033[33m", end=" ") #O que não sobra é pintado de amarelo
        tot += 1 #Quantida de números que sobrou é o que foi divisível
    else:
        print("\033[31m", end=" ") #O que sobra ele pinta de vermelho
    print("{}".format(c),end=" ")
print("\n\033[mO número {} foi divisível {} vezes".format(num, tot))
if tot == 2:
    print("E por isso o número É PRIMO!")
else:
    print("E por isso o número NÃO É PRIMO")

