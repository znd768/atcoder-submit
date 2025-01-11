import itertools

def input_graph(num):
    graph = [[False]*num for _ in range(num)]
    edge_num = int(input())
    for i in range(edge_num):
        s, t = map(lambda x: int(x)-1, input().split())
        graph[s][t] = True
        graph[t][s] = True
    return graph

if __name__ == "__main__":
    n = int(input())
    g1 = input_graph(n)
    g2 = input_graph(n)
    costs = [list(map(int, input().split())) for _ in range(n-1)]
    ans = 10**9
    # 頂点の並び替えを全探索
    for p in itertools.permutations(range(n)):
        tmp = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if g2[i][j] != g1[p[i]][p[j]]:
                    tmp += costs[i][j-i-1]
        ans = min(ans, tmp)

    print(ans)