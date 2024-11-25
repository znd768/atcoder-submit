s_initial = input()
t = input()
x = []
s = s_initial
str_num = len(s)
while s != t :
  l = []
  for i in range(str_num) :
    if i == 0 :
      replaced = t[0] + s[1:]
    elif i == str_num - 1:
      replaced = s[:-1] + t[-1]
    else :
      replaced = s[:i] + t[i] + s[i + 1:]
    if replaced != s :
      l.append(replaced)
  s = sorted(l)[0]
  x.append(s)

print(len(x))
print('\n'.join(x)) if len(x) > 0 else None
