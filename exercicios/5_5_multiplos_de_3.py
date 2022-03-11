# Exercício 5.5
# Escreva um programa que mostre os 10 primeiros
# múltiplos de 3.

print('10 primeiros múltiplos de 3 ==> { - ', end="")
multiplo = 0
contador = 0
while contador <= 10:
    print(multiplo, end=" - ")
    multiplo += 3
    contador += 1
print('}\nFim!')
