# Exercício 4.9
# Escreva um programa para aprovar o empréstimo 
# bancário para compra de uma casa. O programa
# deve perguntar o valor da casa a comprar, o
# salário e a quantidade de anos a pagar. O valor 
# da prestação mensal não pode ser superior a 30% do
# salário. Calcule o valor da prestação como sendo o
# valor da casa a comprar dividindo pelo número de 
# meses a pagar.

print('Cálculo de aprovação de empréstimo:\n')

valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Informe seu salário: R$ '))
anos = int(input('Anos a pagar a casa: '))

meses = anos * 12
valor_mensal_casa = valor_casa / meses

if valor_mensal_casa > ((salario * 30) / 100):
    print('\nEmpréstimo recusado.')
else:
    print('\nEmpréstimo aprovado.')
