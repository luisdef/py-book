# Exercício 4.6
# Escreva um programa que pergunte a distância
# que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50
# por km para viagens de até 200 km, e R$ 0,45
# para viagens mais longas.
print('Cálculo do valor do ticket de uma passagem:\n')
distancia = int(input('Distância que irá percorrer [km]: '))
if distancia <= 200:
    valor_passagem = distancia * 0.50
    print(f'\nValor da passagem: R$ {valor_passagem:.2f}.')
else:
    valor_passagem = distancia * 0.45
    print(f'\nValor da passagem: R$ {valor_passagem:.2f}.')
