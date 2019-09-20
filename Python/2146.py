while True:
  try:
    a = int(input())
    a = a - 1 
    print(a)
  except EOFError:
    break