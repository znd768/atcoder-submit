import math

n = int(input())
if n == 1:
    print(0)
    exit()

n -= 1
digits = 0
while True:
    digits += 1
    l = (digits+1)//2
    num = 9
    for i in range(l):
        num *= 10
        if n > num:
            n -= num
            continue
    n += num//9 - 1
    s = str(n)
    rs = s[::-1]
    if len(s) % 2 == 1:
        s = s[:-1]
    print(s+rs)
    exit()