# Exercício 3.15
# Escreva um programa para calcular o
# tempo de redução de vida de um fumante.
# Pergunte a quantidade de cigarros fumados
# por dia e quantos anos ele já fumou. Considere
# que um fumante perde 10 minutos de de vida a cada
# cigarro, e calcule quantos dias de vida um fumante
# perderá. Exiba o total de dias.

print('\nPerda do tempo de vida pelo Cigarro:\n')

cigarros = int(input('Cigarros por dia: '))
anos = int(input('Anos fumando: '))

cigarros_fumados = (365 * anos) * cigarros
minutos_perdidos = cigarros_fumados * 10
dias_perdidos = (minutos_perdidos / 60) / 24

print(f'\nDias de vida perdidos: {int(dias_perdidos)}.')
