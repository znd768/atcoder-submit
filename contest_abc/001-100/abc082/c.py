from collections import Counter
n = int(input())
al = list(map(int, input().split()))

c = Counter(al)
ans = 0
for k, v in c.items():
  if k > v:
    ans += v
  else:
    ans += v - k

print(ans)