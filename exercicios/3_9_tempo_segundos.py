# Exercícios 3.9
# Escreva um programa que leia a quantidade de
# dias, horas, minutos e segundos do usuário.
# Calcule o total em segundos.

print('\nTempo total em segundos:\n')

dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

total_segundos = segundos + (((dias * 24) * 60) * 60) + ((horas * 60) * 60) + (minutos * 60)

print(f'\nO total do tempo em segundos é: {total_segundos} s.')
input('Pressione Enter para sair... ')
