result = 0

numerator, denominator = 3, 2
for i in range(1, 1000):
    numerator, denominator = numerator + 2 * denominator, numerator + denominator
    if len(str(numerator)) > len(str(denominator)):
        result += 1

print(result)
