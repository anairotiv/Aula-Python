#carteira = 100
carteira = int(input('quanto eu tenho? '))
tenis = int (input ('Quanto custa? '))
necessidade = input ('preciso mesmo disso [s/n] ')
             
#tenis = 150

if carteira >= tenis and necessidade == 's':
    print ('comprei um tenis novo')
else:
    print ('deixa para o mes que vem')