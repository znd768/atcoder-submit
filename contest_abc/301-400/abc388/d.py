n = int(input())
al = list(map(int, input().split()))
bl = al.copy()
could_distribute = [0] * (n+1)
if al[0] != 0:
    could_distribute[1] = 1
    could_distribute[min(al[0]+1, n)] = -1
a = 0
for i in range(1, n):
    a += could_distribute[i]
    if al[i] + a > 0:
        could_distribute[i+1] += 1
        could_distribute[min(i+1+a+al[i], n)] -= 1
acc = 0
for i in range(n):
    acc += could_distribute[i]
    bl[i] = max(0, bl[i] + acc - (n - i - 1))
print(*bl)