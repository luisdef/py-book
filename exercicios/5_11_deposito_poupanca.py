# Exercício 5.11
# Escreva um programa que permita o depósito inicial
# e a taxa de juros de uma poupança. Exiba os valores
# mês a mês para os 24 primeiros meses. Escreva o total
# ganho com juros no período.

print("Calculadora de rendimentos na poupança:\n")

dep_inicial = float(input("Depósito inicial: R$ "))
taxa_jur_poupanca = float(input("Taxa de juros poupança: "))


print("\n+-------+---------------+")
print("|  Mês  |      Valor    |")
print("+-------+---------------+")

poupanca = dep_inicial
meses = 1
while meses <= 24:
    poupanca += poupanca * taxa_jur_poupanca / 100
    fstr_poupanca = f"{poupanca:.2f}"
    print(f"|{meses:^7}| R$ {fstr_poupanca:11}|")
    meses += 1
print("+-------+---------------+")
