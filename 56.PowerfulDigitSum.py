def binary_pow(a, b):
    if b == 0:
        return 1
    c = pow(a * a, b // 2)
    if b % 2 == 1:
        c = c * a
    return c

print(max(sum(ord(c) - ord('0') for c in str(binary_pow(a, b)))for a in range(1, 100) for b in range(1, 100)))
