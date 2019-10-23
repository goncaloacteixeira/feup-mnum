def func(x):
    return x**4 - 4*x**3 + x - 3

print("alinea a)")
print("R: 2 soluçoes")

print("alinea b)")
print("R: não enquadra em [1, 3.5]")

print("alinea c)")

def g1(x):
    return (4*x**2-1.0/x**2 + 3.0/x**3)**(1.0/3.0)

def g2(x):
    return 4 - 1.0/x**2 + 3.0/x**3

def g3(x):
    return -x**4 + 4*x**3 +3

guess = 1

# while abs(guess - g2(guess)) > 0.000001:
#     guess = g2(guess)
#     print(round(guess,4))
print("funcao 3 não converge para raiz")

print("ex 7")

from math import sin

def func7(x):
    return x**3 - 10*sin(x) + 2.8

a = 1.5
b = 4.2

for i in range(2):
    m = (b + a) / 2.0
    if (func7(a)*func7(m) <= 0.0):
        b = m
    else:
        a = m
print(round(b,4))