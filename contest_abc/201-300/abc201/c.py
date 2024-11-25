s = input()
exists = []
not_exists = []
i = 0
for i, moji in enumerate(s) :
  if moji == 'o' :
    exists.append(i)
  elif moji == 'x' :
    not_exists.append(i)

ans = 0
for i in range(0, 10**4) :
  com = str(format(i, '04d'))
  f = True
  for e in exists :
    if str(e) not in com :
      f = False
  for e in not_exists :
    if str(e) in com :
      f = False
  if f :
    ans += 1
print(ans)