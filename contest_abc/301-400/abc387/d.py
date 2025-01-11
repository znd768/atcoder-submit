from collections import deque
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Grid:
    height: int
    width: int
    rows: list[str]

h, w = map(int, input().split())
g: Grid = Grid(h, w, [input() for _ in range(h)])

def check(t: int, s: int, grid: Grid) -> bool:
    return 0 <= t < grid.height and 0 <= s < grid.width and grid.rows[t][s] in (".", "G")

start = Point(0, 0)
goal = Point(h-1, w-1)
for row_num, row in enumerate(g.rows):
    if "S" in row:
        start.x, start.y = row_num, row.index("S")
    if "G" in row:
        goal.x, goal.y = row_num, row.index("G")

dp = [[[-1]*2 for _ in range(w)] for _ in range(h)]
dp[start.x][start.y][0] = 0
dp[start.x][start.y][1] = 0

d = deque([start])
moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

while d:
    p: Point = d.popleft()
    for idx, (dx, dy) in enumerate(moves):
        nx, ny = p.x+dx, p.y+dy
        if not check(nx, ny, g):
            continue
        if idx <= 1 and dp[p.x][p.y][1] >= 0 and dp[nx][ny][0] == -1:
            dp[nx][ny][0] = dp[p.x][p.y][1]+1
            d.append(Point(nx, ny))
        elif idx > 1 and dp[p.x][p.y][0] >= 0 and dp[nx][ny][1] == -1:
            dp[nx][ny][1] = dp[p.x][p.y][0]+1
            d.append(Point(nx, ny))

if dp[goal.x][goal.y][0] > 0 and dp[goal.x][goal.y][1] > 0:
    print(min(dp[goal.x][goal.y]))
elif dp[goal.x][goal.y][0] > 0:
    print(dp[goal.x][goal.y][0])
elif dp[goal.x][goal.y][1] > 0:
    print(dp[goal.x][goal.y][1])
else:
    print(-1)