tot18 = totHomem = totMulher = 0

while True:
    print("-"*30)
    print("     CADASTRE UMA PESSOA")
    print("-"*30)
    idade = int(input("Idade: "))
    if idade >= 18:
        tot18 += 1
    sexo = str(input("Sexo: [M/F] "))[0].strip().lower()
    if sexo == "m":
        totHomem += 1
    elif sexo == "f" and idade <= 20:
        totMulher += 1
    print("-"*30)
    r = str(input("Quer continuar? [S/N] "))[0].strip().lower()
    while r == "s":
        print("-"*30)
        print("     CADASTRE UMA PESSOA")
        print("-"*30)
        idade = int(input("Idade: "))
        if idade >= 18:
            tot18 += 1
        sexo = str(input("Sexo: [M/F] "))[0].strip().lower()
        if sexo == "m":
            totHomem += 1
        elif sexo == "f" and idade <= 20:
            totMulher += 1
        print("-"*30)
        r = str(input("Quer continuar? [S/N] "))[0].strip()
        if r == "n":
            print(f"Total de pessoas com mais de 18 anos: {tot18}")
            print(f"Ao todo temos {totHomem} homens cadastrados")
            print(f"E temos {totMulher} mulheres com menos de 20 anos")
            break
    break