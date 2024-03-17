dia = int(input("Quantos dias alugados? "))
Km = int(input("Quantos Km rodados?"))
valor = (dia * 60) + (Km * 0.15)
print("O total a pagar é de R${:.2f}".format(valor))
