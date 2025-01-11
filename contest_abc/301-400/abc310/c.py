n = int(input())
sl = {}
for i in range(n):
    s = input()
    if s > s[::-1]:
        s = s[::-1]
    if sl.get(s, 0) > 0:
        sl[s] += 1
    else:
        sl[s] = 1
print(len(sl))