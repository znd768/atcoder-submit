n = int(input())
s = input()
if '/' not in s or s.count('/') != 1:
  print('No')
  exit()
left, right = s.split('/')

if len(left) == len(right):
  ls = set(left)
  rs = set(right)
  if len(ls) == len(rs):
    if len(ls) == 0 or ls.pop() == '1' and rs.pop() == '2':
      print('Yes')
      exit()
print('No')