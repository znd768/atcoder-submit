n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
dp = [[-10**9]*2 for _ in range(n+1)]
dp[0][0] = 0 # healthy
dp[0][1] = 0 # poisoned
for idx, (x, y) in enumerate(xy, start=1):
    if x == 0:
        # safe
        dp[idx][0] = max(dp[idx-1][0], dp[idx-1][0]+y, dp[idx-1][1]+y)
        dp[idx][1] = dp[idx-1][1]
    else:
        # poison
        dp[idx][0] = dp[idx-1][0]
        dp[idx][1] = max(dp[idx-1][0]+y, dp[idx-1][1])
print(max(dp[n]))