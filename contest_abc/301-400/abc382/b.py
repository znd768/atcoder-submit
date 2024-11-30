n, d = map(int, input().split())
s = input()
rs = s[::-1].replace('@', '.', d)
print(rs[::-1])