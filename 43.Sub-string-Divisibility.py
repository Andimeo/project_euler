p = [2, 3, 5, 7, 11, 13, 17]
d = {}
for i in range(12, 987):
    s = '%03d' % i
    if len(set(c for c in s)) != 3:
        continue
    for v in p:
        if i % v == 0:
            if v not in d:
                d[v] = []
            d[v].append(s)

ans = []
def dfs(i, cur, s):
    if i == -1:
        print('s: ', s, len(s), len(set(c for c in s)))
        assert(len(set(c for c in s)) == 9)
        s = list(set(c for c in '0123456789') - set(s))[0] + s
        ans.append(s)
        return
    candidates = list(filter(lambda x: x[1:] == cur[:2] and x[0] not in set(c for c in s), d[p[i]]))
    for c in candidates:
        dfs(i-1, c, c[0] + s)

for cur in d[17]:
    dfs(5, cur, cur)

print(sum(int(x) for x in ans))
print(sum(int(x) for x in ans if x[0] !='0'))
print(sorted(ans))
