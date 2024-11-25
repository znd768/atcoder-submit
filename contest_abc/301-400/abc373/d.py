import sys
sys.setrecursionlimit(10 ** 7)
import numpy as np

num_of_vertex, number_of_edges = map(int, input().split())
uvw = [list(map(int, input().split())) for _ in range(number_of_edges)]
value_list = np.array([-1] * num_of_vertex, dtype=np.int64)
# uvw[i][2] + value_list[uvw[i][0]] = value_list[uvw[i][1]]

graph = [[] for _ in range(num_of_vertex)]
for u, v, w in uvw:
  graph[u - 1].append((v - 1, w))
  graph[v - 1].append((u - 1, -w))

seen_vertex = [False] * num_of_vertex

def dfs(vertex: int, value: int) -> bool:
  if seen_vertex[vertex]:
    return True
  seen_vertex[vertex] = True
  value_list[vertex] = value
  for next_vertex, next_value in graph[vertex]:
    dfs(next_vertex, value + next_value)

if __name__ == '__main__':
  for i in range(num_of_vertex):
    if not seen_vertex[i]:
      value_list[i] = 0
      dfs(i, 0)
  print(' '.join(map(str, value_list)))
