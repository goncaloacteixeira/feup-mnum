def upperTriang(amatrix):
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

def lowerTriang(amatrix):
    dimV = len(amatrix)
    for diag in range(dimV - 1, -1, -1):
        for lin in range(diag - 1, -1, -1):
            aux = amatrix[lin][diag]
            for col in range(diag, dimV + 1):
                amatrix[lin][col] -= amatrix[diag][col] * aux

    return amatrix


def printMatrix(amatrix):
    for line in amatrix:
        print("%.05f %.05f %.05f %.05f | %.05f" % (line[0], line[1], line[2], line[3], line[4]))


if __name__ == "__main__":
    matrix = [[0.1, 0.5, 3, 0.25,0],
              [1.2, 0.2, 0.25, 0.2,1],
              [-1, 0.25, 0.3, 2,2],
              [2, 0.00001, 1, 0.4,3]]

    print("Alinea a)")
    printMatrix(upperTriang(matrix))
    print()
    print("Alinea b)")
    printMatrix(lowerTriang(upperTriang(matrix)))
