from collections import Counter

l = list(map(int, input().split()))
c = Counter(l)
ans = 0
for key, value in c.items():
    if value < 2:
       continue
    ans += value // 2
print(ans)