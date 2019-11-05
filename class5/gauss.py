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
            print(str(round(i,2)) + "  ", end=" ")
            # print(str(i) + "  ", end=" ")
        print()


m = [[3, 2, 3, 16], [2, 5, 1, 15], [4, 2, 3, 17]]
mC = copy.deepcopy(m)


def triangularization(m):
    dimV = len(m)

    for diag in range(dimV):
        aux = m[diag][diag]
        for col in range(dimV + 1):
            m[diag][col] /= aux
        for lin in range(diag + 1, dimV):
            aux2 = m[lin][diag]
            for col in range(diag, dimV + 1):
                m[lin][col] -= m[diag][col] * aux2

    for diag in range(dimV - 1, -1, -1):
        for lin in range(diag - 1, -1, -1):
            factor = m[lin][diag]
            for col in range(diag, dimV + 1):
                m[lin][col] -= m[diag][col] * factor

    return m

printMatrix(triangularization(m))
