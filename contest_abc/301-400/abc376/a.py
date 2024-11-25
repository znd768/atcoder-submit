#A
n, c = map(int, input().split())
tl = list(map(int, input().split()))
ans = 1
prev = tl[0]
for i in range(1, n):
  if tl[i] - prev < c:
    pass
  else:
    ans += 1
    prev = tl[i]
print(ans)