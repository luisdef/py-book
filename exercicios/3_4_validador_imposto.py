# Exercício 3.4 p.60
# Escreva uma expressão para determinar 
# se uma pessoa deve ou não pagar imposto. 
# Considere que pafam imposto pessoas 
# cujo salário é maior que R$ 1200,00.

print("Validador Imposto\n\n")

# Primeiro solicitar o salário
salario = float(input("Salário: R$ "))
print("Paga imposto:", end=" ")
print(salario > 1200)

input("\nDigite Enter para sair... ")
