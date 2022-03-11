# Exercício 5.7
# Faça um programa de tabuada que permita que o
# usuário escolha qual o primeiro valor a calcular
# a tabuada e qual o último (ao invés de 1 e 10).

print('Tabuada personalizada:')

num_tabuada = int(input('N° a ser tabuado: '))
inicio = int(input('Início da tabuada em: '))
fim = int(input('Fim da tabuada em: '))

while inicio >= fim:
    print('O número de início deve ser maior que o número do fim.')
    inicio = int(input('Início da tabuada em: '))
    fim = int(input('Fim da tabuada em: '))

contador = inicio
while contador <= fim:
    print(f'{contador} x {num_tabuada} = {contador * num_tabuada}')
    contador += 1
print('Fim!')
