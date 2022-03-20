# Exercício 5.12
# Altere o programa anterior de forma a perguntar também
# O valor depositado mensalmente. Esse valor será depositado
# no início de cada mês, e você deve considerá-lo para o cálculo
# de jutos do mês seguinte.

print("Calculadora de rendimentos mensais na poupança:\n")

dep_inicial = float(input("Depósito inicial: R$ "))
mes_dep = float(input("Depósito mensal: R$ "))
tax_jur_poup = float(input("Taxa de juros da poupança: "))

poupanca = dep_inicial

print("\n+-------+---------------+")
print("|  Mês  |      Valor    |")
print("+-------+---------------+")

meses = 1
while meses <= 24:
    poupanca += mes_dep
    poupanca += poupanca * tax_jur_poup / 100
    fstr_poupanca = f"{poupanca:.2f}"
    print(f"|{meses:^7}| R$ {fstr_poupanca:11}|")
    meses += 1
print("+-------+---------------+")