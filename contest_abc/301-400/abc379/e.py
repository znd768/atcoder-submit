n = int(input())
s = int(input())
ans = 0
cnt = 1
x = 1
while s != 0:
  num = s % 10
  s //= 10
  ans += num * x * (n-cnt+1)
  x += 10**cnt
  cnt += 1

print(ans)