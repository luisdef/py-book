# Programa 4.3
# Cálculo do Imposto de Renda

print('Cálculo do Imposto de Renda:\n')
salario = float(input('Digite o salário para cálculo do imposto: R$ '))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 100) * 0.20)
print(f'\nSalário: R$ {salario:.2f};\nImposto a pagar: R$ {imposto:.2f}.')
