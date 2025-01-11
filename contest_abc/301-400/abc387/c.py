l, r = input().split()
ans = sum([i**(len(r)-1) for i in range(1, 10)])

def output(num, max_num):
    digits = len(str(num))
    return min(max_num, int(str(num)[0])) * max_num**(digits-1)

for idx, char in enumerate(r):
    num = int(char)
    if idx == 0 and num > 1:
        for i in range(num-1, 0, -1):
            ans += i**(len(r)-1)
    else:
        ans += 1
    for i in range(len(r)-1):
        tmp = r[0]
        for j in range(int(r[0])):
            ans += j**(len(r)-1-i)
