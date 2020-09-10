from collections import Counter

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

N = 10 ** 4
p = sieve(N)

ps = list(filter(lambda x: x > 1000, p))
pset = set(ps)

for i in range(len(ps)):
    for j in range(i):
        pi, pj, pk = ps[i], ps[j], ps[j] - (ps[i] - ps[j])
        if pk in pset and Counter(str(pi)) == Counter(str(pj)) == Counter(str(pk)):
                print(pk, pj, pi)
