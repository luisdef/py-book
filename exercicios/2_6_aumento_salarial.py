# Exercício 2.6 p.49
# Modifique o programa "../programas/2_calculo_de_aumento_salario.py"
# de forma que ele calcule um aumento de 15%,
# para um salário de R$ 750,00

salario = 750
aumento = 15

salario_pos_aumento = salario + (salario * aumento / 100)
print(f"\nSalário = R$ {salario}\n"
      f"Aumento = {aumento} %\n"
      f"Salário com o aumento aplicado = R$ {salario_pos_aumento}")

input("\nDigite Enter para sair... ")
