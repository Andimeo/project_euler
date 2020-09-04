import numpy as np

N = 2001001
t = np.ones(N)
t[0] = t[1] = 0

for i in range(2, N):
    if t[i] == 0:
        continue
    for j in range(i * i, N, i):
        t[j] = 0

p = set(i for (i, v) in enumerate(t) if v == 1)

i, j = 0, 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        l = 0
        while l * l + a * l + b in p:
            l += 1
        if l > j:
            j = l
            i = a * b
            if j == 71:
                print(a, b)

print(i, j)
