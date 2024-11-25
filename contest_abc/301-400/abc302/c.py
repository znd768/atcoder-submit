import itertools
n, m = map(int, input().split())
sl = [input() for _ in range(n)]
for l in itertools.permutations(sl):
  for i in range(n-1):
    cnt = 0
    flg = True
    for j in range(m):
      if l[i][j] != l[i+1][j]:
        cnt += 1
    if cnt != 1:
      flg = False
      break
  if flg:
    print('Yes')
    exit()
print('No')