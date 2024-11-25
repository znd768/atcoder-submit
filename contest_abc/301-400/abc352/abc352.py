"""
n, x, y, z = map(int, input().split())
if z in range(min(x, y), max(x, y) + 1) :
  print('Yes')
else : print('No')
"""

"""
s = input()
t = input()
output = []
offset = 0
for e in s :
  a = t.index(e) + 1
  output.append(a+offset)
  t = t[a:]
  offset += a

for e in output :
  print(e, end=' ')
"""

"""
n = int(input())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]
s = sum(a)
mx = 0
for i in range(n) :
  mx = max(mx, s-a[i]+b[i])
print(mx)
"""
import math
import heapq
n, m = map(int, input().split())

lv = [list() for _ in range(n)]
for _ in range(e) :
  s, *t = map(int, input().split())
  lv[s].append(t)

lans = [math.inf for _ in range(v)]
lans[r] = 0
heapl = []
heapq.heappush(heapl, (lans[r], r))
seen = set()
while len(heapl) != 0 :
  h = heapq.heappop(heapl)
  if h[0] > lans[h[1]] : continue
  seen.add(h[1])
  for e in lv[h[1]] :
    lans[e[0]] = min(lans[h[1]]+e[1], lans[e[0]])
    if e[0] not in seen :
      heapq.heappush(heapl, (lans[e[0]], e[0]))

for e in lans :
  if e == math.inf :
    print('INF')
  else : print(e)