N, m, h, k = map(int, input().split())
# sは長さNの文字列
s = input()
grid = dict()
for i in range(m):
  x, y = map(int, input().split())
  grid[(x, y)] = True

current_point = [0, 0]
for i,direction in enumerate(s):
  h -= 1
  # print(h)
  if h < 0:
    print('No')
    exit()
  if direction == 'R':
    current_point[0] += 1
  if direction == 'L':
    current_point[0] -= 1
  if direction == 'U':
    current_point[1] += 1
  if direction == 'D':
    current_point[1] -= 1
  if h < k and grid.get((current_point[0], current_point[1]), False):
    h = k
    del grid[(current_point[0], current_point[1])]
print('Yes')