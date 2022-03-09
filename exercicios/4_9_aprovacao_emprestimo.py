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
# Valor da casa; Salário; Anos a pagar.
casa = float(input('Valor da casa: R$ '))
print(f'Valor digitado: R$ {casa:.2f}')
