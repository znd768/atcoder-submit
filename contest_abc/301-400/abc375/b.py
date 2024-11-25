n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i, (x, y) in enumerate(xy):
  if i == 0 :
    prev_x, prev_y = 0, 0
  else:
    prev_x, prev_y = xy[i-1]
  ans += ((x-prev_x) ** 2 + (y-prev_y) ** 2) ** (1 / 2)
else:
  ans += (xy[-1][0] ** 2 + xy[-1][1] ** 2) ** (1 / 2)
print(ans)