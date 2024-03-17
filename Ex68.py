print("="*30)
print("{:^30}".format("BANCO CEV"))
print("="*30)
valor = int(input("Que valor você quer sacar? R$ "))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd: #Se o valor que eu quero sacar for maior que 50, então ele vair subtrair com 50
        total -= céd
        totcéd += 1 #Conta a quantidade cédulas de 50 reais
    else:
        if totcéd > 0:
            print(f"Total de {totcéd} cédulas de R${céd}")
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break