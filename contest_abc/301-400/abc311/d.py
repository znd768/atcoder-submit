from dataclasses import dataclass
from collections import deque

@dataclass
class Point:
    x: int
    y: int

def check(p: Point, h: int, w: int, g:[[str]]) -> bool:
    return 0 < p.y < h-1 and 0 < p.x < w-1 and g[p.y][p.x] != "#"

def could_add(p: Point, g: [[str]]) -> bool:
    return g[p.y][p.x] == "."

if __name__ == '__main__':
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    start = Point(1, 1)
    stopped = set()
    mv = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    d = deque([start])
    ans = 0
    while d:
        cp = d.popleft()
        if (cp.x, cp.y) in stopped:
            continue
        stopped.add((cp.x, cp.y))
        for dx, dy in mv:
            np = Point(cp.x + dx, cp.y + dy)
            if not check(np, n, m, grid):
                continue
            while True:
                if could_add(np, grid):
                    ans += 1
                    grid[np.y][np.x] = "x"
                nnp = Point(np.x+dx, np.y+dy)
                if not check(nnp, n, m, grid):
                    break
                np = nnp
            d.append(np)
    print(ans if ans > 0 else 1)




