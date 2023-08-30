def mndel(a):
    for x in range(2, a):
        if a % x == 0:
            return x
    return 0


def mxdel(b):
    for y in range(b-1, 1, -1):
        if b % y == 0:
            return b
    return 0

z = 850001
n = 0
while n < 6:
    f = mxdel(z) - mndel(z)
    if (f != 0) and (f % 3 == 0):
        print(z, f)
        n += 1
    z += 1
