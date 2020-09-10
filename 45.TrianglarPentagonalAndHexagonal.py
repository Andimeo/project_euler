import math

a = 286

def is_square(n):
    x = int(math.sqrt(n) + 1e-9)
    return x * x == n

def sqrt(n):
    return int(math.sqrt(n) + 1e-9)

while True:
    r = a ** 2 + a
    sb, sc = 1 + 12 * r, 4 + 16 * r
    if is_square(sb) and (1 + sqrt(sb)) % 6 == 0 and is_square(sc) and (2 + sqrt(sc)) % 8 == 0:
        b, c = (1 + sqrt(sb)) // 6, (2 + sqrt(sc)) // 8
        print(a, b, c, a * (a + 1) // 2, b * (3 * b - 1) // 2, c * (2 * c - 1))
        break
    a += 1
    if a % 10000 == 0:
        print('processing ...', a)
