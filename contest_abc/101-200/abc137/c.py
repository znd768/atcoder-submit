from collections import Counter

n = int(input())
sl = [input() for _ in range(n)]
d = Counter(["".join(sorted(s)) for s in sl])
ans = 0
for k, v in d.items():
    if v < 2:
        continue
    ans += v*(v-1)//2
print(ans)