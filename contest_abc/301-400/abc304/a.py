n = int(input())
l = [input().split() for _ in range(n)]
_, age_list1 = [list(x) for x in zip(*l)]
age_list2 = list(map(int, age_list1))
idx = age_list2.index(min(age_list2))
output = l[idx:] + l[:idx]
for name, _ in output:
    print(name)