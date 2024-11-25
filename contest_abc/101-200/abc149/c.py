import math

def is_prime(num) :
  if num == 2 :
    return True
  elif num % 2 == 0 or num <= 1:
    return False
  for i in range(3, int(math.sqrt(num)) + 1, 2) :
    if num % i == 0 :
      return False
  return True

def raise_prime(n) :
  return [x for x in range(n + 1) if is_prime(x)]

if __name__ == "__main__":
  n = int(input())
  while True:
    if is_prime(n):
      print(n)
      break
    n += 1
  