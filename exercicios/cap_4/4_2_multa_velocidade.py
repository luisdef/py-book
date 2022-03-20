# Exercício 4.2
# Escreva um programa que pergunte
# a velocidade de um carro de um
# usuário. Caso ultrapasse 80 km/h,
# exiba uma mensagem dizendo que o
# usuário foi multado. Nesse caso,
# exiba o valor da multa, cobrando 
# R$ 5 por km acima de 80 km/h.

print('Verificação de velocidade:\n')

velocidade = int(input('Velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f'\nO carro está acima da velocidade. A multa é de R$ {multa:.2f}.')
else:
    print('\nO carro está dentro do limite de velocidade.')
