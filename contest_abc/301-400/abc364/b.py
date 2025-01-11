h, w = map(int, input().split())
sh, sw = map(lambda x: int(x)-1, input().split())
grid = [list(input()) for _ in range(h)]
commands = input()
moves = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

def is_valid(y, x):
    return 0 <= y < h and 0 <= x < w and grid[y][x] == "."

for command in commands:
    dy, dx = moves[command]
    ny, nx = sh + dy, sw + dx
    if is_valid(ny, nx):
        sh, sw = ny, nx
print(sh+1, sw+1)