n = int(input())
s = input()
t = input()
for i in range(n):
  if s[i] == t[i]:
    continue
  elif s[i] in ('1', 'l') and t[i] in ('1', 'l'):
    continue
  elif s[i] in ('0', 'o') and t[i] in ('0', 'o'):
    continue
  else:
    print('No')
    exit()
print('Yes')