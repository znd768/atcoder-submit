h, w = map(int, input().split())
r, c = map(int, input().split())
ans = 0
if r - 1 > 0 : ans += 1
if r < h : ans += 1
if c - 1 > 0 : ans += 1
if c < w : ans += 1
print(ans)