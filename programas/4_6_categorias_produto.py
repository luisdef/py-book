# Programa 4.6 e 4.7
# Categorai x preço
executed_lines = [4,5,6]
print('Preço da categoria de um produto:\n')
categoria = int(input('Categoria do produto [int]: '))
if categoria == 1:
    preco = 10
    executed_lines.append(7)
else:
    executed_lines.append(9)
    if categoria == 2:
        preco == 18
        executed_lines.append(11), executed_lines.append(12)
    else:
        executed_lines.append(14)
        if categoria == 3:
            preco = 23
            executed_lines.append(16), executed_lines.append(17)
        else:
            executed_lines.append(19)
            if categoria == 4:
                preco = 26
                executed_lines.append(21), executed_lines.append(22)
            else:
                executed_lines.append(24)
                if categoria == 5:
                    preco = 31
                    executed_lines.append(26), executed_lines.append(27)
                else:
                    executed_lines.append(29)
                    print('Categoria inválida, digite um valor entre 1 e 5!')
                    preco = 0
                    executed_lines.append(31), executed_lines.append(32), executed_lines.append(34), executed_lines.append(35)
print(f'O preço do produto é: R$ {preco:.2f}.')
print(f'Linhas executadas: {executed_lines}')
