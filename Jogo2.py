# Leonardo Balestra
import time
from random import randint

ENTER = str(input("\n\nPense em um número entre 0 e 500 e aperte o enter!"))
time.sleep(1/2)

min = 0
max = 500
L = ['E','A','C','V']
x = randint(min,max)
r = 'a'
N = []
qtd = 0

while r != 'C' and r != 'V':

    print(".")
    time.sleep(1/2)
    print("..")
    time.sleep(1/2)
    
    print("\nO número é o %d?" %x) # Número gerado entre o min e o max
    qtd = qtd + 1
    N.append(x)
    
    r = str(input("\nResponda com 'E' (menor), 'A' (maior) e 'C' (correto): ")).upper()
    
    while r not in L: # Para a resposta não ser inválida, deve estra na lista
        r = str(input("\nResponda com 'E' (menor), 'A' (maior) e 'C' (correto): ")).upper()
        
    time.sleep(0.5)
    
    if max == min and r != 'C': # Quando o programa acha o número (min=max) porém o usuário ainda diz que não está correto(!=C)
        print("\nEspertinho!! Querendo me BUGAR né?!")
        r = 'V'
        
    else:
        if r == 'E': # Se for menor
            max = x - 1 # Como o resultado é menor que o número dado o limite agora é o número digitado menos ele mesmo, pois ele está errado

            if min < 0 or min > max: # caso o min seja menor que 0, ou o min seja maior que max
                print("\nEspertinho!! Querendo me BUGAR né?!")
                r = 'V'
            else:
                x = randint(min,max)
                
        if r == 'A': # Se for maior
            min = x + 1 # Como o resultado é maior que o número dado o limite agora é o número digitado mais ele mesmo, pois ele está errado
            
            if max > 500 or min > max: # caso o max seja maio que 500, ou o min seja maior que max
                print("\nEspertinho!! Querendo me BUGAR né?!")
                r = 'V'
            else:
                x = randint(min,max)
    
if r == 'C':
    print("\n\nSou muito bom nesse jogo, o número é %d!!" %x)
    print("\nHouve %d tentativas, foram elas:\n" %(qtd))
    print(N)
    
else:
    print("\nJogue sem roubar agora!")
    print("\nHouve %d tentativas, foram elas:\n" %(qtd))
    print(N)

