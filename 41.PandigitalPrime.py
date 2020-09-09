import itertools

f = lambda x: x > 1 and all(x % i != 0 for i in range(2, x+1) if i * i <= x)
m = -1
for n in range(7, 3, -1):
    for perm in itertools.permutations(range(1, n+1)):
        num = int(''.join([str(x) for x in perm]))
        if f(num):
            print(num)
            m = max(m, num)
print(m)
