casa = float(input("Valor da casa: "))
salário = float(input("Salário do comprador: R$"))
ano = int(input("Quantos anos de financiamento? "))
prestação = casa / (ano * 12)
mínimo = salário * 30 / 100
print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(casa, ano, prestação))
if salário <= mínimo:
    print("Empréstimo pode ser CONCEDIDO!")
elif salário >= mínimo:
    print("Empréstimo NEGADO!")