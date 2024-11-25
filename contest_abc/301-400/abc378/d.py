h, w, k = map(int, input().split())
grid = [list(input()) for _ in range(h)]

ans = 0
mod = 10**9 + 7

visited = [[False]*w for _ in range(h)]

def run(i, j, cnt):
  global ans
  if cnt == k:
    ans += 1
    ans %= mod
    return
  visited[i][j] = True
  for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    ni, nj = i + x, j + y
    if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj]:
      if grid[ni][nj] == '.':
        run(ni, nj, cnt + 1)
  visited[i][j] = False


for i in range(h):
  for j in range(w):
    if grid[i][j] == '.':
      run(i, j, 0)

print(ans)