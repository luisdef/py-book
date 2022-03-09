# Calcule o resultado da expressão

# A > B and C or D

A = 1
B = 2
C = True
D = False
res = A > B and C or D
print(res)


A = 10
B = 3
C = False
D = False
res2 = A > B and C or D
print(res2)


A = 5
B = 1
C = True
D = True
res3 = A > B and C or D
print(res3)

print(f"""
# |-----------------------------------|
# |  A  |  B  |  C  |  D  | Resultado |
# |  1  |  2  |True |False|{res:^11}|
# | 10  |  3  |False|False|{res2:^11}|
# |  5  |  1  |True |True |{res3:^11}|
# |-----------------------------------|
""")
