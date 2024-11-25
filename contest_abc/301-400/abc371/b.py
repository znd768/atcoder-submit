n, m = map(int, input().split())
a = [False for _ in range(n)]
ans = []
for _ in range(m) :
  n, s = input().split()
  n = int(n) - 1
  if not a[n] and s == "M" :
    ans.append('Yes')
    a[n] = True
  else :
    ans.append('No')
print('\n'.join(ans))
