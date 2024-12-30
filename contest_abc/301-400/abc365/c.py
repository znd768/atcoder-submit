n, budget = map(int, input().split())
al = list(map(int, input().split()))
al.sort()
if sum(al) <= budget:
    print("infinite")
    exit()

min_budget = 0
max_budget = 10**9+1
while min_budget+1 < max_budget:
    mid_budget = (min_budget + max_budget) // 2
    tmp_sum = 0
    for val in al:
        tmp_sum += min(val, mid_budget)
    if tmp_sum == budget:
        print(mid_budget)
        exit()
    elif tmp_sum > budget:
        max_budget = mid_budget
    else:
        min_budget = mid_budget
print(min_budget)
