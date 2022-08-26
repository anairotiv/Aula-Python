# leitura de duas notas parciais de um aluno. E calcular a média alcançada por aluno.
#Aprovado se maior ou igual a sete
#reprovado se menor do que sete
#aprovado com distinção se for igual a dez

print ("Bem vindo ao meu programa, responda as perguntas abaixo para saber sua note")

nota1 = int(input('Qual a sua primeira nota? '))
nota2 = int(input ('Qual a sua segunda nota? '))

media = (nota1 + nota2) / 2

if media >= 7 and 10:
    print ('voce foi aprovado')
elif media < 7:
    print ('voce está reprovado')
