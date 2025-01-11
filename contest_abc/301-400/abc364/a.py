n = int(input())
sl = [input() for _ in range(n)]
prev = sl[0]
num = n - 1
for s in sl[1:]:
    num -= 1
    if prev == s and prev == "sweet":
        break
    prev = s
print("Yes" if num == 0 else "No")