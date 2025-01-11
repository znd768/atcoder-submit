from bisect import insort_right, bisect_left

n, k, q = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(q)]
entries = [0]*n
numbers = [0]*n
current = 0
for x, y in xy:
    x -= 1
    if numbers[x] < 0 and numbers[x] < entries[k-1]:
        current -= numbers[x]
    if -y < entries[k-1]:
        current += -y -entries[k-1]
        insort_right(entries, -y)
    numbers[x] = -y
    print(-current)