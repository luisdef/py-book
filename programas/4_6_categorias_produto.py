# Programa 4.6
# Categorai x preço

print('Preço da categoria de um produto:\n')

categoria = int(input('Categoria do produto [int]: '))

if categoria == 1:
    preco = 10

else:
    if categoria == 2:
        preco == 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    print('Categoria inválida, digite um valor entre 1 e 5!')
                    preco = 0

print(f'O preço do produto é: R$ {preco:.2f}.')
