"""
n, m = map(int, input().split())
#xy = [map(int, input().split()) for _ in range(m)]
#x, y = [list(i) for i in range(*xy)]

l = [[] for _ in range(n)]
for _ in range(m) :
  x, y = map(int, input().split())
  l[x-1].append(y)
ans = ''
for i in range(len(l)) :
  if len(set(l[i])) > 1 :
    ans = -1
    break
  elif len(set(l[i])) == 1 :
    if i == 0 and n > 1 and l[i][0] == 0 :
      ans = -1
      break
    else :
      ans += str(l[i][0])
  else :
    if i == 0 and n == 1 :
      ans = '0'
    elif i == 0 :
      ans += '1'
    else : ans += '0'
print(ans)
"""
n, m, k = map(int, input().split())
friends = [[] for _ in range(n)]
blocklist = [[] for _ in range(n)]
for _ in range(m) :
  a, b = map(lambda x: int(x)-1, input().split())
  friends[min(a, b)].append = max(a, b)
for _ in range(k) :
  a, b = map(lambda x: int(x)-1, input().split())
  blocklist[min(a, b)].append = max(a, b)

possibleNumList = [0 for _ in range(n)]

comp = []
def dfs(n) :
  found.append(n)
  comp.append(n)
  global cnt
  cnt += 1
  for e in friends[n-1] :
    if e not in found :
      dfs(e)

while len(comp) != n :
  cnt = 0
  found = []
  for i in range(n) :
    if i+1 not in found :
      dfs(i+1)
      for i in range(found) :
        possibleNumList
      break

