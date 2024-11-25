n = int(input())
grid = [list(input()) for i in range(n)]
for outline in range(n // 2):
  for _ in range((outline+1) % 4):
    col1 = [x[outline] for x in grid][outline:n-outline]
    col2 = [x[-1-outline] for x in grid][outline:n-outline]
    row1 = grid[outline][outline:n-outline]
    row2 = grid[-1-outline][outline:n-outline]
    grid[outline][outline:n-outline] = list(reversed(col1))
    for i in range(outline, n-outline) :
      grid[i][-1-outline] = row1[i-outline]
      grid[i][outline] = row2[i-outline]
    grid[-1-outline][outline:n-outline] = list(reversed(col2))
# print('--------------------')
for row in grid :
  print(''.join(row))