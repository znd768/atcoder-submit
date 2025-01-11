from collections import defaultdict

n, m, sx, sy = map(int, input().split())
sx -= 1
sy -= 1
xy = [list(map(lambda x: int(x)-1, input().split())) for _ in range(n)]
moves = [list(input().split()) for _ in range(m)]

def commands(c, num):
    if c == "U":
        return 0, num
    elif c == "D":
        return 0, -num
    elif c == "L":
        return -num, 0
    elif c == "R":
        return num, 0

ans = 0
cx, cy = sx, sy
moved = []
for command, d in moves:
    dx, dy = commands(command, int(d)-1)
    moved.append((cx, cy, cx+dx, cy+dy))
    cx += dx
    cy += dy


