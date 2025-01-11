h, w, n = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]
d = {t: 1 for t in ab}
ans = h * w - n

def check(i, j):
    return 0 <= i < h and 0 <= j < w

def search(sx, sy, size):
    for x in range(size):
        for y in range(size):
            if not check(sx+x, sy+y):
                return False
            if not d.get((sx+x, sy+y), None):
                return False
    return True

for i in range(2, min(h, w)+1):
    for start_x in range(min(h, w)):
        for start_y in range(min(h, w)):
            ans += search(start_x, start_y, i)
print(ans)
