import gaussian_elimination as gauss

"""
    @:param sol Solução da matrix representada por @:param original
    
    Calcula o resíduo de uma certa solução
"""


def residue(sol, original):
    res = [0, 0, 0]
    for i in range(len(original)):
        for j in range(len(original)):
            res[i] += original[i][j] * sol[j][3]

    return [res[i] - original[i][3] for i in range(len(sol))]


def printResidue(res):
    print("epsX: ", res[0])
    print("epsY: ", res[1])
    print("epsZ: ", res[2])

"""
    Exemplos para o calculo de resíduos de soluções
    de sistemas lineares usando o método de eliminação de Gauss
"""

def example1():
    m = [[3, 6, 9, 39],
         [2, 5, -2, 3],
         [1, 3, -1, 2]]

    print("Original")
    gauss.printMatrix(m)
    print("\nSolution X0")
    sol0 = gauss.diagonalization(m)
    gauss.printMatrix(sol0)
    print("\nResidue X0")
    res0 = residue(sol0, m)
    printResidue(res0)
    print("Como esta solução é 'perfeita' o resíduo é {0, 0, 0}")


def example2():
    m = [[3, 6, 9, 39],
         [2, 5, -2, 3],
         [1, 3, -1, 2]]

    sol0 = [[1, 0, 0, 1.95],
            [0, 1, 0, 1.02],
            [0, 0, 1, 2.99]]

    print("Original")
    gauss.printMatrix(m)
    print("\nSolution X0")
    gauss.printMatrix(sol0)
    print("\nResidue X0")
    res0 = residue(sol0, m)
    printResidue(res0)

"""
    Fim dos exemplos
"""