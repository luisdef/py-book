# Exercício 3.12
# Escreva um programa que calcule o
# tempo de uma viagem de carro. Pergunte
# a distância a percorrer e a velocidade
# média esperada para uma viagem.

print('\nTempo para uma viagem:\n')

distancia = float(input('Distância [km]: '))
velocidade_media = float(input('Velocidade média esperada [km/h]: '))

tempo = distancia / velocidade_media

print(f'\nTempo esperado da viagem: {tempo} h.')
