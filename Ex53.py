from datetime import date
ano = date.today().year

totMaior = 0
totMenor = 0

for pessoas in range(1, 8):
    anos = int(input("Em que ano a {}° nasceu? ".format(pessoas)))
    idade = ano - anos
    if idade >= 18:
        totMaior += 1
    elif idade < 18:
        totMenor += 1


print("Ao todo tivemos {} pessoas maiores de idades".format(totMaior))
print("Ao todo tivemos {} pessoas menores de idades".format(totMenor))