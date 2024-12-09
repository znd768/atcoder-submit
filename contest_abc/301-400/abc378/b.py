n = int(input())
qr = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
td = [list(map(int, input().split())) for _ in range(q)]

for i, date in td:
    i -= 1
    div_num, mod = qr[i]
    x, y = divmod(date, div_num)
    if y <= mod:
        print(x*div_num + mod)
    else:
        print(div_num*(x + 1) + mod)