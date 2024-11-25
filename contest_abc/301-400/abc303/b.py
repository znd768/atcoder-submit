import math
n, m = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(m)]
s = set()
for row in rows:
  for i in range(n - 1):
    s.add((min(row[i], row[i + 1]), max(row[i], row[i + 1])))
    # print(f"{i = }, {row = }")
print(math.comb(n, 2)-len(s))