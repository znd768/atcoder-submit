import sys
sys.setrecursionlimit(10 ** 6)

def get_root(idx):
    rs = [idx+1]
    nx = edges[idx]
    while nx != idx:
        rs.append(nx+1)
        nx = edges[nx]
    return rs

def dfs(i, seen):
    j = edges[i]
    if seen[j] > -1:
        return get_root(j)
    seen[j] = i
    return dfs(j, seen)

if __name__ == '__main__':
    n = int(input())
    edges = {i:v-1 for i, v in enumerate(map(int, input().split()))}
    seen = [-1] * n
    ans = dfs(0, seen)
    print(len(ans))
    print(*ans)
