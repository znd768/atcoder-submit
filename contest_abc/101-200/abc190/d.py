def divisor(n):
  i = 1
  table = []
  while i * i <= n:
    if n % i == 0:
      table.append(i)
      if i != n // i:
        table.append(n // i)
    i += 1
  return sorted(table)

if __name__ == "__main__":
  n = int(input())
  print(sum([2 for x in divisor(n) if x % 2 == 1]))