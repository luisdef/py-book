# Exercício 5.8
# Escreva um prigrama que leia 2 números.
# Imprima o resultado da multiplicação do primeiro
# pelo segundo. Utilize apenas os operadores de
# soma e subtração para calcular o resultado.

print('Calculadora de multiplicação: ')

num1 = int(input('N° 1: '))
num2 = int(input('N° 2: '))

multiplicacao = 0
contador = num2
while contador > 0:
    multiplicacao += num1
    contador -= 1

print(f'{num1} x {num2} = {multiplicacao}')