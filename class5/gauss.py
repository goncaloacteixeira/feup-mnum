# Gauss
"""

-> resolver
-> calcular residuos
-> estabilidade interna




"""

import copy

def printMatrix(m):
    for lin in m:
        for i in lin:
            print (str(i) + "  ", end=" ")
        print()


m = [[3,2,3,16], [2,5,1,15], [4,2,3,17]]

mC = copy.deepcopy(m)

dimV = len(m)

for diag in range(dimV):
    for col in range(dimV + 1):
        m[diag][col] /= m[diag][diag]
    for lin in range(diag + 1, dimV):
        for col in range(diag, dimV + 1):
            m[lin][col] -= m[diag][col]*m[lin][diag]

printMatrix(m)

