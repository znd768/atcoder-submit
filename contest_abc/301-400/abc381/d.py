n = int(input())
a = list(map(int, input().split()))
used_chars = {}
ans = 0
tmp_ans = 0
i = 0
while i < n-1:
  if a[i] == a[i+1] and not used_chars.get(a[i], False):
    tmp_ans += 2
    used_chars[a[i]] = True
    i += 2
  else:
    ans = max(ans, tmp_ans)
    tmp_ans = 0
    if len(used_chars) > 0:
      i -= 1
    else:
      i += 1
    used_chars = {}
print(max(ans, tmp_ans))