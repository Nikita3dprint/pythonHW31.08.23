k = 0
for x in range(4):
    for y in range(4):
        for z in range(4):
            if (x >= y) and (y >= z):
                k += 1
                print(str(x)+str(y)+str(z))
print(k)
