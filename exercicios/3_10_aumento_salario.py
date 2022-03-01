# Exercício 3.10
# Faça um programa que calcule o aumento de um
# salário. Ele deve solicitar o valor do salário
# e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

print('\nCalculador de salário:\n')

salario_anterior = float(input('Digite o salário: R$ '))
porcentagem_aumento = float(input('Digite a porcentagem do aumento: '))

aumento = salario_anterior * porcentagem_aumento / 100
salario = salario_anterior + aumento

print(f'\nAumento do salário: R$ {aumento:.2f}.')
print(f'Novo salário: R$ {salario:.2f}.')
input('\nPressione Enter para sair...')
