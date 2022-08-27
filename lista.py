#lista é como se fosse um container, inclusive ela permite outros dados dentro.
#elas aceitam todos os tipos de objeto.
#sempre começa a contar a partir do zero.
#geralmente é ordenado.


minha_lista = ['sabao', 'sabonete', 'arroz']

#tmb é permitido inteiros
#minha_lista = ['sabao', 'sabonete', 'arroz', 'feijao', 10, [1,2,3]]

#pode fazer o -1 para pegar o final da lista
#minha_lista [-1]
#se quiser pegar o ultimo da lista dentro da lista é so fazer 
#minha_lista [-1] [-1]

#pegar por posicao
#tambem da certo para saber a ultima posicao do nome ou afins, quando é
#string
#'eduardo' [-1]

print(minha_lista)

#qual a primeira coisa que preciso comprar? qual a posicao da minha lista?
#minha_lista[0]
#vai retornar sabão

#pode usar o for
#for coisa in minha_lista:
#print (coisa)

#### SLICE ####

#forma de fatiar a lista.

#n=[0,1,2,3,4,5,6,7,8,9]

# >>> n[0]    #0            -> 0 
# >>> n[6:]   #[6,7,8,9]    -> contar os primeiros num e dps pegar do 6 para frente
# >>> n[:-6]  #[0,1,2,3]    -> vai contar de trás para frente e pegar os primeiros numeros
# >>> n[::2]  #[0,2,4,6,8]  -> do começo até o final pulando de dois em dois.

#>>> nomes
#['eduardo', 'ana', 'helom', 'guilherme', 'pedro']
#>>> nomes [3]
#'guilherme'
#>>> nomes [-3]
#'helom'
#>>> nomes [:-4]
#['eduardo']
#>>> nomes [0:-1] 
#['eduardo', 'ana', 'helom', 'guilherme']


### MATRIZES ####
#estudar


### MÉTODOS- LISTAS 
# >>> X = [1,2,3]


# >>> x.append(4)   -> como se tivesse uma fala e acrescenta algo no final dessa fila
# >>> #[1,2,3,4]    

# >>> x.insert(4,0)   -> na posicao 4 ele coloca o zero.
# >>> #[1,2,3,0]

# >>> x.count(2)      -> quantos dois vc tem ai dentro.
# >>> #1

# >>> x.remove(2)  -> remove o numero que ta pedindo
# >>> #[1,3]

# >>> x.pop()      -> tira um valor dai de dentro (?)
# 3 | # [1,2]

# x.reverse()      -> inverte a lista
# None|#[3,2,1]

# FILA -> QUANDO QUER INSERIR NO ULTIMO
# LISTA -> inserir em qualquer lugar 
# PILHA -> TIRA DO ULTIMO




