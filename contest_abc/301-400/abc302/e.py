from bisect import insort_right, bisect_left

if __name__ == "__main__":
    n, query_num = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(query_num)]
    edges = [[] for _ in range(n)]
    for query in queries:
        if query[0] == 1:
            x, y = query[1]-1, query[2]-1
            insort_right(edges[x], y)
            insort_right(edges[y], x)
        else:
            x = query[1]-1
            connected = edges[x]
            edges[x] = []
            for y in connected:
                edges[y].pop(bisect_left(edges[y], x))
        print(sum([1 for e in edges if len(e) == 0]))
