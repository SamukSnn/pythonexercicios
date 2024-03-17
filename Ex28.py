import random
from random import randint
#Prints
print("-=-" * 20)
print("Voou pensar em um número entre 0 e 5. Tente Adivinhar...")
print("-=-" * 20)
n = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")


#Sorteio, forma 1
lista = [0, 1, 2, 3, 4, 5]
sorteio = random.choice(lista)
#Sorteio, forma 2
computador = randint(0, 5)


#Verificação
if not n == sorteio:
    print("GANHEI! Eu pensei no número {} e não no {}".format(sorteio, n))
else:
    print("PARABÉNS! Você conseguiu me vencer!")