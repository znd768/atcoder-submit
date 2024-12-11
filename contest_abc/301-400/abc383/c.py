from collections import deque
h, w, distance = map(int, input().split())
grid = [input() for _ in range(h)]
each_distance = [[10**19] * w for _ in range(h)]

def valid_position(x, y):
    return 0 <= x < h and 0 <= y < w and grid[x][y] != '#' and each_distance[x][y] == 10**19

q = deque()
for row_num, row in enumerate(grid):
    for col_num, col in enumerate(row):
        if col == "H":
            each_distance[row_num][col_num] = 0
            q.append((row_num, col_num))
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
current_d = 0
while len(q) > 0:
    current_x, current_y = q.popleft()
    for move_x, move_y in moves:
        next_x, next_y = current_x + move_x, current_y + move_y
        if valid_position(next_x, next_y):
            q.append((next_x, next_y))
            each_distance[next_x][next_y] = each_distance[current_x][current_y] + 1
ans = 0
for i in range(h):
    for j in range(w):
        if each_distance[i][j] <= distance:
            ans += 1

print(ans)