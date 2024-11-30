from bisect import bisect_left

n, m = map(int, input().split())
a_l = list(map(int, input().split()))
b_l = list((map(int, input().split())))
ans_l = [-1] * m
memo = dict()

min_v = 10**9
for i, v in enumerate(a_l, start=1):
    if v >= min_v:
        continue
    memo[v] = i
    min_v = v

ll = sorted(memo.keys())

for i, v in enumerate(b_l):
    k = bisect_left(ll, v)
    if k == 0 and ll[k] != v:
        continue
    if k == len(ll) or ll[k] != v:
        k -= 1
    ans_l[i] = memo[ll[k]]

# output
print(*ans_l, sep="\n")