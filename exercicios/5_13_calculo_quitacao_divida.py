# Exercício 5.13
# Escreva um programa que pergunte o valor inicial
# de uma dívida e também o juro mensal. Pergunte
# também o valor mensal que será pago. Imprima o n°
# de meses para que a dívida seja paga, o total
# pago e o total de juros pagos.

print("Cálculo de quitação de dívida:\n")

divida = float(input("Valor da dívida: R$ "))
juros = float(input("Juros mensais: "))
valor_mensal_quit = float(input("Valor mensal para a quitação: R$ "))

while valor_mensal_quit < (divida * juros / 100):
    print("O valor mensal para a quitação da dívida deve ser maior do que o valor cobrado dos juros.")
    juros = float(input("Juros mensais: "))
    valor_mensal_quit = float(input("Valor mensal para a quitação: R$ "))

meses = 1
juros_pagos = 0
total_pago = divida

while divida > 0:
    valor_juro = divida * juros / 100
    divida += valor_juro
    divida -= valor_mensal_quit

    total_pago += valor_juro
    juros_pagos += valor_juro

    meses += 1
print(f"São necessários {meses} meses para cobrir a dívida.")
print(f"Total pago em juros: R$ {juros_pagos:.2f}.")
print(f"Total pago: R$ {total_pago:.2f}.")