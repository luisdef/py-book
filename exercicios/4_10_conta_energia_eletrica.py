# Exercício 4.10
# Escreva um programa que calcule o preço a pagar pelo
# fornecimento de energia elétrica. Pergunte a quantidade
# de kWh consumida e o tipo de instalação: R para residências,
# I para indústrias e C para comércios. Calcule o preço a pagar
# de acordo com a tabela a seguir.

# Preço por faixa de consumo:
# --------------------------------------------
# | Tipo        | Faixa (kWh)     | Preço    |
# --------------------------------------------
# | Residencial | Até  500        | R$ 0,40  |
# |             | Acima de 500    | R$ 0,65  |
# --------------------------------------------
# | Comercial   | Até 1000        | R$ 0,55  |
# |             | Acima de 1000   | R$ 0,60  |
# --------------------------------------------
# | Industrial  | Até 5000        | R$ 0,55  |
# |             | Acima de 5000   | R$ 0,66  |
# --------------------------------------------

print('Calculador de Fornecimento de energia:\n')

kwh = int(input('Informe os kWh consumidos: '))
instalacao = input('Tipo de instalação:\n  (R) Residência;\n  (I) Industrial;\n  (C) Comércios.\n>> ').strip().upper()[0]
