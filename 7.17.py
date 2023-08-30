a = [int(x) for x in open('17var7.txt')]
k = 0
mxproz = -100000001
for i in range(len(a) - 1):
    if (a[i] % 2 != 0) and (a[i+1] % 2 != 0) and (a[i] % 10 == a[i+1] % 10):
        k += 1
        if abs(a[i] * a[i+1]) > mxproz:
            mxproz = abs(a[i] * a[i+1])
print(k, mxproz)
