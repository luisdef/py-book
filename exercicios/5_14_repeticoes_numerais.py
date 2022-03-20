# Exercício 5.14
# Escreva um programa que leia números inteiros do teclado.
# O programa deve ler os números até que o usuário digite
# 0. No final da execução, exiba a quantidade de números digitados,
# assim como a soma e a média aritmética.

soma = 0
qtde = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n == 0:
        break
    soma += n
    qtde += 1
media = soma / qtde
print(f"\nNúmeros digitados: {qtde}.")
print(f"Soma: {soma}.")
print(f"Média: {media}.")
