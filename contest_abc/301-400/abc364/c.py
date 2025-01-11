from itertools import accumulate

n, max_sweet, max_salty = map(int, input().split())
sweet_val = list(map(int, input().split()))
salty_val = list(map(int, input().split()))

sweet_val.sort(reverse=True)
salty_val.sort(reverse=True)
accumulated_sweet = 0
accumulated_salty = 0
ans = n
for idx, (swe_val, sal_val) in enumerate(zip(sweet_val, salty_val), start=1):
    accumulated_sweet += swe_val
    accumulated_salty += sal_val
    if accumulated_sweet > max_sweet or accumulated_salty > max_salty:
        ans = idx
        break
print(ans)
