from linear_systems import gaussian_elimination as gauss

"""
    @:param sol Solução da matrix representada por @:param original
    
    Calcula o resíduo de uma certa solução
    
    função muito mal implementada -> melhor solução no ficheiro gauss_jacobi_seidel
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


"""
    Para ajustar a nossa solução podemos adicionar o residuo (res0) à solução previamente
    determinada (sol0) e obter então uma nova solução (sol1)
    
    Se o residuo desta nova solução (res1) for menor que res0 então podemos dizer que melhoramos 
    a nossa solução caso contrário, a sol0 é melhor que a sol1 e paramos por aqui.
"""


def adjust(sol, res):
    for i in range(len(res)):
        sol[i][3] += res[i]
    return sol


def example3():
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

    sol1 = adjust(sol0, res0)
    print("\nSolution X1")
    gauss.printMatrix(sol1)
    print("\nResidue X1")
    res1 = residue(sol1, m)
    printResidue(res1)

    print("\nUma vez que res1 é maior que res0 a solução X0 é melhor.")


"""
    Fim do exemplo
"""
