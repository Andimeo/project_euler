gcd = lambda a, b: a if b == 0 else gcd(b, a % b)

N = 12001

ans = 0
for i in range(2, N):
    if i % 1000 == 0:
        print('processing ...', i)
    # print(i, ': ', sep='', end='')
    for j in range((i + 2) // 3, (i + 1) // 2):
        if gcd(i, j) == 1:
           ans += 1
           # print(j, end=', ')
    # print()
    # input()
print(ans - 1)
