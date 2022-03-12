# Exercício 5.9
# Escreva um programa que leia dois números de um usuário

print('Calculadora de divisão:')

num = int(input('Numerador: '))
den = int(input('Denominador: '))

cont = 0
numerador = num
while den <= numerador:
    numerador -= den
    cont += 1

divisao = str(cont)

resto = str(num / den).split('.')
divisao += "."+resto[1]

print(f'{num} / {den} = {divisao}')