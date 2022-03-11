# Exercício 3.11
# Faça um programa que solicite o preço
# de uma mercadoria e o percentual de 
# desconto. Exiba o valor do desconto 
# e o valor a pagar.

print('\nCálculo de desconto de mercadoria:\n')
valor_mercadoria = float(input('Valor da mercadoria: R$ '))
percentual_desconto = float(input('Percentual de desconto: '))
desconto = valor_mercadoria * percentual_desconto / 100
mercadoria = valor_mercadoria - desconto
print(f'\nValor do desconto: R$ {desconto:.2f}.')
print(f'Valor da mercadoria: R$ {mercadoria:.2f}.')
