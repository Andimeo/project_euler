import numpy as np

d = np.zeros((101, 101))
for i in range(101):
    d[i, 0] = 1
for i in range(1, 101):
    for j in range(1, i+1):
        d[i, j] = d[i-1, j] + d[i-1, j-1]

print(sum(1 for i in range(2, 101) for j in range(2, 101) if d[i, j] > 10**6))