n = int(input())
al = list(map(int, input().split()))
print(al.index(sorted(al, reverse=True)[1])+1)