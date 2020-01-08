def function(x):
    return x**7 + 0.5*x - 0.5

def corda(func,a,b,N=20):
    print("Iteration 0")
    print("x: %.06f" % a)
    for i in range(1,N+1):
        rr = (a * func(b) - b * func(a)) / (func(b) - func(a));
        if func(a) * func(rr) <= 0.0:
            b = rr;
        else:
            a = rr;
        print("Iteration",i)
        print("x: %.06f" % a)

    return a,b


if __name__ == "__main__":
    corda(function,0,0.8,3)
    print()
    corda(function,0.8,0.656044,3)
    print()
    corda(function,0.656044,0.8,3)





