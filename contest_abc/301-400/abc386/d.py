n, m = map(int, input().split())
l = [list(input().split()) for _ in range(m)]

memo_b_x = dict()
memo_b_y = dict()
memo_w_x = dict()
memo_w_y = dict()

ans = True
for x, y, char in l:
    x, y = int(x)-1, int(y)-1
    if char == "B":
        if memo_b_x.get(x, -1) < y:
            memo_b_x[x] = y
        if memo_b_y.get(y, -1) < x:
            memo_b_y[y] = x
        if memo_w_x.get(x, 10**9) < y:
            ans = False
            break
        if memo_w_y.get(y, 10**9) < x:
            ans = False
            break
    elif char == "W":
        if memo_w_x.get(x, 10**9) > y:
            memo_w_x[x] = y
        if memo_w_y.get(y, 10**9) > x:
            memo_w_y[y] = x
        if memo_b_x.get(x, -1) > y:
            ans = False
            break
        if memo_b_y.get(y, -1) > x:
            ans = False
            break
if ans:
    print("Yes")
else:
    print("No")
print(memo_b_x)
print(memo_b_y)
print(memo_w_x)
print(memo_w_y)