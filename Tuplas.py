#tuplas é lista imutável
#desempacotamento
#contar posicão

#count -> contar qunatos numeros tem dentro

#   x=(1,2,3)

#   x.count (2) -> 1 quantos 2 tem 
#   x.index(2) -> 1 posicao do valor

minha_tupla = ('eduardo', 20, '72462472','rua magalhaes, 0')

nome, idade, *coisas_que_eu_n_quero = minha_tupla

#pesquisando no interpretador.
#nome -> eduardo
#idade -> 20

# coisas_que_eu_n_quero
# ['72462472','rua magalhaes, 0']

#nome, idade = idade, nome
#inverte.

#codigos separados por virgulas são sempre tuplas.

def minha_func():
        return 1,2,3 
    
#estudar mais empacotamento das tuplas.