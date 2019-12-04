"""
        Minimização Unidimensional

    min(fx)

    calcular minimo de uma função utilizando um guess

    -> guess

    1º pesquisa para enquadrar num intervalo
        (esq. ou dir.)
        passo constante ou variavel
    2º redução intervalar
        terços
        secção aurea
    3º ajuste quádricas

"""

"""
            Triseção
    
    com um intervalo temos de criar 2 pontos nesse intervalo para 
    termos 3 novos intervalos
    1 deles podemos descartar vendo a configuração dos pontos
    
    razao = 3.0
    while abs(b-a) > prec:
        c = a + (b-a)/razao
        d = b - (b-a)/razao
        if f(c) < f(d):
            b = d
        else:
            a = c
"""

"""
        Secção Aurea
        
    B = proporção aurea = (sqrt(5) - 1) / 2
    
    igual a triseção
    
    c = a + (b-a) * B
    d = b - (b-a) * B

    fc = f(c)
    fd = f(d)

    while abs(b-a) > prec:
        if fc < fd:
            b = d
            d = c
            fd = fc
            c <- novo --- c = a + B * (b-a)
            fc = f(c)
        else:
            a = c
            c = d
            fc = fd
            d <- novo --- d = b - B * (b-a)
            fd = f(d)
            
"""

"""
        Ajuste da Quádrica
        
    Não é um método iterativo, basta aplicar uma fórmula
    
    
                    h * (f(x1) - f(x3)  
    x = x2 - -------------------------------- 
               2 * (f(x1) - 2*f(x2) + f(x3))
               

    h = x2 - x1;
    h = x3 - x2;
    h = (x3 - x2) / 2
    
"""

"""
    Exemplo da aula
    
    Minimizar a função sin2(x)
"""

from math import sqrt, sin, pi

"""
    avaliar o minimo de 2 a 4
"""


def func(x):
    return sin(x) ** 2


def intervalSearch(x0, x1, f, h=0.5):
    # passo constante

    a = x0
    b = a + h

    if f(b) < f(a):
        a += h
        b += h
        while True:
            if f(b) < f(a):
                a += h
                b += h
            else:
                break

    return [a, b]


def aureaSec(rangeVal, f, prec=0.1):
    # B = proporção
    B = (sqrt(5) - 1) / 2

    a = rangeVal[0]
    b = rangeVal[1]

    c = a + (b - a) * B
    d = b - (b - a) * B

    fc = f(c)
    fd = f(d)

    while abs(b - a) > prec:
        if fc < fd:
            b = d
            d = c
            fd = fc
            c = a + B * (b - a)
            fc = f(c)
        else:
            a = c
            c = d
            fc = fd
            d = b - B * (b - a)
            fd = f(d)

    return [a, b]


def quadAdjust(points, f):
    x1 = points[0]
    x3 = points[1]
    x2 = (x1 + x3) / 2.0

    h = x2 - x1

    return x2 - (h * (f(x1) - f(x3))) / (2 * (f(x1) - 2 * f(x2) + f(x3)))


interval = intervalSearch(2, 4, func, h=0.0000001)
print("interval after search:", interval)
interval = aureaSec(interval, func, prec=0.0000000001)
print("interval after aurea section:", interval)
min = quadAdjust(interval, func)
print("min calc:", min)
print("f(min):", func(min))
print("rel. error:", ((min - pi) / pi) * 100.0, "%")
