#Crie um algoritmo que leia um número inteiro. Se o número lido for positivo, 
# escreva uma mensagem indicando se ele e par ou impar.
codigo=int(input("digite o codigo de digitacao"))
num1=int(input("digite o total de vendas"))
if(num1<100):
    print("a comissao aumentou 0%")
elif(num1>100)and(num1<350):
    print("a comissao aumentou 6%")
    soma=(num1/6)+num1
    print(soma)
elif(num1>350):
    print("a comissao aumentou10%")
    soma=(num1/10)+num1
    print(soma)