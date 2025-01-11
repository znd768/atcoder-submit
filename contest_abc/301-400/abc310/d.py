n, num_team, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(m)]
d = [[] for _ in range(n)]
for a, b in ab:
    d[a - 1].append(b - 1)
    d[b - 1].append(a - 1)
for i in range(n):
    for j in range(num_team):