import math
n = int(input())
ans = []
while n > 0:
    x = math.floor(math.log(n, 3))
    ans.append(x)
    n -= math.pow(3, x)
print(len(ans))
print(*ans)