def function(t,T):
    return -0.25*(T-37)


def euler(h, t, T, f, N=2):
    for i in range(N):
        t += h
        T += h * f(t, T)
    return T


if __name__ == "__main__":
    print("T: %.05f" % euler(0.4,5,3,function))
