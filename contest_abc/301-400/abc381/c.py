n = int(input())
s = input()
# s = '111/22//122/222/111/222/'
len_s = len(s)
# idx = [i for i, char in enumerate(s) if char == '/']
# print(idx)
ans = 1
start = s.find('1')
if start == -1:
  print(ans)
  exit()
cnt1 = 0
cnt2 = 0
rev = False
for i, char in enumerate(s):
  if i < start:
    continue
  if rev:
    if char == '2':
      cnt2 += 1
    else:
      ans = max(ans, min(cnt1, cnt2)*2 + 1)
      rev = False
      cnt1 = 0
      if char == '1':
        cnt1 += 1
      cnt2 = 0
  else:
    if char == '1':
      cnt1 += 1
    elif char == '/' and cnt1 > 0:
      rev = True
    else:
      cnt1 = 0
else:
  if rev and cnt2 > 0:
    ans = max(ans, min(cnt1, cnt2)*2 + 1)

print(ans)
