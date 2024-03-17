from random import randint
from time import sleep

print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogada = int(input("Qual é a sua jogada? "))
list = ["Pedra", "Papel", "Tesoura"]
computador = randint(0, 2)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")


print("-=-" * 10)
print("Computador jogou {}".format(list[computador]))
print("Jogador jogou {}".format(list[jogada]))
print("-=-" * 10)

if jogada > 2:
    print("Opção inválida. Tente novamente!")
elif computador == 0 and jogada == 2:
    print("Computador Ganhou!")
    comp = list[0]
elif computador == 1 and jogada == 0:
    print("Computador Ganhou!")
    comp = list[1]
elif computador == 2 and jogada == 1:
    print("Computador Ganhou!")
    comp = list[2]
elif jogada == 0 and computador == 2:
    print("Você Ganhou!")
    jogador = list[0]
elif jogada == 1 and computador == 0:
    print("Você Ganhou!")
    jogador = list[1]
elif jogada == 2 and computador == 1:
    print("Você Ganhou!")
    jogador = list[2]
elif jogada == computador:
    print("EMPATE!")