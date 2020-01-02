from pesos import calcularPesos as cp
from neuronios import *

print("## REDE NEURAL ##\n".center(20))

valorUm = int(input('valorUm -> '))
valorDois = int(input('valorDois -> '))
valorTres = int(input('valorTres -> '))



pesos = cp()
print(f"\nlog> 'pesos' {pesos}") # LOG
sinapse_um = sinapse_um(valorUm, valorDois, valorTres, pesos)
print(f"log> 'sinapse_um' {sinapse_um}") # LOG
sinapse_dois = sinapse_dois(sinapse_um[0], sinapse_um[1], pesos)
print(f"log> 'sinapse_dois' {sinapse_dois}") # LOG

if sinapse_dois[0] > sinapse_dois[1]:
    print('\nAção 1')
else:
    print('\nAção 2')

