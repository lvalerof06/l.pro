#Escreva um algoritmo que receba 100 números, e conte quantos deles estão no intervalo [10, 20] 
#e quantos deles estão fora do intervalo, escrevendo estas informações.
contar=0
for i in range (100):
    f1=int(input("digite um numero"))
    if(f1>10)and(f1<20):
        contar1=contar+1
    print(contar1)
else:
    contar1=contar+1