"""
s = input()
if int(s[3:]) < 350 and int(s[3:]) != 316 and s[3:] != '000':
  print('Yes')
else :
  print('No')

n, q = map(int, input().split())
l = list(map(int, input().split()))

---------------------------------------------
ans = n
s = set()
for e in l :
  if l.count(e) % 2 == 0 : continue
  elif e not in s :
    ans -= 1
  s.add(e)
print(ans)
-------------------------------------
n = int(input())
l = list(map(int, input().split()))
cnt = 0
outputL = []
indexL = [None for _ in range(n+1)]
for i in range(n) :
  indexL[l[i]] = i
for i in range(n) :
  if l[i] != i + 1 :
    tmp = indexL[i+1]
    l[i], l[tmp] = l[tmp], l[i]
    indexL[l[tmp]] = tmp
    outputL.append([i+1, tmp+1])
    cnt += 1

print(cnt)
for e in outputL :
  print(e[0], e[1])
"""

import math
import heapq
n, m = map(int, input().split())
lv = [list() for _ in range(n)]
for _ in range(e) :
  s, t = map(int, input().split())
  lv[s].append(t)

ans = 0
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

