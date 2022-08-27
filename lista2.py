#utilizando o metodo append da lista.

lista = []
resposta = ''

while resposta != 'acabou':
    resposta = input ('o que temos que comprar? ')
    if resposta != 'acabou': 
      lista.append(resposta)
    
print (lista)

#>>> lista = []
#>>> lista.append (0) 
#>>> lista
#[0]

