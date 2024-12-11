from collections import deque
n = int(input())
height = list(map(int, input().split()))
ans = [0] * n
d = deque()
for i in range(n-1, -1, -1):
    ans[i] = len(d)
    while len(d) > 0 and d[-1] < height[i]:
        d.pop()
    d.append(height[i])

print(" ".join(map(str, ans)))