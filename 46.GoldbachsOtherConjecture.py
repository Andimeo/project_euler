import math

def sieve(limit):
    ans = []
    a = [1] * limit
    a[0] = a[1] = 0
    for i in range(2, limit):
        if a[i] == 0:
            continue
        ans.append(i)
        for j in range(i*i, limit, i):
            a[j] = 0;
    return ans

is_square = lambda x: int(math.sqrt(x) + 1e-9) ** 2 == x

N = 10 ** 6

p = sieve(N)
ps = set(p)
for i in range(9, N, 2):
    if i in ps:
        continue
    found = False
    for j in p[1:]:
        if j > i:
            break
        q = (i - j) // 2
        if is_square(q):
            found = True
            break
    if not found:
        print(i)
        break

