#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
n=int(input('digite um numero: '))
if n>1:
    for i in range (2,n):
        if (n%i==0):
            print('n e nmr primo')
            break
        else:
            print('nmr primo')
            break
else:
    print('n e nmr primo')