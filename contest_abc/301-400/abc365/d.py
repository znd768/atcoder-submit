n = int(input())
s = input()
pattern = {"R": "P", "P": "S", "S": "R"}

dp = [[0] * (n+1) for _ in range(3)]
for idx, char in enumerate(s, start=1):
    for j, p in enumerate("RPS"):
        if p == char:
            dp[j][idx] = max(dp[(j+1)%3][idx-1], dp[(j+2)%3][idx-1])
        elif p == pattern[char]:
            dp[j][idx] = max(dp[(j+1)%3][idx-1], dp[(j+2)%3][idx-1]) + 1
        else:
            dp[j][idx] = -10
print(max(dp[0][n], dp[1][n], dp[2][n]))