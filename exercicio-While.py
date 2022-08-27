#Faça um programa que peça uma nota, entre zero e dez. Mostre ma msg caso o valor seja inválido
# e continue pedindo até que o usuário informe um valor
#válido

nota=float(input("informe um numero de 0 a 10: "))
while (nota>10) or (nota<0):
	nota=float(input("digite um numero entre 0 a 10: "))
 
#como eu faria para dizer que o numero inserido é válido não.
