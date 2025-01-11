n = int(input())
al = list(map(int, input().split()))
memo = [[] for _ in range(n)]
ans_list = [-1]*n
for idx, num in enumerate(al):
    memo[num-1].append(idx)
    if len(memo[num-1]) == 2:
        ans_list[num-1] = idx
print(*sorted(range(1, n+1), key=lambda x: ans_list[x-1]))