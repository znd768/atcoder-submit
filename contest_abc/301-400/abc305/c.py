h, w = map(int, input().split())
grid = [input() for _ in range(h)]

first = 0
for i, row in enumerate(grid):
    if '#' in row:
        first = i
        break
while True:
    if grid[first] != grid[first + 1]:
        next_line = grid[first].count('#') > grid[first + 1].count('#')
        if next_line:
            print(first+2, end=' ')
        else:
            print(first+1, end=' ')
        for i, (p, q) in enumerate(zip(grid[first], grid[first + 1])):
            if p != q:
                print(i+1)
        break
    first += 1