s = sorted(input(), reverse=True)
t = sorted(input(), reverse=True)
available = list("atcoder")
ans = True
s_contains = [0] * 26
t_contains = [0] * 26
s_joker = 0
t_joker = 0
for i in range(len(s)):
  if s[i] == "@" :
    s_joker += 1
  else:
    s_contains[ord(s[i]) - ord('a')] += 1
  if t[i] == "@" :
    t_joker += 1
  else:
    t_contains[ord(t[i]) - ord('a')] += 1
for i in range(26):
  if chr(i + ord('a')) not in available:
    if s_contains[i] != t_contains[i]:
      ans = False
      break
  else:
    if s_contains[i] > t_contains[i]:
      t_joker -= s_contains[i] - t_contains[i]
    else:
      s_joker -= t_contains[i] - s_contains[i]
    if s_joker < 0 or t_joker < 0:
      ans = False
      break
print("Yes" if ans else "No")