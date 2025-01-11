from queue import Queue
import math
num_of_vertex, num_of_edge = map(int, input().split())
edges_input = [list(map(lambda x: int(x)-1, input().split())) for _ in range(num_of_edge)]
edges = [[] for _ in range(num_of_vertex)]
for u, v in edges_input:
  edges[u].append(v)
max_num = math.inf
dist = [max_num] * num_of_vertex
ans = math.inf
q = Queue()
q.put(0)

dist[0] = 0
while not q.empty():
  u = q.get()
  for v in edges[u]:
    if dist[v] != max_num:
      continue
    dist[v] = dist[u] + 1
    q.put(v)

for u, v in edges_input:
  if v == 0:
    ans = min(ans, dist[u]+1)

print(ans) if ans != math.inf else print(-1)
