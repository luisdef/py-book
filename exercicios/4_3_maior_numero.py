# Exercício 4.3
# Escreva um programa que leia
# três números e que imprima o
# maior e o menor.

print('Maior e menor número:\n')

maior = None
menor = None

for i in range(0, 3):
    n = int(input('Digite um número: '))
    if i == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f'\nMaior número: {maior}.')
print(f'Menor número: {menor}.')
