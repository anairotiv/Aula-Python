#Faça um programa que receba uma data de nascimento (15/07/87) e imprima
#voce nasceu em <dia> de <mes> de <ano>


resposta = input ('qual sua data de nascimento ')
# 29/09/2001

dia, mes, ano = resposta.split('/')

print (f'voce nasceu em {dia} do {mes} do {ano}')