#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
#Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
mais=0
menos=10000
cmenos=0
cmais=0
for i in range(2):
    numero=int(input('digite seu numero: '))
    altura=float(input('digite sua altura: '))
    if altura > mais:
        mais=altura
        cmais=numero
    if altura < menos:
        menos=altura
        cmenos=numero
        print(f'aluno mais alto',{mais},{cmais})
        print(f'alunos mais baixo',{menos},{cmenos})