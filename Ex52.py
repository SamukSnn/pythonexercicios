frase = str(input("Digite uma frase: ")).upper().strip()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) -1, -1, -1): #O len conta quantas letras tem, ou seja, 6 letras, mas em uma string é do 0 que começa, ou seja, é do 0 ao 5
    print("{}".format(junto[letra]), end="")
    inverso += junto[letra]
if inverso == junto:
    print("\nTemos um Palíndromo.")
else:
    print("\nA frase digitada não é um Palíndromo.")


#Samuel: 6 Letras no len, 5 letras em uma string.