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
            print(str(round(i, 2)) + "  ", end = " ")
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


m = triangularization(m)


def residue(m, mC):
    res = [0, 0, 0]
    for i in range(len(mC)):
        for j in range(len(mC)):
            res[i] += mC[i][j] * m[j][3]

    return [res[i] - mC[i][3] for i in range(len(m))]


sol0 = [[1, 0, 0, 0.95], [0, 1, 0, 2.25], [0, 0, 1, 2.9]]


def adjust(sol, eps):
    sol1 = copy.deepcopy(sol)
    for i in range(len(eps)):
        sol1[i][3] += eps[i]
    return sol1


print("original matrix")
printMatrix(mC)
print()
print("solved matrix (x0)")
printMatrix(sol0)
print()
print("residue x0")
eps0 = residue(sol0, mC)
print(eps0)
print()
sol1 = adjust(sol0, eps0)
print("solved matrix (x1)")
printMatrix(sol1)
print()
print("residue x1")
eps1 = residue(sol1, mC)
print(eps1)
