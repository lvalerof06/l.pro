# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
#o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota 
#(atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto; Total de Alunos que utilizaram o sistema; A Média das Notas da Turma.Gabarito da Prova:
# 01 - A 02 - B 03 - C 04 - D 05 - E 06 - E 07 - D 08 - C 09 - B 10 - A
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
alunos = []

while True:
    acertos = 0
    print("Responda as questões da prova:")
    
    for i in range(10):
        while True:
            resposta = input("Questão {} (A/B/C/D/E): ".format(i + 1))
            if resposta in ['A', 'B', 'C', 'D', 'E']:
                break
            print("Resposta inválida. Tente novamente.")
        
        if resposta == gabarito[i]:
            acertos += 1
    
    alunos.append(acertos)
    print("Sua nota: {} pontos.".format(acertos))

    continuar = input("Outro aluno vai utilizar o sistema? (s/n): ")
    if continuar != 's':
        break

if alunos:
    maior_acerto = alunos[0]
    menor_acerto = alunos[0]
    total_alunos = 0
    soma_notas = 0

    for nota in alunos:
        if nota > maior_acerto:
            maior_acerto = nota
        if nota < menor_acerto:
            menor_acerto = nota
        soma_notas += nota
        total_alunos += 1

    media_notas = soma_notas / total_alunos

    print("Resultados finais:")
    print("Maior acerto: {}".format(maior_acerto))
    print("Menor acerto: {}".format(menor_acerto))
    print("Total de alunos que utilizaram o sistema: {}".format(total_alunos))
    print("Média das notas da turma: {:.2f}".format(media_notas))