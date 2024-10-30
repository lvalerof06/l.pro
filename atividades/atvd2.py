#Construa um algoritmo que leia cem números e mostre qual o maior número que foi lido
maior=0
for i in range(100):
    nmr1=float(input("digite o numero"))
    if(nmr1>maior):
        maior=nmr1
print("o maior numero lido foi ",maior)
