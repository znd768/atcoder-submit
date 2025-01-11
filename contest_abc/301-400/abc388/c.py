from bisect import bisect_left

n = int(input())
al = list(map(int, input().split()))
al.sort()
ans = 0
for idx, length in enumerate(al):
    find = bisect_left(al, length*2)
    ans += n - find
print(ans)