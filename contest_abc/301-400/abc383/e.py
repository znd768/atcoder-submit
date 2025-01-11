from collections import Counter

class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = []
        self.parent = list(range(size))
        self.rank = [0] * size
    def add_vertex(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges.append((u, v, weight))
    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
    def kruskal(self):
        result = []
        self.edges = sorted(self.edges, key=lambda x: x[2])
        for u, v, weight in self.edges:
            x = self.find(u)
            y = self.find(v)
            if x != y:
                result.append((u, v, weight))
                self.union(x, y)
        return result
# input
num_vertex, num_edge, num_item = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(num_edge)]
list_a = [list(map(lambda x: int(x)-1, input().split())) for _ in range(num_item)]
list_b = [list(map(lambda x: int(x)-1, input().split())) for _ in range(num_item)]
count_a = Counter(list_a)
count_b = Counter(list_b)

#solve
g = Graph(num_vertex)
for u, v, weight in edges:
    g.add_vertex(u-1, v-1, weight)


#output