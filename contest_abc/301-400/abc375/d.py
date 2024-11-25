from collections import Counter
input_s = input()
len_s = len(input_s)
ans = 0
left = [0] * 26
right = [0] * 26
for s in input_s:
  right[ord(s)-ord('A')] += 1
for i, s in enumerate(input_s):
  right[ord(s)-ord('A')] -= 1
  for j in range(26):
    ans += left[j] * right[j]
  left[ord(s)-ord('A')] += 1
print(ans)