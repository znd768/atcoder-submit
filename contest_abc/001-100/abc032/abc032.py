n, m = map(int, input().split())
l = [[] for _ in range(n)]
for _ in range(m) :
  a, b = map(int, input().split())
  l[min(a,b)-1].append(max(a,b))
  
found = []
cnt = 0

def dfs(n) :
  found.append(n)
  for e in l[n-1] :
    if e not in found :
      dfs(e)

while len(found) != n :
  for i in range(n) :
    if i+1 not in found :
      dfs(i+1)
      if i != 0 :
        cnt += 1
      break
print(cnt)