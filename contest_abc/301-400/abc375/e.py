n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
power_sum = sum([b for _, b in ab])
if power_sum % 3 != 0:
  print(-1)
  exit()
ideal = power_sum // 3
INF = 10**9
dp = [[[INF] * (ideal+1) for _ in range((ideal+1))] for _ in range(n+1)]

for i in range(n):
  for j in range(ideal + 1):