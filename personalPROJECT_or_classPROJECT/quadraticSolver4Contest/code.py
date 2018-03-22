def quad():

  a = input()
  b = input()
  c = input()
  
  a = int(a)
  b = int(b)
  c = -(int(c) * 2)
  
  x1 = (-b + (((b ** 2) - 4 * a * c) ** .5)) / (2 * a)
  x2 = (-b - (((b ** 2) - 4 * a * c) ** .5)) / (2 * a)
  
  if (int(x1) == float(x1)):
    print(int(x1))
  elif (int(x2) == float(x2)):
    print(int(x2))
  else:
    print(0)
