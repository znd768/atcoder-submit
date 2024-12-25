a, b, c = input().split()
n = int(a)
s = input()
ans = []
for i, char in enumerate(s):
    if char != b:
        ans.append(c)
    else:
        ans.append(char)
print("".join(ans))