peso = float(input("Qual seu peso? (Kg) "))
altura = float(input("Qual sua altura? (m) "))
imc = peso / (altura ** 2)

print("O IMC dessa pessoa é de {:.2f}".format(imc))

if imc < 18.5:
    print("OLHA! Você está Abaixo do Peso.")
elif imc >= 18.5 and imc < 25:
    print("PARABÉNS! Você está no Peso Ideal.")
elif imc >= 25 and imc < 30:
    print("ATENÇÃO! Você está com Sobrepeso.")
elif imc >= 30 and imc <= 40:
    print("SE CUIDE! Você está com Obesidade.")
elif imc > 40:
    print("CUIDADO! Você está com Obesidade Mórbida.")
