p, q = input().split()
l = [0, 3, 1, 4, 1, 5, 9]
sl = []
for i, d in enumerate(l):
    sl.append(d)
    if i != 0:
        sl[i] += sl[i - 1]
x, y = map(lambda z: ord(z) - ord('A'), [p, q])
print(abs(sl[y] - sl[x]))