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

if __name__ == '__main__':
  n, m = map(int, input().split())
  t = divisor(m)
  for d in t:
    if d * n <= m:
      ans = d
  print(ans)