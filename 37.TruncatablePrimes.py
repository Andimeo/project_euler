f = lambda x: x > 1 and all(x % i != 0 for i in range(2, x) if i * i <= x)
n = 10
num = 0
while num < 11:
  if n % 10 != 3 and n % 10 != 7:
    pass 
  elif not (set(int(x) for x in str(n)) <= set([1, 2, 3, 5, 7, 9])):
    pass
  else:
    for i in range(len(str(n))):
      x = int(str(n)[:len(str(n))-i])
      y = int(str(n)[i:])
      if not f(x) or not f(y):
        break
    else:
      num += 1
      print(n)
  n += 1
  if n % 100000 == 0:
    print('processing n...', n)
