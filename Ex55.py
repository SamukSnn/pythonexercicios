média = 0
maiorIdade = 0
nomeVelho = ""
totMulher = 0
totHomem = 0
somalidade = 0

for p in range(1, 5):
    print("{:-^21}".format(" {}° PESSOA ".format(p)))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))[0].lower()
    somalidade += idade
    if p == 1 and sexo == "m":
        maiorIdade = idade
        nomeVelho = nome
    else:
        if idade > maiorIdade and sexo == "m":
            maiorIdade = idade
            nomeVelho = nome
    if p == 1:
        if sexo == "f" and idade < 20:
            totMulher += 1
    else:
        if sexo == "f" and idade < 20:
            totMulher += 1
    if p == 1:
        if sexo == "m":
            totHomem += 1
    else:
        if sexo == "m":
            totHomem += 1
print("-=-" * 10)
print("A média de idade do grupo é de {:.1f} anos".format(somalidade/4))
if totHomem == 0:
    print("Nenhuma pessoa do sexo Masculino foi encontrada.")
else:
    print("O homem mais velho tem {} anos e se chama {}".format(maiorIdade, nomeVelho.capitalize()))

if totMulher == 0:
    print("Nenhuma pessoa do sexo Feminino foi encontrada.")
else:
    print("Ao todo são {} mulheres com menos de 20 anos.".format(totMulher))
print("-=-" * 10)