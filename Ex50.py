print("="*40)
print("          10 TERMOS DE UMA PA")
print("="*40)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
décimo = primeiro + (10 - 1) * razao

for c in range(primeiro, décimo + razao, razao):
    print("{} ".format(c), end="-> ")
print("ACABOU!")