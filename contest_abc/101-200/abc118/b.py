from collections import Counter
n, m = map(int, input().split())
c = Counter()
for _ in range(n):
  c.update(list(map(int, input().split()))[1:])
ans = 0
for k, v in c.items():
  if v == n:
    ans += 1
print(ans)