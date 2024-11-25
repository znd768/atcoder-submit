s = input()
t = input().lower()
ans = 'No'
if s.find(t[0]) != -1 and s.find(t[1]) != -1 :
  s = s[s.index(t[0])+1:]
  if s.find(t[1]) != -1 :
    s = s[s.index(t[1])+1:]
    if t[2] == 'x' :
      ans = 'Yes'
    elif s.find(t[2]) != -1 :
      ans = 'Yes'

print(ans)