import numpy as np

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

N = 10**6
p = sieve(N)
print(len(p))

ps = set(p)
dp = [1] * len(p)

for i in range(len(p)):
    s = p[i]
    for j in range(i - 1, -1, -1):
        s += p[j]
        if s > N:
            break
        if s in ps:
            dp[i] = i - j + 1

ind = np.argmax(dp)
print(sum(p[ind - dp[ind] + 1 : ind + 1]))
