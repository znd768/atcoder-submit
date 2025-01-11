n, m = map(int, input().split())
dp = [[0]*2 for _ in range(n)]
dp[0][0] = 1
mod = 998244353
for i in range(1, n):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = dp[i-1][0] * (m-1)
    dp[i][1] += dp[i-1][1] * (m-2)
    dp[i][1] %= mod
print(dp[n-1][1] * m % mod)