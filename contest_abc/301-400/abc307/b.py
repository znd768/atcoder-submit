import itertools

n = int(input())
sl = [input() for _ in range(n)]

for x, y in itertools.combinations(range(n), 2):
    s = sl[x] + sl[y]
    if s == s[::-1]:
        print("Yes")
        exit()
    s = sl[y] + sl[x]
    if s == s[::-1]:
        print("Yes")
        exit()
print("No")