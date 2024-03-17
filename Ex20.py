import random

a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))
lista = [a1, a2, a3, a4]
random.shuffle(lista) # Aqui ele está embaralhando a lista acima, realizando uma ação.
print("A ordem de apresentação será")
print(lista)