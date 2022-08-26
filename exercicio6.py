# Faça um programa que pergunte o preço de 3 produtos e informe qual o produto voce deve comprar, sabendo que a decisão
#é semore pelo mais barato.

print ("Bem vindo, siga as instruções para escolher o melhor produto para voce\n")

produto_1 = float(input('digite o preço do primeiro produto  '))
produto_2 = float(input('Digite o preço do segundo produto'  ))
produto_3 = float(input('digite o preço do terceiro produto'  ))

#if produto_1 < produto_2 < produto_3:
    #print ('compre o 1')
#elif produto_2 < produto_3 < produto_1:
    #print ('compre o 2')
#else:
    #print ('compre 0 3')

if produto_1 > produto_2 and produto_2 < produto_3:
    print ('escolha o produto 3 ')
elif produto_2 > produto_1 and produto_1 < produto_3:
    print ('compre o 1')
    