# Exercício 5.3
# Faça um programa para escrever a contagem regressiva do
# lançamento de um foguete. O programa deve imprimir 10,9,8,...,0 e Fogo! na tela.

from time import sleep as esperar

print('Contagem regressiva de lançamento de um foguete: ')

c = 10
while c >= 0:
    print(f'{c}')
    esperar(1)
    c -= 1
print('Fogo!!! 🚀🚀🚀🚀')
