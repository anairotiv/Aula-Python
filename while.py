
#Resposta = 'Inicial'

#resposta = input ('Vamos sair hoje? [s/n]? ')

#while resposta != 's':
    #resposta = input ('Vamos sair hoje [s/n]')
    
#print ('Então, vamos!!!')


resposta = input ('Bora dá um rolê hoje? [s/n]? ')

n=1

while resposta != 's':
      resposta = input (f'Bora{"a" * n} [s/n]? ')
      n += 1
      if 'chato' in resposta or 'chata' in resposta:
        print ('foi mal')
        break
else:
    
        print ('Então bora!!!')