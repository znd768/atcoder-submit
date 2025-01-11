import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
ans = []

def calc(list_a):
    if len(list_a) == n:
        ans.append(list_a)
        return
    l = 1
    if len(list_a) > 0:
        l = list_a[-1] + 10
    list_a.append(l)
    while list_a[-1]+10*(n-len(list_a)) <= m:
        lisb = list_a.copy()
        calc(list_a)
        lisb[-1] += 1
        list_a = lisb

calc([])
print(len(ans))
for a in ans:
    print(*a)
