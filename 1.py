# Faça um programa, com uma função que precisa de três parâmetros, e que forneça a soma desses três argumentos.
def somatresnumeros(a,b,c):
    return a+b+c
numr1=float(input('digite o primeiro numero: '))
numr2=float(input('digite o segundo numero: '))
numr3=float(input('digite o terceiro numero: '))
resultado=somatresnumeros(numr1,numr2,numr3)
print(f'a soma de tres numeros e: {resultado}')