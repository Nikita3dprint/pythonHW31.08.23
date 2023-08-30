for a in range(1000, 1, -1):
    k = 1
    for x in range(1, 100):
        if ((x % a == 0) or ((x % 24 != 0) or (96 % x != 0))) == 0:
            k = 0
    if k == 1:
        print(a)
        break
