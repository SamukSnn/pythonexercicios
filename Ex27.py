nome = str(input("Digite seu nome completo: ")).strip().lower()
n = nome.split()
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(n[0].capitalize()))
print("Seu último nome é{}".format(nome[nome.rfind(" "):].title()))