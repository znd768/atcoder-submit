n, t, p = map(int, input().split())
l = list(map(int, input().split()))

l.sort(reverse=True)
ok_cnt = 0
last_v = 0
for i, v in enumerate(l, start=1):
    if v >= t:
        ok_cnt += 1
    if i == p:
        last_v = v

if ok_cnt >= p:
    print(0)
else:
    print(t - last_v)