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

p_num = [0, 0]
dp = [0, 0]

for i in range(2, N):
    n = i
    j = 0
    p_num_i = 0
    # print('For ', i, ': ')
    while n > 1 and j < len(p):
        if n % p[j] == 0:
            p_num_i += 1
        p_num_i_j = 0
        while n % p[j] == 0:
            n /= p[j]
            p_num_i_j += 1
        j += 1
        # if p_num_i_j > 0:
            # print(p[j-1], '^', p_num_i_j, sep='')
    # print('')
    if n != 1:
        p_num_i += 1
        # print(n, '^', 1, sep='')
    p_num.append(p_num_i)
    dp.append(dp[-1] + 1 if p_num_i == 4 else 0)
    if dp[i] == 4:
        print(i-3, i-2, i-1, i)
        break
    if i % 10000 == 0:
        print('processing ...', i)
