# 欧拉函数打表

N = 1000001

euler = [n for n in range(N)]
euler[0] = euler[1] = 0

for i in range(2, N):
    if euler[i] == i:
        for j in range(i, N, i):
            euler[j] = euler[j] // i * (i - 1)

print(sum(euler))
