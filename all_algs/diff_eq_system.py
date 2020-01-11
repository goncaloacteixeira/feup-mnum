def euler(deltaX, x, y, z, xf, dy, dz):
    print("Iteration 0")
    print("x: %.05f" % x)
    print("y: %.05f" % y)
    print("z: %.05f" % z)
    i = 1
    while x < xf:
        x += deltaX
        deltaY = dy(x, y, z)
        deltaZ = dz(x, y, z)
        y += deltaY * deltaX
        z += deltaZ * deltaX
        print("Iteration", i)
        print("x: %.05f" % x)
        print("y: %.05f" % y)
        print("z: %.05f" % z)
        i += 1

    return y, z


def runga_kutta_4(deltaX, x, y, z, xf, dy, dz):
    print("Iteration 0")
    print("x: %.05f" % x)
    print("y: %.05f" % y)
    print("z: %.05f" % z)
    i = 1
    while x < xf:
        x += deltaX
        dY1 = dy(x, y, z) * deltaX
        dZ1 = dz(x, y, z) * deltaX
        dY2 = deltaX * dy(x + deltaX / 2, y + dY1 / 2, z + dZ1 / 2)
        dZ2 = deltaX * dz(x + deltaX / 2, y + dY1 / 2, z + dZ1 / 2)
        dY3 = deltaX * dy(x + deltaX / 2, y + dY2 / 2, z + dZ2 / 2)
        dZ3 = deltaX * dz(x + deltaX / 2, y + dY2 / 2, z + dZ2 / 2)
        dY4 = deltaX * dy(x + deltaX, y + dY3, z + dZ3)
        dZ4 = deltaX * dz(x + deltaX, y + dY3, z + dZ3)
        y += (dY1 / 6 + dY2 / 3 + dY3 / 3 + dY4 / 6)
        z += (dZ1 / 6 + dZ2 / 3 + dZ3 / 3 + dZ4 / 6)

        print("Iteration", i)
        print("x: %.05f" % x)
        print("y: %.05f" % y)
        print("z: %.05f" % z)
        i += 1
    return y, z


def convergence_quotient(deltaX, x, y, z, xf, dy, dz, method):
    print("\n", method.__name__)
    print("h=%.05f" % deltaX)
    y0, z0 = method(deltaX, x, y, z, xf, dy, dz)
    print("\nh=%.05f" % (deltaX / 2))
    y1, z1 = method(deltaX / 2, x, y, z, xf, dy, dz)
    print("\nh=%.05f" % (deltaX / 4))
    y2, z2 = method(deltaX / 4, x, y, z, xf, dy, dz)

    quotient_y = (y1 - y0) / (y2 - y1)
    quotient_z = (z1 - z0) / (z2 - z1)

    error_y = (y2 - y1) / (round(quotient_y) - 1)
    error_z = (z2 - z1) / (round(quotient_z) - 1)

    print("CQ(y): %.05f" % quotient_y)
    print("Error(y): %.05f" % error_y)

    print("CQ(z): %.05f" % quotient_z)
    print("Error(z): %.05f" % error_z)

    return quotient_y, quotient_z

convergence_quotient.__doc__ = "Takes diff eq of the type dY(x,y,z)"