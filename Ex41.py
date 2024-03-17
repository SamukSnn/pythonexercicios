from datetime import date

ano = int(input("Ano de nascimento: "))
idade = date.today().year - ano
list = ["MIRIM", "INFANTIL", "JUNIOR", "SÊNIOR", "MASTER"]

if idade <= 9:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: {}".format(list[0]))
elif idade <= 14:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: {}".format(list[1]))
elif idade <= 19:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: {}".format(list[2]))
elif idade <= 25:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: {}".format(list[3]))
elif idade > 25:
    print("O atleta tem {} anos.".format(idade))
    print("Classificação: {}".format(list[4]))