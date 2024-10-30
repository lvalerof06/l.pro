# Faça um programa que leia e valide as seguintes informações:
# Nome: mais de 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
nome=str(input('digite um nome: '))
n1=len(nome)
if(n1 <= 3):
    print('invalido',n1)
else:
    print('valido')
idade=int(input('digite sua idade: '))
if(idade>=0) and (idade<=150):
    print('invalido',idade)
else:
    print('valido')
sexo=str(input('informe seu sexo: '))
if(sexo=='m')or(sexo=='f'):
    print('invalido',sexo)
else:
    print('valido')
estadocivil=str(input('informe seu estado civil: '))
if(estadocivil=='s')or(estadocivil=='c')or(estadocivil=='v')or(estadocivil=='d'):
    print('invalido',estadocivil)
else:
    print('valido')