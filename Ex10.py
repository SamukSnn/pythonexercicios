dinheiro = float(input("Quanto de dinheiro você tem na carteira? R$"))
convert = dinheiro / 3.27
print("Com R${:.2f} você pode comprar U${:.2f}".format(dinheiro, convert))