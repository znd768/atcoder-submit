from collections import deque
n = int(input())
a = list(map(int, input().split()))
cursor = 0
used_chars = dict()
chars_index = deque()
tmp_ans = 0
ans = 0
while cursor + 1 < n:
  if a[cursor] == a[cursor + 1] and used_chars.get(a[cursor], 0) == 0:
    used_chars[a[cursor]] = 2
    chars_index.append(a[cursor])
    cursor += 2
    tmp_ans += 1
  elif tmp_ans > 0 and used_chars.get(a[cursor], 0) != 0:
    tmp_ans -= 1
    char = chars_index.popleft()
    used_chars[char] = 0
    chars_index.append(char)
  else:
    if cursor != 0 and a[cursor - 1] == a[cursor]:
      cursor -= 1
    else:
      cursor += 1
    ans = max(ans, tmp_ans*2)
    tmp_ans = 0
    used_chars.clear()
ans = max(ans, tmp_ans*2)
print(ans)