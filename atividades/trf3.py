 #Faça um algoritmo que receba a sigla da cidade de origem de um grupo de pessoas,
 #ao final informe quantas foram digitalizadas das cidades do Rio de Janeiro, 
 #Belo Horizonte e Santa Catarina (separadamente). O algoritmo encerra quando digitado a palavra “fim”
i=0
rj=0
bh=0
sc=0
while(i<1):
    cdd=str(input('informe:'))
    if(cdd=='rj'):
        rj+=1
    if(cdd=='bh'):
        bh+=1
    if(cdd=='sc'):
        sc+=1
    if(cdd=='fim'):
        i=2
    print('pessoas do rj',rj)
    print('pessoas de bh e',bh)
    print('pessoas de sc',sc)