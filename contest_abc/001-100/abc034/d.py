n, k = map(int, input().split())
wp = [list(map(int, input().split())) for _ in range(n)]
lo = 0.0
hi = 100.0
for i in range(50) :
  mi = (lo + hi) / 2
  l = []
  for j in range(n) :
    l.append((wp[j][1] - mi) * wp[j][0])
  l.sort(reverse=True)
  s = 0.0
  for j in range(k) :
    s += l[j]
  if s < 0.0 : hi = mi
  else : lo = mi
print(hi)