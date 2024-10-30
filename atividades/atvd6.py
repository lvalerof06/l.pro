#Escrever um algoritmo que leia 50 números e informe quantos destes valores são negativos.
contar1=0
contar2=0
for i in range (1,51):
    f1=int(input("digite um numero"))
    if (f1<=0): 
        contar1=contar1+1
else:
    contar2=contar2+1
print("o valor é negativo", contar1)
print("o valor é positivo", contar2)
