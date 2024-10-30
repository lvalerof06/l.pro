#) Construa um algoritmo que receba o código e o total de vendas do vendedor, calcule a comissão conforme a tabela
#e informe o código e a comissão do vendedor:
cs=int(input("informe o codigo"))
cs1=int(input("informe o total de vendas"))
if(cs<=100):
    print("a comissao e de 0%")
if(cs>100)and(cs<350):
    comissao = (cs/100)*6
    print(comissao)
if(cs>350):
    comissao = (cs/100)*10
    print(comissao)