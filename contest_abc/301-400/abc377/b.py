cols_num = 8
cols = [list(input()) for _ in range(cols_num)]

memo_x_direction = set()
memo_y_direction = set()

for x, col in enumerate(cols) :
  for y, char in enumerate(col) :
    if char == '#' :
      memo_y_direction.add(y)
      memo_x_direction.add(x)

cnt_x = len(memo_x_direction)
cnt_y = len(memo_y_direction)

print((8 - cnt_x) * (8 - cnt_y))