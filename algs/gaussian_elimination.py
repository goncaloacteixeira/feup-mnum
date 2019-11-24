"""
    matrix é uma list bidimensional do seguinte tipo:

    a1x     b1y     c1z     a
    a2x     b2y     c2z     b
    a3x     b3y     c3z     c

    [ [a1, b1, c1, a],
      [a2, b2, c2, b],
      [a3, b3, c3, c]]
"""

# função para mostrar uma matriz 3 por 3
def printMatrix(amatrix):
    for line in amatrix:
        print(line[0], '  \t', line[1], ' \t', line[2], ' \t| ', line[3])

# função para fazer a diagonalização de um sistema linear
def diagonalization(amatrix):
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

    # triangularizar a parte de cima
    for diag in range(dimV - 1, -1, -1):
        for lin in range(diag - 1, -1, -1):
            aux = amatrix[lin][diag]
            for col in range(diag, dimV + 1):
                amatrix[lin][col] -= amatrix[diag][col] * aux

    """
        # no fim teremos uma matriz do tipo:
        
        1     0     0   |  x0
        0     1     0   |  y0
        0     0     1   |  z0
        
        em que a solução é {x0, y0, z0}
    """
    return amatrix

# exemplo do livro
m = [[3, 6, 9, 39],
     [2, 5, -2, 3],
     [1, 3, -1, 2]]

m1 = [[1,1,1,6],
      [1,2,2,9],
      [2,1,3,11]]

m2 = [[1,2,-3,1],
      [3,-1,2,0],
      [2,1,1,2]]

# quando aparece "-0.0" é talvez porque o computador não consegue calcular o numero por ser infinitamente pequeno perto de zero
# pelo lado esquerdo da origem