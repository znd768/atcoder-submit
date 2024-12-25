a, b, c = map(int, input().split())
ans = False
if a == b and b == c:
    ans = True
if a + b == c:
    ans = True
if b + c == a:
    ans = True
if a + c == b:
    ans = True
print("Yes" if ans else "No")