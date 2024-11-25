n = int(input())
xy = [input().split() for _ in range(n)]
name_list, height_list = [list(i) for i in zip(*xy)]
idx = list(range(n))
idx.sort(key=lambda x: int(height_list[x]), reverse=True)
print(name_list[idx[1]])