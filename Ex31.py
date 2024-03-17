distancia = float(input("Qual a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {:.1f}Km.".format(distancia))
if distancia <= 200:
    preço = distancia *  0.50
    print("E o preço da sua passagem será de R${:.2f}".format(preço))
if distancia >= 200:
    preço = distancia * 0.45
    print("E o preço da sua passagem será de R${:.2f}".format(preço))
