import itertools, math
num, velo1, velo2 = map(int, input().split())
xyxy = [list(map(int, input().split())) for _ in range(num)]
ans = math.inf

for bit in range(1 << num):
    for x in itertools.permutations(range(num)):
        prev_x, prev_y = 0, 0
        now = 0
        for line in x:
            x1, y1, x2, y2 = xyxy[line]
            if bit & (1 << line):
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            now += math.dist((x1, y1), (x2, y2)) / velo2
            now += math.dist((prev_x, prev_y), (x1, y1)) / velo1
            prev_x = x2
            prev_y = y2
        ans = min(ans, now)
print(ans)