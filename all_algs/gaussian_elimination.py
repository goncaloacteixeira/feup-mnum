def upper_triang(amatrix):
    dimV = len(amatrix)
    for diag in range(dimV):
        aux = amatrix[diag][diag]
        # Dividir todos os membros pelo pivot, para ficar uma diagonal 1
        for col in range(dimV + 1):
            amatrix[diag][col] /= aux
        for lin in range(diag + 1, dimV):
            aux2 = amatrix[lin][diag]
            for col in range(diag, dimV + 1):
                amatrix[lin][col] -= amatrix[diag][col] * aux2

    return amatrix


def lower_triang(amatrix):
    dimV = len(amatrix)
    for diag in range(dimV - 1, -1, -1):
        for lin in range(diag - 1, -1, -1):
            aux = amatrix[lin][diag]
            for col in range(diag, dimV + 1):
                amatrix[lin][col] -= amatrix[diag][col] * aux

    return amatrix


def print_matrix(amatrix):
    for line in amatrix:
        for i,c in enumerate(line):
            if i != len(line) - 1:
                print("%.05f" % c, end=" ")
            else:
                print("| %.05f" % c)
