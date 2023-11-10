result = []
def divider(a, b, reise=None):
  if a < b:
    raise ValueError
  if b > 100:
    reise IndexError
  return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}

for key in data:
  res = divider(key, data[Kem])
  result.append(res)

  print(result)
