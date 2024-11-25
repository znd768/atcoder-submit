import math

n, D = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]
seen = [0] * n
seen[0] = 1
q = [0]
while q:
    idx = q.pop(0)
    for i, x in enumerate(seen):
        if i == idx or x:
            continue
        if math.dist(xy[idx], xy[i]) <= D:
            q.append(i)
            seen[i] = 1
for x in seen:
    print('Yes' if x == 1 else 'No')
