#Faça um programa que receba uma string e responda se ela tem alguma vogal, se sim quais são? e também diga se 
#é uma frase ou não.


frase = (input("Qual sua frase?\n ")) 
                         
                                          
## Deixando a variavel miniscula para aceita de diversas maneiras de digitação
frase = frase.lower()    
  
## Variaveis A E I O U já contadas 
a = int(frase.count('a')); e = int(frase.count('e')); i = int(frase.count('i'));                                                                                                                                                                             
o = int(frase.count('o')); u = int(frase.count('u')); espaco = int(frase.count(' '))            
## Variavel espaco para indetificar se é frase ou palavra


##If com objetivo de decobrir se as variaveis apareciam ao menos uma vez, para determinar se existiam vogais
if (a > 0 or e > 0 or i > 0 or o > 0 or u > 0):                     
    print("Foi encontrada vogal")
else:
    print(" não tem vogal")


## Contagem de vogais A E I O U
if a > 0:                                              
    print(f"Econtramos a vogal A {a} vezes!")
if e > 0:
    print(f"Econtramos a vogal E {e} vezes!")
if i > 0:
    print(f"Econtramos a vogal I {i} vezes!")
if o > 0:
    print(f"Econtramos a vogal O {o} vezes!")
if u > 0:
    print(f"Econtramos a vogal U {u} vezes!")
    
    
## Identificação se é frase ou palavra
if espaco > 0:
    print("Isso é uma frase e não uma palavra!")            
else:
    print("Isso é uma palavra, e não uma frase!")