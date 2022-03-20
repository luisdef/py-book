# Exercício 4.4
# Escreva um programa que pergunte o salário
# do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1250,00, calcule
# um aumento de 10%. Para inferiores ou iguais,
# de 15%.
print('Calculador de Aumento de Salário:\n')
salario = float(input('Informe seu salário: R$ '))
if salario >= 1250:
    aumento = (salario * 10) / 100
    print(f'\nSalário reajustado: R$ {(salario + aumento):.2f}.')
else:
    aumento = (salario * 15) / 100
    print(f'Salário reajustado: R$ {(salario + aumento):.2f}.')
