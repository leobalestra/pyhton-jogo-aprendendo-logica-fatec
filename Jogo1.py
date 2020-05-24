# Leonardo Balestra
from random import randint

min = 0
max = 500
x = -5
N = []
qtd = 0

print("\n************************************************************************")
print("**** Jogo 1 - Aprendendo Lógica em Python - FATEC-SP  - Prof. Banin ****")
print("************************************************************************")
print("************************************************************************")
print("***************** Descubra o número que estou pensando *****************")
print("************************************************************************")

while min > x or x > max: 
    x = int(input("\nDigite um número entre 0 e 500: "))

y = randint(min,max)

if x == y:
    qtd = qtd + 1
    N.append(x)

else:
    while x != y:

        if min <= x and x <= max:
            if x > y:
                qtd = qtd + 1
                N.append(x)
                print("O número é menor!")
                x = int(input("Tente novamente (Seu número anterior foi %d): " %(x)))
            else:
                qtd = qtd + 1
                N.append(x)
                print("O número é maior!")
                x = int(input("Tente novamente (Seu número anterior foi %d): " %(x)))
        else:
            print("O número deve estar entre %d e %d!" %(min,max))
            x = int(input("Tente novamente (Seu número anterior foi %d): " %(x)))

    qtd = qtd + 1
    N.append(x)
         
print("\nParabéns!! O numero correto é %d!" %y)
print("\nHouve %d tentativas, foram elas:\n" %(qtd))
print(N)
