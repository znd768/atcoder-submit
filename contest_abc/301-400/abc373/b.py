s = list(input())
ans = 0

initial_position = s.index('A')
for i in range(1, len(s)):
  ans += abs(initial_position - s.index(chr(65 + i)))
  initial_position = s.index(chr(65 + i))

print(ans)
