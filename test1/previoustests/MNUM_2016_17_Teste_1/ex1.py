def func(x):
    return (0.662*x - 1) / (x - 1)
def g(x):
    return 1.0/0.662

def bissec(funcao, a, b, precisao):
    count = 0
    while abs(a-b) > precisao:
        m = (a+b)/2.0
        if funcao(a)*funcao(m) <= 0.0:
            b = m
        else:
            a = m
        count += 1
    print("Iteraçoes: ", count)
    print("result: ", end="")
    return (a+b)/2.0

print("alinea b)")

def picardPeano(funcao, guess, precisao):
    count = 0
    while abs(guess-funcao(guess)) > precisao:
        guess = funcao(guess)
        count += 1
    print("Iteraçoes: ", count)
    print("result: ", end="")
    return guess

print("Bissec")
print(bissec(func, -5, 2, 0.0001))
print("Picard")
print(picardPeano(g, -2, 0.0001))