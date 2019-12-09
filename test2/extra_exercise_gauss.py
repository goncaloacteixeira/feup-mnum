def upperTriang(amatrix):
    dimV = len(amatrix)

    # triangularizar a parte de baixo
    for diag in range(dimV):
        aux = amatrix[diag][diag]
        for col in range(dimV + 1):
            amatrix[diag][col] /= aux
        for lin in range(diag + 1, dimV):
            aux2 = amatrix[lin][diag]
            for col in range(diag, dimV + 1):
                amatrix[lin][col] -= amatrix[diag][col] * aux2

    return amatrix


def lowerTriang(amatrix):
    dimV = len(amatrix)
    # triangularizar a parte de cima
    for diag in range(dimV - 1, -1, -1):
        for lin in range(diag - 1, -1, -1):
            aux = amatrix[lin][diag]
            for col in range(diag, dimV + 1):
                amatrix[lin][col] -= amatrix[diag][col] * aux

    return m


m = [[0.1, 0.5, 3.0, 0.25, 0],
     [1.2, 0.2, 0.25, 0.20, 1.0],
     [-1.0, 0.25, 0.3, 2.0, 2.0],
     [2.0, 0.00001, 1.0, 0.4, 3.0]]

sol = upperTriang(m)

print("alinea a) values:")
print("1st:", sol[1][2])
print("2nd:", sol[1][3])
print("3rd:", sol[1][4])
print("4th:", sol[2][3])
print("5th:", sol[2][4])
print("6th:", sol[3][4])

sol = lowerTriang(sol)

print("\nalinea b) values:")
print("x1:",sol[0][4])
print("x2:",sol[1][4])
print("x3:",sol[2][4])
print("x4:",sol[3][4])

# TODO - ESTABILIDADES (INTERNA E EXTERNA)