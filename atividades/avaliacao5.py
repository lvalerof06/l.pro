#Crie um algoritmo que leia um número inteiro. Se o número lido for positivo, 
# escreva uma mensagem indicando se ele e par ou impar.
n=int(input("digite um numero inteiro"))
if(n>1):
    print("o numero e positivo")
    if(n%2==0):
        print("o numero e par")
    else:
        print("o numero e impar")
else:
    print("valor negativo")
