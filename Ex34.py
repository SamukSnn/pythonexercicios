salario = float(input("Qual é o salário do funcionário? "))

if salario >= 1250:
    sn1 = salario + ((salario * 10) / 100)
else: 
    sn1 = salario + ((salario * 15) / 100)


print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.".format(salario, sn1))