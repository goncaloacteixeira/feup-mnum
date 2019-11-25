import numpy as np

"""
    Resolver X sendo uma matriz A*X = b
"""

matrixA = [[7, 2, 0],
           [4, 10, 1],
           [5, -2, 8]]

colB = [24, 27, 27]

"""
    Gauss-Jacobi
    
    Basicamente é o método de Picard-Peano
    a regra é definida por recursão:
    
    o novo Xj é dado por:
    Xj = (b[j] - (A[j][0] * x[0] + A[j][1] * x[1] + A[j][2] * x[2])) / A[j][j]
    
    sendo que j é o indice da linha da matriz
"""


def gaussJacobi(A, b, N=25, x=None, info=True):
    if x is None:
        x = [0 for i in A[0]]

    for i in range(N):
        aux = []
        for j in range(len(A[0])):
            x1 = (b[j] - (A[j][0] * x[0] + A[j][1] * x[1] + A[j][2] * x[2])) / A[j][j]
            aux.append(x1)
        x = [x[i] + aux[i] for i in range(len(x))]

        if info:
            eps = residue(x, A, b)
            print("iteration %i" % i)
            for j in range(len(x)):
                print("x%i: %f\teps%i: %f" % (j, x[j], j, eps[j]))

    return x


"""
    Gauss-Seidel
    
    Neste caso as novas soluçoes xj são substituidas no calculo de x(j+1)
    
    converge mais rapidamente
"""


def gaussSeidel(A, b, N=25, x=None, info=True):
    if x is None:
        x = [0 for i in A[0]]

    for i in range(N):
        for j in range(len(A[0])):
            x1 = (b[j] - (A[j][0] * x[0] + A[j][1] * x[1] + A[j][2] * x[2])) / A[j][j]
            x[j] += x1

        if info:
            eps = residue(x, A, b)
            print("iteration %i" % i)
            for j in range(len(x)):
                print("x%i: %f\teps%i: %f" % (j, x[j], j, eps[j]))

    return x


"""
    Uma melhor implementação para calculo do residuo
    em sistemas lineares.
    
    esta implementação requer 
        uma matriz coluna X (solução)
        uma matriz A
        uma matriz coluna b
        
    devolve uma matriz coluna com os valores do residuo                 
"""
def residue(sol, originalA, originalb):
    res = [0 for i in sol]
    for i in range(len(originalA)):
        for j in range(len(originalA)):
            res[i] += originalA[i][j] * sol[j]

    return [abs(res[i] - originalb[i]) for i in range(len(sol))]
