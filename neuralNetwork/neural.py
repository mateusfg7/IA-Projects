from random import *

print("## REDE NEURAL ##\n".center(20))

distancia = int(input('distancia -> '))
altura = int(input('altura -> '))
velocidade = int(input('velocidade -> '))

pesos1 = []
def calcularPesos1():
    neuronio = 1

    while neuronio <= 2:

        peso1 = distancia*randrange(-1000,1000)
        peso2 = altura*randrange(-1000,1000)
        peso3 = velocidade*randrange(-1000,1000)

        pesos1.append([peso1, peso2, peso3])

        neuronio += 1

calcularPesos1()

def sinapse1():
    resultdo = [0,0]

    index = 0
    while index <= 1:
        for p in pesos1[index]:
            resultdo[index] += p
        index += 1
    
    for r in resultdo:
        index = 0
        if r <= 0:
            resultdo[index] = 0
            index += 1

    return resultdo


pesos2 = []
def calcularPesos2(peso):
    neuronio = 1

    while neuronio <= 2:

        peso1 = peso[0]*randrange(-1000,1000)
        peso2 = peso[1]*randrange(-1000,1000)

        pesos2.append([peso1, peso2])

        neuronio += 1

calcularPesos2(sinapse1())

def sinapse2out():
    resultdo = [0,0]

    index = 0
    while index <= 1:
        for p in pesos2[index]:
            resultdo[index] += p
        index += 1
    
    for r in resultdo:
        index = 0
        if r <= 0:
            resultdo[index] = 0
            index += 1

    return resultdo

out = sinapse2out()

if out[0] > out[1]:
    print('\npular')
else:
    print('\nabaixar')
