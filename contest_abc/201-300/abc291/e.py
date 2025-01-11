from collections import deque

# トポロジカルソート

n, m = map(int, input().split())
xy = [list(map(lambda x: int(x)-1, input().split())) for _ in range(m)]

edges = [[] for _ in range(n)]
nums = [0]*n
# ver1 -> ver2
for ver1, ver2 in xy:
    # ver2に向いてる頂点を追加
    edges[ver2].append(ver1)
    # 辺が出ている頂点の辺の数をカウント
    nums[ver1] += 1

q = deque()
for i in range(n):
    if nums[i] == 0:
        # 辺を出さない頂点(= 最大)をキューに追加
        q.append(i)

output_order = [0]*n
na = n
while q:
    if len(q) > 1:
        print("No")
        exit()
    ver = q.popleft()
    output_order[ver] = na
    na -= 1
    for to in edges[ver]:
        nums[to] -= 1
        if nums[to] == 0:
            q.append(to)
print("Yes")
print(*output_order)