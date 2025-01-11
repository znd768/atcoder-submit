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

# x + y = n
cnt = 0
for x in range(1, n):
    y = n - x
    cnt += len(divisor(x)) * len(divisor(y))
print(cnt)