h, w, d = map(int, input().split())
grid = [input() for _ in range(h)]
ans = 0

def calc(i, j, s, t):
    apply_area = set()
    for x in range(h):
        for y in range(w):
            if abs(i - x) + abs(j - y) <= d and grid[x][y] == ".":
                apply_area.add((x, y))
    for x in range(h):
        for y in range(w):
            if abs(s - x) + abs(t - y) <= d and grid[x][y] == ".":
                apply_area.add((x, y))
    return len(apply_area)

for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            continue
        for s in range(i, h):
            for t in range(j, w):
                if grid[s][t] == '#':
                    continue
                ans = max(ans, calc(i, j, s, t))
print(ans)
