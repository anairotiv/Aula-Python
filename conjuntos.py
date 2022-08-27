#x = {1,2,3}; y={3,4,5}

#x.union(y)              -> união dos conjuntos
#>>> {1, 2, 3, 4, 5}

#>>> x.intersection(y)   -> só pega o numero em comum
#{3}

#>>> x.difference(y)      -> pega os numeros diferentes
#{1, 2}

#>>> x.discard(1)         -> discarta usm número
#>>> x
#{2, 3}

#>>> x.update(y)           -> juntar os dois
#{1,2,3,4,5}

#>>> x.pop()               -> tira o último
#2

#set -> conjunto em portugues

#pode viras uma tupla ou uma lista
#em conjuntos não pode haver repetição
A= {'Eduardo', 'Eduardo'}
print(A)

# {'Eduardo'}
# >>> A.union ({'Ana Vitoria'})
# {'Eduardo', 'Ana Vitoria'}
