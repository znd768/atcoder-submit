n = int(input())
sl = [input() for _ in range(n)]
max_len = 0
for row in sl:
    max_len = max(max_len, len(row))
new_sl = []
for row in reversed(sl):
    new_sl.append(list(row + "*"*(max_len-len(row))))
for rows in zip(*new_sl):
    print("".join(rows).rstrip("*"))