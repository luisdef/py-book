# Exercício 5.4
# Faça um programa que imprima os números pares até o número que
# foi informado pelo usuário.

print('Contagem de números pares:\n')
fim = int(input('Último número a mostrar: '))
x = 1
while x <= fim:
    print(x)
    x += 2
print('Fim!')