# 累積和を使って区間内に特定の数字があるかを判定する

n, s = map(int, input().split())
a = list(map(int, input().split()))
sub_sum = [0] * (2 * n)
for idx, val in enumerate(a+a):
    if idx == 0:
        sub_sum[idx] = val
    else:
        sub_sum[idx] = sub_sum[idx-1] + val
real_num = s % sum(a)
ans = False
d = dict()
for idx, val in enumerate(sub_sum):
    d[val] = 1
for idx, val in enumerate(sub_sum):
    if d.get(val-real_num, 0):
        ans = True
        break
print(sub_sum)
print("Yes" if ans else "No")