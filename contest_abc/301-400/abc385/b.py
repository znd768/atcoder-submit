h, w, x, y = map(int, input().split())
rows = [input() for _ in range(h)]
t = input()
current_x = x - 1
current_y = y - 1

moves = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
passed_house_num = 0
passed_houses = dict()

def is_valid_xy(px, py):
    return 0 <= px < h and 0 <= py < w and rows[px][py] != "#"

for i, char in enumerate(t):
    move_x, move_y = moves[char]
    if is_valid_xy(current_x + move_x, current_y + move_y):
        current_x, current_y = current_x + move_x, current_y + move_y
    if rows[current_x][current_y] == "@" and passed_houses.get((current_x, current_y), 0) == 0:
        passed_house_num += 1
        passed_houses[(current_x, current_y)] = 1
    # print(f"{i = } {current_x = } {current_y = }")

print(current_x+1, current_y+1, passed_house_num)