s = 1
v = 1
for i in range(1, 501):
    s += 4*(v + 5 * i)
    v = v + 8 * i

print(s, v)
