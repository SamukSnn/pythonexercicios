from random import randint

computador = randint(1, 10)
contV = 0
linhaIgualTraço = "=-"*15
LinhaTraço = "-"*30

#Início
print(linhaIgualTraço)
print("VAMOS JOGAR PAR OU ÍMPAR")
print(linhaIgualTraço)
jogador = int(input("Digite um valor: "))
p = str(input("Par ou Ímpar? [P/I] "))[0].upper()
soma = jogador + computador
print(LinhaTraço)

#Pares
if soma % 2 == 0:
    par = "P"
    #Verificação se o jogador venceu ou perdeu
    while True:
        if not p == par:
            print(f"Você jogou {jogador} e o computador {computador}. Total de {jogador+computador} DEU PAR")
            print(LinhaTraço)
            print("Você PERDEU!")
            print(linhaIgualTraço)
            print(f"GAME OVER! Você venceu {contV} vezes.")
            break
        if p == par:
            print(f"Você jogou {jogador} e o computador {computador}. Total de {jogador+computador} DEU PAR")
            print(LinhaTraço)
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            print(linhaIgualTraço)
            jogador = int(input("Digite um valor: "))
            p = str(input("Par ou Ímpar? [P/I] "))[0].upper()
            contV += 1

#Ímpares
if soma % 2 == 1:
    impar = "I"
    #Verificação se o jogador venceu ou perdeu
    while True:
        if not p == impar:
            print(f"Você jogou {jogador} e o computador {computador}. Total de {jogador+computador} DEU ÍMPAR")
            print(LinhaTraço)
            print("Você PERDEU!")
            print(linhaIgualTraço)
            print(f"GAME OVER! Você venceu {contV} vezes.")
            break
        if p == impar:
            print(f"Você jogou {jogador} e o computador {computador}. Total de {jogador+computador} DEU ÍMPAR")
            print(LinhaTraço)
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            print(linhaIgualTraço)
            n = int(input("Digite um valor: "))
            p = str(input("Par ou Ímpar? [P/I] "))[0].upper()
            contV += 1