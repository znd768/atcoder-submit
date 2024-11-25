import math

def run(h, w, max_h, max_w, grid, visited, memo):
  if (h == max_h - 1) and (w == max_w - 1):
    return 0
  if visited[h][w]:
    return memo[h][w]
  visited[h][w] = True
  res = -math.inf
  if w + 1 < max_w:
    res = max(res, grid[h][w + 1] - run(h, w + 1, max_h, max_w, grid, visited, memo))
  if h + 1 < max_h :
    res = max(res, grid[h + 1][w] - run(h + 1, w, max_h, max_w, grid, visited, memo))
  memo[h][w] = res
  return res

def str_to_int(s):
  return 1 if s == '+' else -1

def main():
  h, w = map(int, input().split())
  grid = [list(map(str_to_int, input())) for _ in range(h)]
  visited = [[False] * w for _ in range(h)]
  memo = [[-1] * w for _ in range(h)]
  score = run(0, 0, h, w, grid, visited, memo)
  if score == 0:
    print('Draw')
  elif score > 0:
    print('Takahashi')
  else:
    print('Aoki')

if __name__ == '__main__':
  main()