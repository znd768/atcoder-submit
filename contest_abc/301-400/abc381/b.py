s = input()
if len(s) % 2 == 1:
  print('No')
  exit()
used_chars = dict()
for i, char in enumerate(s):
  if used_chars.get(char, 0) > 2:
    print('No')
    exit()
  used_chars[char] = used_chars.get(char, 0) + 1
  if i % 2 == 0:
    if char != s[i+1]:
      print('No')
      exit()

for k, v in used_chars.items():
  if v != 2:
    print('No')
    exit()
print('Yes')