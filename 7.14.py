x = 4 ** 700 + 4 ** 100 - 16 ** 100 - 64
k = 0
while x > 0:
    if x % 4 == 3:
        k += 1
    x = x // 4
print(k)
