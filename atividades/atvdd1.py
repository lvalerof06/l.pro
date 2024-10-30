#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
#utilizando as seguintes fórmulas: Para homens: (72.7*h) - 58 Para mulheres: (62,1*h) - 44,7
num=str(input('homem ou mulher?'))
altura=float(input('qual a sua altura?'))
if num == 'homem':
    num=72.2*num-58
    print(num)
else:
    num='mulher'
    print('mulher? kkkk sapata')
    numr=(62.1*altura-44.7)
    print(numr)
