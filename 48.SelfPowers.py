def pow(a, n, M):
    if n == 0:
        return 1
    v = pow(a, n // 2, M)
    v = v * v % M
    if n % 2 == 1:
        v = v * a % M
    return v

M = 10**10
ans = sum(pow(i, i, M) for i in range(1, 1001)) % M
print(ans)
