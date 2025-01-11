n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

mod = 998244353

dp = [[0]*2 for _ in range(n)]

for idx, (val1, val2) in enumerate(l):
    if idx == 0:
        dp[idx][0] = 1
        dp[idx][1] = 1
        continue
    if val1 not in l[idx-1]:
        dp[idx][0] = (dp[idx-1][0]+dp[idx-1][1]) % mod
    elif val1 != l[idx-1][0]:
        dp[idx][0] = dp[idx-1][0]
    elif val1 != l[idx-1][1]:
        dp[idx][0] = dp[idx-1][1]
    else:
        print(0)
        exit()
    if val2 not in l[idx-1]:
        dp[idx][1] = (dp[idx-1][0]+dp[idx-1][1]) % mod
    elif val2 != l[idx-1][0]:
        dp[idx][1] = dp[idx-1][0]
    elif val2 != l[idx-1][1]:
        dp[idx][1] = dp[idx-1][1]
    else:
        print(0)
        exit()
print((dp[n-1][0]+dp[n-1][1]) % mod)