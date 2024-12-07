# TLE

import sys
sys.setrecursionlimit(10 ** 6)

h, w, distance = map(int, input().split())
grid = [input() for _ in range(h)]
apply_area = [[False] * w for _ in range(h)]

def calc(x, y, dis):
    if not (0 <= x < h and 0 <= y < w):
        return
    if grid[x][y] == "#":
        return
    global apply_area
    if grid[x][y] == ".":
        apply_area[x][y] = True
    elif grid[x][y] == "H":
        apply_area[x][y] = True
        if dis != distance:
            return
    if dis > 0:
        calc(x+1, y, dis-1)
        calc(x-1, y, dis-1)
        calc(x, y+1, dis-1)
        calc(x, y-1, dis-1)

for i in range(h):
    for j in range(w):
        if grid[i][j] == "H":
            calc(i, j, distance)

ans = 0
for row in apply_area:
    ans += sum(row)
print(ans)