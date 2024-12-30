s = list(input())
n = len(s)
cnt = 0
cursor = 0
while True:
    if cursor == n:
        break
    if s[cursor] == "0" and cursor < n - 1 and s[cursor + 1] == "0":
        cursor += 1
    cnt += 1
    cursor += 1
print(cnt)