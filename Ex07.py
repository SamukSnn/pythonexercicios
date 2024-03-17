'''p1 = float(input("Primeira nota do aluno: "))
p2 = float(input("Segunda nota do aluno: "))
m = (p1 + p2) / 2
print("A média do aluno foi {:.1f}".format(m))'''

#Escola Nikkei
#Média de acima de 28 pontos para passar
#FAÇA UM PROGRAMA QUE TIRE A MÉDIA ARITMÉTICA DA ESCOLA NIKKEI

nome = str(input("Nome do Aluno: "))
n1 = float(input("1° Nota: "))
n2 = float(input("2° Nota: "))
n3 = float(input("3° Nota: "))
n4 = float(input("4° Nota: "))
média = (n1 + n2 + n3+ n4) / 4
print("O aluno {} com as notas {}, {}, {}, {}, ficou com a média de {}".format(nome, n1, n2, n3, n4, média))
if média >= 7:
    print("Aluno aprovado! Parabéns!")
else:
    print("Aluno reprovado! Estude mais!")