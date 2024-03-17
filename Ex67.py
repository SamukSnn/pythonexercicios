print("-"*30)
print("      LOJA SUPER BARATÃO")
print("-"*30)
totCompra = totMil = cont = menor = 0
barato = ""

while True:
    produto = str(input("Nome do produto: "))
    preço = float(input("Preço: R$"))
    cont += 1
    totCompra += preço
    if preço >= 1000:
        totMil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    r = " "
    while r not in "sn":
        r = str(input("Quer continuar? [S/N] "))[0].lower().strip()
    if r == "n":
        break
print("{:=^40}".format(" FIM DO PROGRAMA "))
print(f"O total da compra foi R${totCompra:.2f}")
print(f"Temos {totMil} custando mais de R$1000.00")
print(f"O produto mais barato foi {produto} que custa {menor:.2f}")