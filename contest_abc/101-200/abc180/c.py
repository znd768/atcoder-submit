n = int(input())

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

ans = divisor(n)
for a in ans:
  print(a)