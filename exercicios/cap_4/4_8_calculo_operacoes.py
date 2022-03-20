# Exercício 4.8
# Escreva um programa que leia dos números e que pergunte
# qual operação deseja realizar. Você deve poder
# calcular soma (+), subtração (-), multiplicação (*) e 
# divisão (/). Exiba o resultado da operação solicitada.

print('Calculadora simples de operações:\n')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

operacao = input('''Opções:
  (+) Adição;
  (-) Subtração;
  (*) Multiplicação;
  (/) Divisão.
Sua opção: ''').strip()[0]

if operacao in '+':
    print(f'\n{n1} + {n2} = {n1+n2}.')
elif operacao in '-':
    print(f'\n{n1} - {n2} = {n1-n2}.')
elif operacao in '*':
    print(f'\n{n1} * {n2} = {n1*n2}.')
elif operacao in '/':
    print(f'\n{n1} / {n2} = {n1/n2}.')
else:
    print(f'\nOperação ({operacao}) não identificada.')
