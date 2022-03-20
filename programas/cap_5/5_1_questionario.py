# Programa 5.1
# Utilizando contadores para calcular pontos em um questionário.

pontos = 0
questao = 1
while questao <= 3:
    resposta = input(f"Resposta da questao {questao}: ")
    if questao == 1 and resposta == "b":
        pontos += 1
    if questao == 2 and resposta == "a":
        pontos += 1
    if questao == 3 and resposta == "c":
        pontos += 1
    questao += 1
print(f"O aluno fez {pontos} ponto(s).")