n = int(input())
s = list(input())
ans = 0
memo = 1
for idx, num in enumerate(reversed(s)):
  ans += int(num) * memo * (n-idx)
  memo = memo*10 + 1
  # print(memo)
  # ans += int(num) * (idx+1) * (10 ** (n - idx - 1))
print(ans)