# https://www.mathblog.dk/project-euler-75-lengths-of-wire-right-angle-triangle/
# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Pythag/pythag.html#section2


import math
N = 1500000 + 1
M = int(math.sqrt(N // 2))

l = [0] * N
is_primitive = [False] * N

gcd = lambda a, b: a if b == 0 else gcd(b, a%b)

for m in range(1, M):
    for n in range(m % 2 + 1, m, 2):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if a+b+c <= N and gcd(m, n) == 1:
            l[a+b+c] += 1
            is_primitive[a+b+c] = True

for i in range(1, N):
    if is_primitive[i]:
        for j in range(i + i, N, i):
            l[j] += l[i]

print(sum(1 for v in l if v == 1))
