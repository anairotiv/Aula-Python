#como fazer para descobrir se algo é falso ou verdadeiro em booleano

#2>3 #MENTIRA, INVERDADE, FALSe
#3>2 #verdade, True

nome_1 = 'fausto'
idade_1 = 3

nome_2= 'maria'
idade_2 = 23

nome_3 = 'fausto'
idade_3 = 45

nome_1 == nome_2 #false
nome_1 == nome_3 #true

nome_1 != nome_2 #true

#and -> conectivo
nome_1 == nome_3 and idade_1  == idade_3 #false
#se uma delas for falso da falso
# se a primeira e a segunda for verdade então da verdadeiro

#no or (ou) se uma delas for verdade tudo se torna verdade
nome_1 == nome_3 or idade_1  == idade_3 

#not 
#inverta a lógica 
not nome_1 == nome_3
