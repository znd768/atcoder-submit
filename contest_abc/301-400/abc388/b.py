n, d = map(int, input().split())
tl = [tuple(map(int, input().split())) for _ in range(n)]
for i in range(1, d+1):
    print(max([t*(l+i) for t, l in tl]))