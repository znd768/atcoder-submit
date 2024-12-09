n = int(input())
al = list(map(int, input().split()))
d = dict()
for idx, num in enumerate(al, start=1):
    print_num = d.get(num, -1)
    d[num] = idx
    print(print_num, end=" ")