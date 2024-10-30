# Escreva um programa que receba um número inteiro de 1 à 12 e imprima na tela seu mês correspondente. 
# #Se o número não estiver no intervalo [1, 12], informe que o mês solicitado é inválido. janeiro
m = int(input("digite um numero: "))
if(m==1):
    print("janeiro")
if(m==2):
    print("fevereiro")
if(m==3):
    print("marco")
if(m==4):
    print("abril")
if(m==5):
    print("maio")
if(m==6):
    print("junho")
if(m==7):
    print("julho")
if(m==8):
    print("agosto")
if(m==9):
    print("setembro")
if(m==10):
    print("outubro")
if(m==11):
    print("novembro")
if(m==12):
    print("dezembro")
if(m>12):
    print("nao e um mes boca aberta")