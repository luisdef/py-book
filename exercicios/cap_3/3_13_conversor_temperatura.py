# Exercício 3.13
# Escreva um programa que
# converta temperatura de C° para F°.
# F = ((9 x C) / 5) + 32
# C = ((F - 32) / 1.8)

print('\nConversor de temperaturas:\n')

opt = input('Converter Celcius ou Fahrenheit [C ou F]: ').strip().upper()[0]
while opt not in 'CF':
    print('Entrada não aceita.')
    opt = input('Converter Celcius ou Fahrenheit [C ou F]: ').strip().upper()[0]

if opt in 'C':
    c = float(input('C°: '))
    f = ((9 * c) / 5) + 32
    print(f'{c} C° ----> {f} F°.')
elif opt in 'F':
    f = float(input('F°: '))
    c = (f - 32) / 1.8
    print(f'{f} F° ----> {c} C°.')
else:
    print('Erro.')
