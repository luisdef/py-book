# Exercício 3.14
# Escreva um programa que pergunte
# a quantidade de km percorridos por
# um carro alugado pelo usuário,
# assim com a quantidade de dias pelos
# quais o carro foi alugado.
# Calcule o preço a pagar, sabendo
# que o carro custa R$ 60 por dia e
# R$ 0,15 por km rodado.

print('\nLocação de carros:\n')

km_percorridos = int(input('Km percorridos pelo carro alugado: '))
dias = int(input('Dias que o carro foi alugado: '))

valor = (km_percorridos * 0.15) + (dias * 60)

print(f'\nPreço da locação: R$ {valor:.2f}.')
