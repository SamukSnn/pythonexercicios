cidade = str(input("Em que cidade você nasceu? ")).strip().lower()
espaço = cidade.find(" ") #Aqui ele vai procurar onde se encontra o primeiro espaço, logo verifica se começa com ou sem a palavra santo
print(cidade[0:espaço] in "santo")

"""
cid = str(input("Em que cidade você nasceu? ")).strip()
print(cid[:5].upper() == "SANTO)

"""