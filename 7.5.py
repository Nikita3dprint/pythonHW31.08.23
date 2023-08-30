for n in range(200, 1, -1):
    n -= n % 4
    b = bin(n)[2:]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    r = int(b, 2)
    if r < 64:
        print(n)
        break
