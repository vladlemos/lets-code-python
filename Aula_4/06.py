'''
Faça uma função que recebe uma string e retorna ela ao contrário. 
Exemplo: Recebe "teste" e retorna "etset".
'''

palavra = input('digite uma palavra: ')

def inverter(palavra):
    return palavra[len(palavra)::-1]

print (inverter(palavra))





