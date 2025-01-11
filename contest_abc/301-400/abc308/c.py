n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
for num in sorted(range(n), key=lambda x: ab[x][0]/(ab[x][1]+ab[x][0]), reverse=True):
    print(num+1, end=" ")