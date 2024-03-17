print("{:=^40}".format(" LOJAS GUANABARA "))
preço = float(input("Preço das compras: R$"))
desconto1 = preço * 10 / 100
desconto2 = preço * 5 / 100
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opção = int(input("Qual é a opção? "))
if opção == 1:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preço, preço-desconto1))
elif opção == 2:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preço, preço-desconto2))
elif opção == 3:
    print("Sua compra de R${:.2f} será preço normal.")
elif opção == 4:
    parcelas = int(input("Quantas parcelas? "))
    pnovo = preço * 20 / 100
    total = (preço + pnovo) / parcelas
    total2 = pnovo + preço
    print("Sua compra será parcelada em {}x de {:.2f} COM JUROS!".format(parcelas, total))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço, total2))
else:
    print("OPÇÃO INVÁLIDA de pagamento. Tente novamente!")
