#sum -> soma
#len -> tamanho

#def soma (numero_1, numero_2):
    #return numero_1 + numero_2


#def media(lista_de_numeros):
    #return sum (lista_de_numeros) / len(lista_de_numeros)

#executar ali no terminal python
# media ([1,2,3])
#2.0

#sum ([1,2,3,4])
#10

#### Funcoes nomeadas"""
### ele não falou sobre funcoes anonimas e funcao geradora""" -> ESTUDAR.
def imprime_relatorio (nome,cpf,telefone):
    return f"""
     
     Relátorio parcial
     
     Nome: {nome}
     cpf: {cpf}
     telefone: {telefone}
     
     """
print (imprime_relatorio
       ('Ana vitoria', '12345678','6299180-0826')
)
    