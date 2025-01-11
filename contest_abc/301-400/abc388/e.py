import math

n = int(input())
half_n = n // 2
al = list(map(int, input().split()))
smaller = al[:half_n]
bigger = al[half_n:]
ans = 0
cursor = 0
for sn in smaller:
    while cursor < math.ceil(n/2):
        if sn*2 <= bigger[cursor]:
            ans += 1
            cursor += 1
            break
        cursor += 1
print(ans)