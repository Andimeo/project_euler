d = [1, 5]
s = set(d)
n = 2

def add_to_d(num):
    global n
    while d[-1] < num:
        n += 1
        d.append(n * (3*n - 1) // 2)
        s.add(d[-1])

ans = -1
j = 1
while j < len(d):
    i = j - 1
    add_to_d(d[j] + d[i])
    while i >= 0:
      if d[j] + d[i] in s and d[j] - d[i] in s:
        print(i, j, d[i], d[j])
        ans = d[j] - d[i]
        break
      i -= 1
    if ans != -1:
        break
    j += 1

print(ans)
