h, w, q = map(int, input().split())
query_list = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(q)]
grid = [True for _ in range(h * w)]
for i, j in query_list:
  if grid[i * w + j]:
    grid[i * w + j] = False
  else:
    up, down, left, right = False, False, False, False
    u = i + 1
    while not up and u < h :
      if grid[u * w + j]:
        up = True
        grid[u * w + j] = False
      u += 1
    d = i - 1
    while not down and d >= 0:
      if grid[d * w + j]:
        down = True
        grid[d * w + j] = False
      d -= 1
    l = j - 1
    while not left and l >= 0:
      if grid[i * w + l]:
        left = True
        grid[i * w + l] = False
      l -= 1
    r = j + 1
    while not right and r < w:
      if grid[i * w + r]:
        right = True
        grid[i * w + r] = False
      r += 1
print(sum(grid))