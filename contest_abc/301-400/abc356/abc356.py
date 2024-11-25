#A
# n, l, r = map(int, input().split())
# ans = ''
# al = list(range(1, l))
# bl = list(range(r, l-1, -1))
# cl = list(range(r+1, n+1))
# print(' '.join(map(str, (al + bl + cl))))

# n, m = map(int, input().split())
# al = list(map(int, input().split()))
# mat = [list(map(int, input().split())) for _ in range(n)]
# suml = [0 for _ in range(m)]
# for j in range(n) :
#   for i in range(m) :
#     suml[i] += mat[j][i]
# # print(suml)
# ans = 'Yes'
# for i in range(m) :
#   if al[i] > suml[i] :
#     ans = 'No'
# print(ans)

import itertools
n, m, k = map(int, input().split())
l = [list(input().split()) for _ in range(m)]
keypl_f = []
keypl_s = []
for i, e in enumerate(l):
  re = e[int(e[0])+1]
  if re == 'o' :
    keypl_s.append(list(map(lambda x: int(x)-1, list(e[1:int(e[0])+1]))))
  else :
    keypl_f.append(list(map(lambda x: int(x)-1, list(e[1:int(e[0])+1]))))
ans = 0
for i in range(2**n) :
  flg = 1
  l = [0 for _ in range(n)]
  for j in range(n) :
    if ((i >> j) & 1) :
      l[j] = 1
  for e in keypl_s :
    tm = 0
    for u in e :
      tm += l[u]
    if tm < k :
      flg = 0
      break
  for e in keypl_f :
    tm = 0
    for u in e :
      tm += l[u]
    if tm >= k :
      flg = 0
      break
  if flg :
    ans += 1
print(ans)

n, m = map(int, input().split())
