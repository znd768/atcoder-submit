n, d = map(int, input().split())
str_list = [input() for _ in range(n)]
ans = 0
tmp = 0
for l in zip(*str_list):
    today = "x" not in l
    if today:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 0
ans = max(ans, tmp)
print(ans)