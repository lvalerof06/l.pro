# Construir um algoritmo que receba cem números e informe a média e a soma entre os números positivos.
x9=0
for i in range(1,5):
    f1=int(input("informe um numero"))
    if(f1>0):
        x9 = x9 + f1
media=x9/i
print("a soma dos numero e",x9)
print("a media dele e",media)