# Escreva uma expressão que será utilizada para decidir se um
# aluno foi ou não aprovado. Para ser aprovado, todas as médias
# do aluno devem ser maiores que 7. Considere que o aluno cursa
# apenas 3 matérias, e que a nota de cada uma está armazenada
# nas seguintes variáveis: materia1, materia2 e materia3.

materia1 = float(input("Nota matéria 1: "))
materia2 = float(input("Nota matéria 2: "))
materia3 = float(input("Nota matéria 3: "))

if materia1>=7 and materia2>=7 and materia3>=7:
    print("Aprovado.")
else:
    print("Reprovado.")
