nome = str(input("Digite seu nome completo aqui: ")).strip()
print("Analisando seu nome...")
print("Seu nome competo em maiúsulo é {}".format(nome.upper()))
print("Seu nome completo em minúsculo é {}".format(nome.lower()))
#print("Seu nome tem ao todo {} letras".format(len(nome)-nome.count(" ")))
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))