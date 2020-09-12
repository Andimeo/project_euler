from collections import Counter

for x in range(1, 10**6):
    if Counter(str(x)) == Counter(str(x*2)) == Counter(str(x*3)) == Counter(str(x*4)) == Counter(str(x*5)) == Counter(str(x*6)):
        print(x)
        break
