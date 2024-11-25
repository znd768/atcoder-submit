s = input()
n = int(input())
sl = len(s)
at_least = ''
for i, m in enumerate(s):
  if m == '?':
    at_least += '0'
  else:
    at_least += m
if int(at_least, 2) > n :
  print(-1)
  exit()

ans = ''
for i, m in enumerate(s):
  if m == '?':
    if i < n - 1:
      tmp = int((ans + '1' + at_least[i+1:]), 2)
    else:
      tmp = int((ans + '1'), 2)
    if tmp <= n:
      ans += '1'
    else:
      ans += '0'
  else:
    ans += m
print(int(ans,2))