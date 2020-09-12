from collections import Counter

for x in range(1, 10**6):
    if all(Counter(str(x)) == Counter(str(x*y)) for y in range(2, 7)):
        print(x)
        break
