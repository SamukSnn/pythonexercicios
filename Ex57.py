import random
tot = 1
print('''Sou seu computador..
Acabei de pensar em um número de 0 a 10.
Será que você consegue adivinhar qual foi?''')
palpite = int(input("Qual seu palpite? "))
computador = random.randint(0, 10)

#acertou = False
#while not acertou:
while palpite != computador:
    if palpite < computador:
        palpite = int(input("Mais... Tente mais uma vez.\nQual seu palpite? "))
        tot += 1
    elif palpite > computador:
        palpite = int(input("Menos... Tente mais uma vez.\nQual seu palpite? "))
        tot += 1
    if palpite == computador:
#        acertou = True
        print("Acertou com {} tentativas. Parabéns!".format(tot))