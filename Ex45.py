from time import sleep
segundos = int(input("Qual a contagem regressiva para bomba explodir? "))

for c in range(segundos, 0, -1):
    print(c)
    sleep(1)
print("BUM! BUM! POOOW!!!")
