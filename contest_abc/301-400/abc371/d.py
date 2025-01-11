from bisect import bisect_left, bisect_right

n = int(input())
xl = list(map(int, input().split()))
pl = list(map(int, input().split()))
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

idx = list(range(n))
idx.sort(key=lambda i: xl[i])
xl.sort()
sub_sum = [0] * (n + 1)
for point, idx in enumerate(idx):
    sub_sum[point + 1] = sub_sum[point] + pl[idx]

for l, r in lr:
    l = bisect_left(xl, l)
    r = bisect_right(xl, r)
    print(sub_sum[r] - sub_sum[l])