s = [9, 2*90, 3*900, 4*9000, 5*90000, 6*900000]

def f(n):
    i = 0
    while n > s[i]:
        n -= s[i]
        i += 1
    p = (n - 1) / (i + 1)
    num = 10 ** i + p
    q = (n - 1) % (i + 1)
    return int(str(num)[q])

for i in range(7):
    print(10**i, f(10**i))


