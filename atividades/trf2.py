#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
#Os códigos utilizados são: 1 , 2, 3, 4 - Votos para os candidatos associados
# (você deve montar uma tabela  ex: 1 - José/ 2- João /3 - Maria/ 4 - Meu nego) 5 - Voto Nulo 6 - Voto em Branco
i=0
joao=0
jose=0
maria=0
meunego=0
nulo=0
embranco=0
while(i<6):
    candidato=int(input('informe seu candidato:'))
    if(candidato==1):
        jose+=1
    if(candidato==2):
        joao+=1
    if(candidato==3):
        maria+=1
    if(candidato==4):
        meunego+=1  
    if(candidato==5):
        embranco+=1
    if(candidato==6):
        nulo+=1
    total=jose+joao+maria+meunego
    print('o total de votos para jose',jose)
    print('o total de votos para joao',joao)
    print('o total de votos para maria',maria)
    print('o total de votosm para meunego',meunego)
    if(candidato==0):
        i=7