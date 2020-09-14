is_palindrome = lambda n: all(n[i] == n[-1-i] for i in range((len(n)+1)//2))

result = 0

for i in range(10000):
    is_lychrel = True
    n = i
    for j in range(50):
        n = n + int(str(n)[::-1])
        if is_palindrome(str(n)):
            is_lychrel = False
            break
    if is_lychrel:
        result += 1
print(result)
