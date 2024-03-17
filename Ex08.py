metros = float(input("Digite uma distância em metros: "))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = int(metros * 10)
cm = int(metros * 100)
mm = int(metros * 1000)
print("A medida de {:.1f} corresponde a".format(metros))
print("{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm".format(km,hm, dam, dm, cm, mm))
# OU
# print("{}km \n{}hm \n{}dam \n{:0f}dm \n{:0f}cm \n{:0f}mm".format(km,hm, dam, dm, cm, mm))