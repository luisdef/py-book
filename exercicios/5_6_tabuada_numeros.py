# Exercício 5.6
# Exiba os resultados de uma tabuada.

print('Tabuada\n')

num_tabuada = int(input('Informe um n° inteiro: '))
contador = 1

while contador <= 10:
    print(f'{contador} x {num_tabuada} = {contador * num_tabuada}')
    contador += 1

print('Fim!')
