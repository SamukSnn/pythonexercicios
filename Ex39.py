from datetime import date
ano = int(input("Ano de nascimento: "))
anoatual = date.today().year
idade = anoatual-ano
idadeA = 18 - idade
idadeB = anoatual + (18 - idade)
idadeD = idade - 18
print("Quem nasceu em {} tem {} em {}.".format(ano, idade, anoatual))
if idade == 18:
    print("Você tem que se ailstar IMEDIATAMENTE!")
elif idade < 18:
    print("Ainda faltam {} anos para o alistamento.".format(idadeA))
    print("Seu alistamento será em {}".format(idadeB))
elif idade > 18:
    print("Você já deveria ter se alistado há {} anos.".format(idadeD))
    print("Seu alistamento foi em {}".format(idadeB))