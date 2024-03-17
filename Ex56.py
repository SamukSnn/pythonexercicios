sexo = str(input("Informe seu sexo: [M/F] "))[0].upper()
while not sexo == "M" or sexo == "F":
    sexo = str(input("Dados inválidos. Por favor, Informe seu sexo: "))[0].strip().upper()
print("Sexo {} registrado com sucesso".format(sexo))