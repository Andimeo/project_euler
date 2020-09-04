def f(d):
    i = 0
    s = {}
    n = 1
    while n > 0:
        p = n // d
        q = n % d
        print(p, q)
        if q in s:
            return i - s[q]
        s[q] = i
        i += 1
        n = q * 10
    return 0


idx = 0
length = 0
for d in range(2, 1000):
    if f(d) > length:
        length = f(d)
        idx = d

print(idx, length)
