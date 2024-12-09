# WA
h, w, k = map(int, input().split())
grid = [list(input()) for _ in range(h)]

ans = 0
memo = [[-1] * w for _ in range(h)]

def check_valid_point(h, w, x, y):
  return 0 <= x < w and 0 <= y < h

def search(x, y, cnt):
  global memo
  if not check_valid_point(h, w, x, y):
    return 0
  if grid[y][x] == "#":
    return 0
  if memo[y][x] != -1:
    return 0
  memo[y][x] = cnt
  search(x+1, y, cnt + 1)
  search(x-1, y, cnt + 1)
  search(x, y+1, cnt + 1)
  search(x, y-1, cnt + 1)

for y, row in enumerate(grid):
  for x, point in enumerate(row):
    if point == "#":
      continue
    else:
      memo = [[-1] * w for _ in range(h)]
      search(x, y, 0)
      for row2 in memo:
        ans += row2.count(k)

print(ans)