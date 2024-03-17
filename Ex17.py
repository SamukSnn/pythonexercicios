import math

co = float(input("Comprimento do Cateto Oposto: "))
ca = float(input("Comprimento do Cateto Adjacente: "))
hip = math.sqrt((math.pow(co, 2)) + (math.pow(ca, 2)))
#hip = ((co ** 2) + (ca ** 2)) ** (1/2)
#hip = math.hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hip))