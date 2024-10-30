#1) Escreva um programa que receba três notas, mostre a média aritmética delas 
# e informe se o aluno foi aprovado ou
#  reprovado. Nota para ser aprovado deve ser igual ou maior que 7.
nota1=float(input("informea primeira nota: "))
nota2=float(input("informe a segunda nota: "))
nota3=float(input("informe a terceira nota: "))
soma=(nota1+nota2+nota3)/3
if(soma >7):
    print("aprovado")
else:
    print("desaprovado")
