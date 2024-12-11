n = int(input())
lis = list(map(int, input().split()))
sum_value = sum(lis)
ans = sum_value
for bit in range(1 << n):
    tmp_lis = []
    for j in range(n):
        mask = 1 << j
        if bit & mask:
            tmp_lis.append(lis[j])
    ans = min(ans, max(sum_value - sum(tmp_lis), sum(tmp_lis)))
print(ans)