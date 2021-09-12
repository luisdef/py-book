# Exercício 2.1 - Livro p.45
# Convertaa as seguintes expressões matemáticas
# para que possam ser calculadas usando o
# interpretador Python.

# 10 + 20 x 30
# 4² : 30
# (9^4 + 2) x 6 - 1

expressao1 = 10 + 20 * 30
print(f"A expressão '10 + 20 x 30',\n"
      f"em Python é traduzida para '10 + 20 * 30',\n"
      f"que resulta em {expressao1}\n")

expressao2 = 4 ** 2 / 30
print(f"A expressão '4² : 30',\n"
      f"em Python é traduzida para '4 ** 2 / 30',\n"
      f"que resulta em {expressao2}\n")

expressao3 = (9 ** 4 + 2) * 6 - 1
print(f"A expressão '(9^4 + 2) x 6 - 1',\n"
      f"em Python é traduzida para '(9 ** 4 + 2) * 6 - 1',\n"
      f"que resulta em {expressao3}\n")

input("Digite Enter para sair... ")