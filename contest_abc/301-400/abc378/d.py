from collections import deque
def check_valid_point(h, w, x, y):
  return 0 <= x < h and 0 <= y < w

if __name__ == '__main__':
  row_num, col_num, k = map(int, input().split())
  grid = [list(input()) for _ in range(row_num)]

  ans = 0
  moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  for i in range(row_num):
    for j in range(col_num):
      if grid[i][j] == '.':
        memo = [[-1] * col_num for _ in range(row_num)]
        d = deque()
        d.append((i, j))
        memo[i][j] = 0
        tmp_ans = 0
        while d:
          x, y = d.popleft()
          for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if check_valid_point(row_num, col_num, nx, ny) and grid[nx][ny] == '.' and memo[nx][ny] == -1:
              d.append((nx, ny))
              memo[nx][ny] = memo[x][y] + 1
              if memo[x][y] + 1 == k:
                tmp_ans += 1
          if memo[x][y] == k - 1:
            ans += tmp_ans
            break
  print(ans)