import math

"""
    Problema:

    dy
   ----  = sen(x)      p(0,0)
    dx

     sol. geral             sol. particular
    y = -cos(x) + C  ---->  y = -cos(x) + 1


    em todos os métodos delta(xn) é arbitrado

    a solução mais simples para esse algoritmo é delta(xn)
    ter um valor constante

    delta(xn) tem duas estratégias:
        - passo variavel (depende do erro)
        - passo constante

    delta(yn) depende do método

    { xn+1 = xn + deltax
    { yn+1 = yn + deltay


    Controlo do erro usando o QC
"""

"""
    EULER
    delta(yn) = delta(xn)*f(xn,yn)
"""

"""
    RK-4
    necessita de 4 estimas do incremento y para fazer uma media
    ponderada
    
    delta-1 = delta(xn)*f( xn, yn )
    delta-2 = delta(xn)*f( (xn+delta(xn)) / 2, (yn+delta-1) / 2 )
    delta-3 = delta(xn)*f( (xn+delta(xn)) / 2, (yn+delta-2) / 2 )
    delta-4 = delta(xn)*f( xn+delta(xn), yn+delta-3 )
    
    delta(yn) = delta-1/6.0 + delta-2/3.0 + delta-3/3.0 + delta-4/6.0   
"""

"""
                 QC
            xn      xn+1
    
    P   com delta(xn)                         
    P'  com 2 passos delta(xn)/2
    P'' com 4 passos delta(xn)/4
    
    QC = (P' - P) / (P'' - P')
        se QC ~ 2
        eps'' ~ (P'' - P')/(2^n - 1)
    
"""


def func(x):
    return math.sin(x)


def batota(x):
    return -math.cos(x) + 1


def euler(deltaxn, func, N=5):
    x = 0
    y = 0
    yBat = batota(x)
    for i in range(N-1):
        print("x:", x)
        print("y(batota):", yBat)
        print("y(calcul):", y)
        print()
        x += deltaxn
        y += deltaxn * func(x)
        yBat = batota(x)


euler(0.01, func)
