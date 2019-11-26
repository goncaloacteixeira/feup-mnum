import math
from numpy import arange # usada para fazer um loop com floats

# função-exemplo para teste
def func1(x):
    return math.sin(x)

# função-exemplo para segunda derivada de teste
def diffdifffunc1(x):
    return -math.sin(x)


"""
    Regra dos trapézios
    
    É possivel calcular um integral definido através da divisão da area que queremos calcular em pequenos
    trapézios.
"""


def trapezoidalRule(x0, x1, f, N):
    res = 0;
    h = abs((x1 - x0) / N)
    x = x0 + h

    for i in range(N - 1):
        res += f(x)
        x += h

    return h * (f(x0) + f(x1) + 2 * res) / 2


# calcula o erro de acordo com a formula (4.3)
def calcErroTrap(x0, x1, diffdiff, N):
    h = abs((x1 - x0) / N)

    aux = 0
    for i in arange(x0, x1 + 0.001, 0.001):
        if abs(diffdiff(i)) > abs(aux):
            aux = diffdiff(i)
    return -(x1 - x0) * aux * h ** 2 / 12

# diferença entre o valor calculado analiticamente e o valor calculado
# pela regra dos trapézios
def erroObs(real, cal):
    return abs(real - cal)


x0 = 0
x1 = math.pi/2
N = 80
expected = 1

res = trapezoidalRule(x0, x1, func1, N)
print("Resultado:", res)
print("Erro Cal.:", calcErroTrap(x0, x1, diffdifffunc1, N))
print("Erro Obs.:", erroObs(expected, res))
